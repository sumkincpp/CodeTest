# 
python -c'import time; print repr(time.time())'

# %3N not works for MAC OS X
date +%s%3N

# perl msec
perl -MTime::HiRes -e 'printf(\"%.0f\n\",Time::HiRes::time()*1000)'
