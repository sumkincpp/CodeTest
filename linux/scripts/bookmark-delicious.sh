#!/bin/sh
# newsbeuter bookmarking plugin for del.icio.us
# (c) 2007 Andreas Krennmair
# documentation: http://delicious.com/help/api#posts_add

username="your delicious.com username here"
password="your delicious.com password here"

url="$1"
title="$2"
desc="$3"

delicious_url="https://api.del.icio.us/v1/posts/add?url=${url}&description=${title}&extended=${desc}"

output=`wget --http-user=$username --http-passwd=$password -O - "$delicious_url" 2> /dev/null`

output=`echo $output | sed 's/^.*code="\([^"]*\)".*$/\1/'`

if [ "$output" != "done" ] ; then
  echo "$output"
fi

# https://raw.githubusercontent.com/aleprovencio/dotfiles/0878ed7d641481d21fd28c64e4c6a0d99dc4433c/.newsbeuter/scripts/bookmark-delicious.sh
