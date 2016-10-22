# Mac OS X change shell
chsh -s /bin/zsh

# probably need to lish shell in /etc/shells
$ echo "/usr/local/bin/fish" | sudo tee -a /etc/shells
$ chsh -s /usr/local/bin/fish
Changing shell for fedor.
Password for fedor:


# Specifying Screenshots folder in Mac OS X
fedor@Fedors-MacBook-Pro:~$ defaults write com.apple.screencapture location ~/Pictures/Screenshots/
fedor@Fedors-MacBook-Pro:~$ killall SystemUIServer

# Keep awake, with screen on
caffeinate -u -t 36000
