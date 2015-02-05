# self-signed certificate (verse.key) and private key (verse.pem)
# sha256 as `sha1` is unsecure
sudo openssl req -config openssl.cnf -x509 -sha256 -nodes -days 3650 -newkey rsa:4096 -keyout verse.key -out verse.crt
cat verse.crt verse.key | sudo tee verse.pem

# One line subject
openssl req -subj ‘/CN=domain.com/O=My Company Name LTD./C=US’ -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt

# get openssl digests
openssl dgst --help

# verifying cert fields (in pem format)
openssl x509 -noout -text -in verse.crt 

# sha hashes
> echo -n "abc" | openssl sha1 -binary | base64
qZk+NkcGgWq6PiVxeFDCbJzQ2J0=

> echo -n "abc" | openssl sha1
(stdin)= a9993e364706816aba3e25717850c26c9cd0d89d

> echo -n "abc" | openssl sha1 -sha256
(stdin)= ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
