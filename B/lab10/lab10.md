# lab10

## Ques:

- 1.`root`

- 2.是同一个容器 检查容器的配置文件

- ```dockerfile
  # Specify Fedora Linux as base image
  FROM fedora:latest
  
  # Install Python with yum (Fedora's Package Manager)
  # Install required Python packages
  RUN yum update -y && yum install -y python3 python3-pip && \
      python3 -m pip install pyfiglet termcolor
   
  # Add the missile.py file to the final image
  ADD missile.py /
  
  # Specify the command to be run on container creation
  CMD ["/usr/bin/python3", "missile.py"]
  ```

- 好的接下来你会遇到连不上`Dockerhub`的问题 接下来你需要换源清华的,本篇用的ubuntu 以下是教程

  - ```shell
    #可能会遇到像我这样的问题
     => ERROR [internal] load metadata for docker.io/library/fedora:latest                                                30.0s
    ------
     > [internal] load metadata for docker.io/library/fedora:latest:
    ```

  - ```shell
    #添加源
    sudo nano /etc/apt/sources.list
    
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    
    
    
    #安装Docker
    sudo apt update
    sudo apt install docker.io
    
    #然后在etc文件夹下创建docker文件夹
    #接着修改daemon.json文件
    sudo nano /etc/docker/daemon.json
    
    {
      "dns": ["8.8.8.8", "8.8.4.4"],
      "registry-mirrors": ["https://mirrors.tuna.tsinghua.edu.cn/dockerhub"]
    }
    #保存退出 然后重启docker
    sudo systemctl restart docker #如果失败了手动重启
    
    #然后就是激动人心的时刻了
    docker pull fedora:latest
    docker build -t missile:latest .
    #成功!!!!
    USERNAME@MACHINENAME:~/SysadminDecal/decal-labs/b10$ docker build -t missile:latest .
    [+] Building 79.7s (8/8) FINISHED                                                                            docker:default
     => [internal] load build definition from Dockerfile                                                                   0.0s
     => => transferring dockerfile: 460B                                                                                   0.0s
     => [internal] load metadata for docker.io/library/fedora:latest                                                       0.0s
     => [internal] load .dockerignore                                                                                      0.1s
     => => transferring context: 2B                                                                                        0.0s
     => [1/3] FROM docker.io/library/fedora:latest                                                                         0.0s
     => [internal] load build context                                                                                      0.1s
     => => transferring context: 221B                                                                                      0.0s
     => [2/3] RUN yum update -y && yum install -y python3 python3-pip &&     python3 -m pip install pyfiglet termcolor    76.8s
     => [3/3] ADD missile.py /                                                                                             0.1s
     => exporting to image                                                                                                 2.6s
     => => exporting layers                                                                                                2.5s
     => => writing image sha256:3cdcb7273599f374e99fdd172853132e6169923f5226da79346e8ccef14c30dc                           0.0s
     => => naming to docker.io/library/missile:latest 
    ```

- 1.观察到了`MISSILE`巨大字母

- ```dockerfile
  # 使用 Ubuntu Bionic 作为基础镜像
  FROM ubuntu:bionic
  
  # 更新包列表并安装 fortune 和 fortunes-min
  RUN apt-get update && apt-get install -y fortune fortunes-min && \
      rm -rf /var/lib/apt/lists/*
  
  # 指定容器启动时执行的命令
  CMD ["/usr/games/fortune"]
  
  ```

- ```cpp
  REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
  my-fortune-app      latest    4ad0ed473d89   55 seconds ago   66MB
  missile             latest    3cdcb7273599   3 hours ago      471MB
  ubuntu              latest    59ab366372d5   2 weeks ago      78.1MB
  fedora              latest    eca85b75dc19   6 weeks ago      222MB
  ubuntu              bionic    f9a80a55f492   17 months ago    63.2MB
  hello-world         latest    d2c94e258dcb   18 months ago    13.3kB
  linxi177229/csapp   latest    49617830ad4c   2 years ago      1.04GB
  ```

- 

## `docker build`的参数:

| 参数          | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| `-t, --tag`   | 指定生成的镜像的名称和标签，例如 `-t my-image:latest`。      |
| `-f, --file`  | 指定 Dockerfile 的路径，默认查找当前目录中的 `Dockerfile`。  |
| `--build-arg` | 向 Dockerfile 中的构建参数传递变量，例如 `--build-arg VERSION=1.0`。 |
| `--no-cache`  | 禁用缓存，强制重新构建所有层，例如 `--no-cache -t my-image`。 |
| `--pull`      | 在构建前尝试拉取最新的基础镜像。                             |
| `--rm`        | 默认删除中间容器，使用 `--rm=false` 可保留中间容器。         |
| `-q, --quiet` | 只输出镜像 ID，不显示构建过程的详细输出。                    |
| `--target`    | 指定构建的目标阶段，适用于多阶段构建的 Dockerfile。          |
## `docker run`的参数

