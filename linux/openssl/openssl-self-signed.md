# SHA256 signed, 4096 bit RSA

### Creating private key, in PEM-format, maybe private.pem
openssl genrsa -out key.key 4096
### Creating certificate signing request
openssl req -out csr-2017-03-15.csr -key key.key -new -sha256
### Self-signing csr with key
openssl x509 -req -sha256 -days 3650 -in csr.csr -signkey key.key
 
### View details of a private Key
openssl rsa -in private.pem -text -noout

### View details of a CSR
openssl req -in csr.pem -text -noout

### View details of a Certificate
openssl x509 -in certificate.pem -text -noout

# Links

  * [openssl.md](https://gist.github.com/NoMan2000/06fffaca2ea710175cbcdd1a933c44af)
