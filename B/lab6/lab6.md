# lab6

- 1. `&` 符号的作用是将命令放入后台执行 因此 后台进程或系统服务

- 2.yes消耗了CPU资源

- 3./init/init/bash/sleep 1000

- ```shell
  crontab -e
  * * * * * date +"\%T" >> $HOME/timestamps.txt
  ctrl + o
  enter
  ```

- 5.停止了计数

- 6.恢复了计数

- ```shell
  bg命令用于将一个在前台运行的作业放到后台运行
  ctrl +z 在Unix/Linux中 它用于将当前在前台运行的进程暂停并将其置于后台。这意味着该进程会被暂停（或“停止”），但并不会终止或退出。
  ```

- ```shell
  fg %x 
  把任务从后台带到前台 
  ctrl + x 终止任务
  kill %x 直接终止
  ```

- 

