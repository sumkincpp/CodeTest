RUN cd /opt && wget http://sourceforge.net/projects/boost/files/boost/1.56.0/boost_1_56_0.tar.gz && \
    tar -xzvf boost_1_56_0.tar.gz
    
RUN cd /opt/boost_1_56_0 && \
    ./bootstrap.sh --prefix=/usr/local && \
    ./bjam --layout=system install; true; rm -rf /opt/boost_1_56 
