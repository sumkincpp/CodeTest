# Total java processes usage in bytes
ps -C java -O rss | awk '{total += $2} END {print total}'
