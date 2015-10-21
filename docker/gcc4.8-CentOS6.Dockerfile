# * C++11 compliant compiler and related tools from CentOS's port of RHEL's
#    devtools (http://people.centos.org/tru/devtools-2/)
RUN curl http://people.centos.org/tru/devtools-2/devtools-2.rep o> \
         /etc/yum.repos.d/devtools-2.repo && \
    yum install --setopt=keepcache=0 -y \
                devtoolset-2-gcc-c++ \
                devtoolset-2-binutils && \
    ln -s /opt/rh/devtoolset-2/root/usr/bin/as /usr/local/bin/as && \
    ln -s /opt/rh/devtoolset-2/root/usr/bin/gcc /usr/bin/gcc && \
    ln -s /opt/rh/devtoolset-2/root/usr/bin/cc /usr/bin/cc && \
    ln -s /opt/rh/devtoolset-2/root/usr/bin/g++ /usr/bin/g++ && \
    ln -s /opt/rh/devtoolset-2/root/usr/bin/c++ /usr/bin/c++
