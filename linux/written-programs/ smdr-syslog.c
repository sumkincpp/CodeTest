#include <stdio.h>
#include <stdlib.h>
#include <syslog.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define LISTEN_PORT 3000
#define BUF_SIZE 1000

int port = LISTEN_PORT;
int log_level = LOG_INFO;
int log_facility = LOG_USER;

void listen_loop() {
	int s,c,n;
	struct sockaddr_in addr;
	ssize_t nread;
	char buf[BUF_SIZE];
	struct protoent *entry = getprotobyname("tcp");
	s = c = n = 0;

	// printf("protoent %s %d\n", entry->p_name, entry->p_proto );
	s = socket( AF_INET, SOCK_STREAM, entry->p_proto );
	if (s==-1) 
	{
		perror("Can't open socket.\n");
		exit(1);
	}

	memset( &addr, 0, sizeof(addr) );

	addr.sin_family = AF_INET;
	addr.sin_port = htons(3000);
	addr.sin_addr.s_addr = htonl(INADDR_ANY);

	if ( -1 == bind(s, (struct sockaddr *) &addr, sizeof(addr) ) ) {
		perror("bind failed");
		close(s);
		exit(1);
	}

	if (-1 == listen( s, 10 )) {
		perror("can't listen");
		close(s);
		exit(1);
	}

	for(;;) 
	{
		int cfd = accept( s, NULL, NULL );
		if ( 0 > cfd ) 
		{
			perror("accept failed");
			close(s);
			exit(1);
		}
		
		nread = read( cfd, buf, BUF_SIZE-1 );
		buf[nread-1] = '\0';
		syslog( log_level, "%s", buf );

		if (-1 == shutdown( cfd, SHUT_RDWR ))
		{
			perror("");
			close(cfd);
			close(s);
			exit(1);
		}
		close(cfd);
	}
}

void main( int argc, char * argv[] ) {
	openlog( "[smdr-syslog]", 0, log_facility);
	syslog( log_level, "%s", "smdr-syslog starting" );
	listen_loop();
	closelog();
}

// http://riceball.com/d/content/smdr-logger-ip-office-and-other-pbxs
