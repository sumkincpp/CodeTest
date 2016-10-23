net user %username% 
net users
net session
net accounts /domain

net group "domain user" /domain
net localgroup users /domain

rem started services
net start

net share

net view
net view /domain
