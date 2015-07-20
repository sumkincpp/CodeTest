#maximum compression 
7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on archive.7z piupiupiu/

#exclude by file list
# -r -- recursive
'-xr@\path\to\backup_daily_exclude.lst'

#exclude by directory pattern
-x?!ddd*

7za a test.7z /tmp/test -x\!test/1/*
