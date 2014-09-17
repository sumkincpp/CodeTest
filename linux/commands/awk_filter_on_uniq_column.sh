$ history | awk '!x[$2]++' | grep ls
    4  ls
  447  sbtls
  979  tail -f ls
  982  watch -d ls -l
  986  `ls -ltr | tail -f`
 1276  for m4b in $(ls -1 *.m4b); do ffmpeg -i $m4b -acodec libmp3lame -ar 22050 ${m4b}.mp3; done
 1285  "$(ls -l -1 *.m4b)"