| 参数             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| `-d, --detach`   | 在后台运行容器（分离模式），返回容器 ID。                    |
| `--name`         | 指定容器的名称。                                             |
| `-p, --publish`  | 将主机的端口映射到容器的端口，格式为 ` docker run <主机端口>:<容器端口>`。 |
| `-e, --env`      | 设置环境变量，格式为 `-e VAR_NAME=value`。                   |
| `-v, --volume`   | 将主机的目录或文件挂载到容器中，格式为 `主机路径:容器路径`。 |
| `--rm`           | 容器停止后自动删除容器。                                     |
| `-it`            | 以交互模式运行容器，分配伪终端，适用于需要用户输入的应用。   |
| `--network`      | 指定容器连接的网络。                                         |
| `--restart`      | 设置容器的重启策略，如 `--restart unless-stopped`。          |
| `--privileged`   | 给予容器额外的权限，通常用于需要访问主机硬件的应用。         |
| `-w, --workdir`  | 设置容器内的工作目录。                                       |
| `--entrypoint`   | 覆盖容器的默认入口点。                                       |
| `--user`         | 指定运行容器时的用户，格式为 `USER` 或 `USER:GROUP`。        |
| `-h, --hostname` | 设置容器的主机名。                                           |

## Question:

- ```shell
  phrink@7945hx:~/SysadminDecal/decal-labs/b10/my-fortune-app$ docker ps
  CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS         PORTS                  NAMES
  9894b036b2c3   httpd     "httpd-foreground"   2 minutes ago   Up 2 minutes   0.0.0.0:4002->80/tcp   xenodochial_heyrovsky
  373c77057ca7   httpd     "httpd-foreground"   2 minutes ago   Up 2 minutes   0.0.0.0:4001->80/tcp   silly_moser
  023af7979467   httpd     "httpd-foreground"   2 minutes ago   Up 2 minutes   0.0.0.0:4000->80/tcp   intelligent_babbage
  ```

- ```shell
  DockerID的NAMES都是随机命名 取两个单词 word1_word2
  ```

- ```shell
  #停止某一个容器
  docker stop name1
  #除了stop后面跟名字 还可以跟上ID前几位 例如
  ID  				NAMES
  9894b036b2c3		xenodochial_heyrovsky
  023af7979467 		intelligent_babbage
  
  docker stop 989 #和以下等同
  docker stop xenodochial_heyrovsky
  ```

- 以下是quotes.pp文件

- 

  ```shell
  
  package { 'curl':
    ensure => 'installed',     # What package is required for this script to run?
  }
  
  group { 'quotegather':
    ensure => 'present',       # Do we want the group on this system?
  }
  
  user { 'quotes':
    ensure => 'present',       # Do we want the user on this system?
    gid    => 'quotegather',  # Note that we can pass a group name to gid
    home   => '/tmp',
    shell  => '/bin/false',
    require => Group['quotegather'],  # Do not create the user quotes unless the quotegather group exists
  }
  
  cron { 'getquote':
    user    => 'quotes',      # Which user do we want to run this cron job?
    command => "curl 'https://api.kanye.rest/?format=text' >> quotes && echo >> quotes",  # This pulls quotes from an API and append>  minute  => '*/2',         # Hint: passing * means this runs every minute
  }
  ```

- 

  ```shell
  #10分分钟后提取的内容
  cat /tmp/quotes
  
  "Believe in your flyness...conquer your shyness."
  相信你的魅力……战胜你的害羞。
  
  "Ma$e is one of my favorite rappers and I based a lot of my flows off of him."
  Ma$e 是我最喜欢的说唱歌手之一，我的很多风格都是以他为基础的。
  
  "The world is our family."
  世界是我们的大家庭。
  
  "Trust me ... I won't stop."
  相信我……我不会停止。
  
  "I am Warhol. I am the No. 1 most impactful artist of our generation. I am Shakespeare in the flesh."
  我是沃霍尔。我是我们这一代最具影响力的艺术家。我是活生生的莎士比亚。
  
  "I honestly need all my Royeres to be museum quality... if I see a fake Royere Ima have to Rick James your couch."
  我真心希望我所有的 Royere 都是博物馆级别的……如果我看到假货，我就要像瑞克·詹姆斯那样对待你的沙发。
  ```

- 

