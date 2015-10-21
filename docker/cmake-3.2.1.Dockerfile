RUN cd /opt && wget http://www.cmake.org/files/v3.2/cmake-3.2.1.tar.gz && \
    tar -xzvf cmake-3.2.1.tar.gz && \
    cd cmake-3.2.1 && cd /opt/cmake-3.2.1 && ls && ./configure && \
    make && make install && rm -rf cmake-3.2.1
