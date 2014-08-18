# Creating table of contents from current dir

ls | gawk 'BEGIN { print "<html>"} { print "<a href=\"./" $1 "\">"$1"</a><br>" } END {print "</html>"}' > directory_listing.html
