

## APT

```bash
$ apt-file search --regexp 'bin/ip$'
iproute2: /bin/ip
iproute2: /sbin/ip
```


```
$ dpkg-query -S '*/dig'
bind9-dnsutils: /usr/bin/dig
```


## dpkg-query - find biggest packages

```
$ dpkg-query -W -f='${Installed-Size;8} ${Package}\n' | sort -nr | head -10
  366872 chromium-browser
  115060 raspberrypi-kernel
   72581 libllvm11
   61021 firmware-atheros
   57880 libwebkit2gtk-4.0-37
   51754 firmware-misc-nonfree
   44675 pypy
   41337 vlc-l10n
   40103 gcc-10
   38079 firmware-libertas
```
