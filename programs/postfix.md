# Postfix

After changing the password

```bash
sudo postmap /etc/postfix/sasl_passwd
```

Logs

```
sudo journalctl --since today | grep -E 'postfix/(pickup|cleanup|qmgr|smtp|smtpd|local)'
```
