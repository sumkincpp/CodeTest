# 
python -c'import time; print repr(time.time())'

# %3N not works for MAC OS X
date +%s%3N

# perl msec
perl -MTime::HiRes -e 'printf(\"%.0f\n\",Time::HiRes::time()*1000)'

#convert timestamp
date -d @1223333333

date -d @1278999698 +'%Y-%m-%d %H:%M:%S'

TZ=America/New_York date
Mon Aug 31 03:30:54 EDT 2015

TZ=Europe/Moscow date
Mon Aug 31 10:31:03 MSK 2015
