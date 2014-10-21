// tcp checksum

/*
C++ code to find the tcp checksum of a packet which has to use the awful pseudo-header idea.
This uses linux/(non bsd) interpretation of packets
This code borrows from other places and their ideas.
sysnet.ucsd.edu/~cfleizac/iptcphdr.html
*/

// thanx to http://seclists.org/lists/bugtraq/1999/Mar/0057.html
struct tcp_pseudo /*the tcp pseudo header*/
{
  __u32 src_addr;
  __u32 dst_addr;
  __u8 zero;
  __u8 proto;
  __u16 length;
} pseudohead;


long get_tcp_checksum(struct iphdr * myip, struct tcphdr * mytcp) {
  
  u16 total_len = ntohs(myip->tot_len);
  
  int tcpopt_len = mytcp->doff*4 - 20;
  int tcpdatalen = total_len - (mytcp->doff*4) - (myip->ihl*4);
  
  pseudohead.src_addr=myip->saddr;
  pseudohead.dst_addr=myip->daddr;
  pseudohead.zero=0;
  pseudohead.proto=IPPROTO_TCP;
  pseudohead.length=htons(sizeof(struct tcphdr) + tcpopt_len + tcpdatalen);
  
  int totaltcp_len = sizeof(struct tcp_pseudo) + sizeof(struct tcphdr) + tcpopt_len + tcpdatalen;
  unsigned short * tcp = new unsigned short[totaltcp_len];
  
  
  memcpy((unsigned char *)tcp,&pseudohead,sizeof(struct tcp_pseudo));
  memcpy((unsigned char *)tcp+sizeof(struct tcp_pseudo),(unsigned char *)mytcp,sizeof(struct tcphdr));
  memcpy((unsigned char *)tcp+sizeof(struct tcp_pseudo)+sizeof(struct tcphdr), (unsigned char *)myip+(myip->ihl*4)+(sizeof(struct tcphdr)), tcpopt_len);
  memcpy((unsigned char *)tcp+sizeof(struct tcp_pseudo)+sizeof(struct tcphdr)+tcpopt_len, (unsigned char *)mytcp+(mytcp->doff*4), tcpdatalen);
  
  /*      printf("pseud length: %d\n",pseudohead.length);
  printf("tcp hdr length: %d\n",mytcp->doff*4);
  printf("tcp hdr struct length: %d\n",sizeof(struct tcphdr));
  printf("tcp opt length: %d\n",tcpopt_len);
  printf("tcp total+psuedo length: %d\n",totaltcp_len);
  
  fflush(stdout);
  
  printf("tcp data len: %d, data start %u\n", tcpdatalen,mytcp + (mytcp->doff*4));
  */
  
  
   return checksum(tcp,totaltcp_len);

}

long checksum(unsigned short *addr, unsigned int count) {
  /* Compute Internet Checksum for "count" bytes
  *         beginning at location "addr".
  */
  register long sum = 0;
  
  
  while( count > 1 )  {
  /*  This is the inner loop */
     sum += * addr++;
     count -= 2;
  }
  /*  Add left-over byte, if any */
  if( count > 0 )
     sum += * (unsigned char *) addr;
  
  /*  Fold 32-bit sum to 16 bits */
  while (sum>>16)
  sum = (sum & 0xffff) + (sum >> 16);
  
  return ~sum;
}
