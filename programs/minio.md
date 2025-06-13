# minio 

mcc = minio client (mc)

```bash
$ mcc alias set myminio http://1.1.1.1:9000 admin super-strong-password
$ mcc mb myminio/my-bucket
$ mcc anonymous set download myminio/my-bucket
$ mcc admin user svcacct add myminio admin
Access Key: XXXXXXXXXXXXX
Secret Key: XXXXXXXXXXXXX
Expiration: no-expiry

```
