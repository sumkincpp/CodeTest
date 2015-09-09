# sqlite3 places.sqlite "SELECT moz_places.url FROM moz_places;" | awk -F'/' ' { print $1"//"$3; }' | uniq -c | sort -n
....
   1190 https://mail.yandex.ru
   1288 https://github.com
   1412 https://mail.google.com
   5004 http://www.google.com
   5121 https://www.google.com
