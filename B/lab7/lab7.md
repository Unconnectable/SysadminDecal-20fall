# lab7

## What services are running right now?

 - ```shell
   systemxtl --type=service
   ```

## Exercise

 - ```shell
   reload 是加载他的configuration，不一定会重启
   restart 是 重启
   ```

 - ```shell
   .service 文件中的 ExecReload 字段决定的
   ```

 - 以下是service文件

 - ```service
   [Unit]
   Description=my Toy Service
   After=network.target
   
   [Service]
   ExecStart=/home/phrink/SysadminDecal/decal-tabs/b7/venv/bin/python /home/phrink/SysadminDecal/decal-tabs/b7/app.py
   User=phrink
   Restart=always
   RestartSec=10
   
   [Install]
   WantedBy=multi-user.target
   
   ```

	- 