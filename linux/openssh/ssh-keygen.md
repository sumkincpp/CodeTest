
    ssh-keygen -b 4096 -t rsa -C a@a

Generating putty keys :

    puttygen id_rsa -O private -o aaaa -P
    puttygen id_rsa -O public -o bbb -P

Checking:

    openssl asn1parse -in id_rsa
