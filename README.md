How to make a script run as a service

""
vi /etc/systemd/system/nfs-mount.service
""

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
