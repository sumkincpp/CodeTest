find . -maxdepth 1 -mindepth 1 -type d -exec touch {} \+

find . -exec touch {} \;
