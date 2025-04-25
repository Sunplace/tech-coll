# Openssl

## openssl get server certificate
https://stackoverflow.com/questions/7885785/using-openssl-to-get-the-certificate-from-a-server

with sni
```bash
openssl s_client -showcerts -servername www.example.com -connect www.example.com:443 </dev/null
```
without sni
```bash
openssl s_client -showcerts -connect www.example.com:443 </dev/null
```

## openssl generate self-signed SSL certificate
https://stackoverflow.com/questions/10175812/how-can-i-generate-a-self-signed-ssl-certificate-using-openssl

```bash
# Interactive
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

# Non-interactive and 10 years expiration
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"
```