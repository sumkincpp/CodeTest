for m4b in *.m4b; do echo $m4b j; ffmpeg -i "$m4b" -acodec libmp3lame -ab 128k "${m4b}.mp3"; done
