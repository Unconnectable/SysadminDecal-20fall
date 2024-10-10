# lab4

```shell
sudo apt install gcc
gcc --version
#验证版本

```

```c
#include <stdio.h>
int main()
{
    printf("Hello Penguin!");
    return 0;
}
```

```shell
gcc hellopenguin.c -o hellopenguin
#编译
sudo apt install ruby ruby-dev rubygems build-essential

gem install fpm --user
#Gem 是用于管理 Ruby 包的工具。
#fpm 是一个用于创建 Linux 软件包的 Ruby Gem。

export PATH=~/.gem/ruby/2.5.0/bin:$PATH

mkdir packpenguin
cd packpenguin
mkdir -p usr/bin
mv hellopenguin packpenguin/usr/bin/
fpm -s dir -t deb -n hellopenguin -v 1.0~ocf1 -C packpenguin

sudo apt install ./hellopenguin_<version+arch>.deb
#版本是1.0~ocf1  上面的命令有
#arch 可以直接在cmd中查看  
#$arch  我电脑是x86_64  
#但是.deb 文件通常使用 amd64 来表示 64 位架构
sudo apt install ./hellopenguin_1.0~ocf1_amd64.deb

hellopenguin
```

