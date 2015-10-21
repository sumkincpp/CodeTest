RUN cd /opt && wget http://search.cpan.org/CPAN/authors/id/S/SH/SHAY/perl-5.20.2.tar.gz && \
    tar -xzvf perl-5.20.2.tar.gz && cd perl-5.20.2 && sh Configure -des -A ccflags="-fPIC" && \
    make && make test && make install
