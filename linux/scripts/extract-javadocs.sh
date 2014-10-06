# Extracting (.*)-javadoc.jar files to $1 directories (heh, hi there!)
ls | sed -re "s/(.*)-javadoc.jar/\1/" | xargs -I % sh -c 'unzip %-javadoc.jar -d %'
