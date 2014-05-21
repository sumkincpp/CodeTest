
# Splitting by "." and displaying all fields in range from 1 to 9
cat p1.cpk.mngmt.snap | cut -d'.' -f1-9 | uniq
