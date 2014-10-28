/*
This simple program creates a TCP socket and waits for a connection.
After the accept call returnes, it reads 8 bytes from the socket and
prints them on stdout.

usage: receive listen_port
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
