# Keylogger en Python

Almacena las teclas pulsadas en un fichero y lo envía a un servidor FTP con TLS.

## Referencias

- [Módulo FTP](https://docs.python.org/3/library/ftplib.html)
- [Contenedor con VSFTPD](https://hub.docker.com/r/fauria/vsftpd)
- [Configuración de VSFTPD](https://www.geeksforgeeks.org/how-to-setup-and-configure-an-ftp-server-in-linux/)
- [Opciones en VSFTPD](http://vsftpd.beasts.org/vsftpd_conf.html)
- [Operaciones con ficheros en Python](https://www.programiz.com/python-programming/file-operation)

### Configuración de servidor FTP con el contenedor de referencia

#### Creación del contenedor
```bash
sudo docker run -d -p 20:20 -p 21:21 -p 21100-21110:21100-21110 -e FTP_USER=myuser -e FTP_PASS=mypass -e PASV_ADDRESS=127.0.0.1 -e PASV_MIN_PORT=21100 -e PASV_MAX_PORT=21110 --name vsftpd --restart=always fauria/vsftpd
```
#### Configuración de VSFTPD

**Fichero /etc/vsftpd/vsftpd.conf**
```TXT
anonymous_enable=YES
anon_upload_enable=YES
no_anon_password=YES
anon_other_write_enable=YES

# Configuración SSL

rsa_cert_file=/etc/ssl/private/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.pem
ssl_enable=YES
allow_anon_ssl=YES
force_local_data_ssl=YES
force_local_logins_ssl=YES
ssl_tlsv1=YES
ssl_sslv2=NO
ssl_sslv3=NO
require_ssl_reuse=NO
ssl_ciphers=HIGH
```

#### Generar certificado

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem
```

#### Garantizar permisos sobre /var/ftp/pub

```bash
chmod 757 -R /var/ftp/pub
```

