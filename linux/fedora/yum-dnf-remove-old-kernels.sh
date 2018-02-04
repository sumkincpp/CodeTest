
Query kernels ->
# rpm -q kernel

Leave only 5 latest kernels ->
# dnf install yum-utils
# package-cleanup --oldkernels --count=5

/etc/yum.conf, /etc/dnf/dnf.conf
installonly_limit=5


# DNF approach, keeping latest 2 kernels
sudo dnf remove $(dnf repoquery --installonly --latest-limit=-2 -q)
