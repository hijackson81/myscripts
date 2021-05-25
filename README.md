# How to make a script run as a service

```
vi /etc/systemd/system/nfs-mount.service
```

```
[Unit]
Description=My custom startup script
# After=network.target
# After=systemd-user-sessions.service
# After=network-online.target
[Service]
# User=spark
# Type=simple
# PIDFile=/run/my-service.pid
ExecStart=/home/tpcloud/mountnfs.sh start
# ExecReload=/home/transang/startup.sh reload
# ExecStop=/home/transang/startup.sh stop
# TimeoutSec=30
# Restart=on-failure
# RestartSec=30
# StartLimitInterval=350
# StartLimitBurst=10
[Install]
WantedBy=multi-user.target
```


```
# Create private key for CA
openssl genrsa -out ca.key 2048

# Comment line starting with RANDFILE in /etc/ssl/openssl.cnf definition to avoid permission issues
sudo sed -i '0,/RANDFILE/{s/RANDFILE/\#&/}' /etc/ssl/openssl.cnf

# Create CSR using the private key
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr

# Self sign the csr using its own private key
openssl x509 -req -in ca.csr -signkey ca.key -CAcreateserial  -out ca.crt -days 1000
```
