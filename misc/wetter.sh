#!/usr/bin/env bash

# curl https://www.ard-text.de/mobil/171 | grep -zPo "<p>(.|\n)*</p>" > wetter-`date +%F-%H-%M`.txt
# cat page.html | grep -zPo "<div class='std'>(.|\n)*?</div>" | xmllint --xpath '//p/text()' - | xargs echo | sed 's/\. /\.\n/g'

curl -sS https://www.ard-text.de/mobil/171 | \
    grep -zPo "<div class='std'>(.|\n)*?</div>" | \
    xmllint --xpath '//text()' - | \
    xargs echo | \
    sed 's/\. /\.\n/g' | \
    tee wetter-`date +%F-%H-%M`.txt
