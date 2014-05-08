# Mac OS X change shell
chsh -s /bin/zsh

# probably need to lish shell in /etc/shells
$ echo "/usr/local/bin/fish" | sudo tee -a /etc/shells
$ chsh -s /usr/local/bin/fish
Changing shell for fedor.
Password for fedor:
