RUN cd /opt && wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz && \
    tar xvf autoconf-2.69.tar.gz && \
    cd autoconf-2.69 && ./configure && make && make install && cd .. && rm -rf /opt/autoconf-2.69

RUN cd /opt && wget http://ftp.gnu.org/gnu/automake/automake-1.14.tar.gz && \
    tar xvf automake-1.14.tar.gz && \
    cd automake-1.14 && ./configure && make && make install && cd .. && rm -rf /opt/automake-1.14

RUN cd /opt && wget http://ftp.gnu.org/gnu/bison/bison-3.0.4.tar.gz && \
    tar xvf bison-3.0.4.tar.gz && \
    cd bison-3.0.4 && ./configure && make && make install && cd .. && rm -rf /opt/bison-3.0.4

RUN cd /opt && git clone https://git-wip-us.apache.org/repos/asf/thrift.git && \
    cd thrift && ./bootstrap.sh && ./configure --with-lua=no && \
    make && make install
