
# Splitting by "." and displaying all fields in range from 1 to 9
cat p1.cpk.mngmt.snap | cut -d'.' -f1-9 | uniq

# yet another cut with delimeter, yau 
echo "fsdfsd: fsdfs: fsdfds" | cut -d: -f2-
 fsdfs: fsdfds
