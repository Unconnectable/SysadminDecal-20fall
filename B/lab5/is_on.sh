#!/bin/bash

# 检查是否提供了主机名或IP地址
if [ -z "$1" ]; then
    echo "用法: $0 <host>"
    exit 1
fi

# 使用 ping 命令检查主机是否在线
ping -c 1 "$1" &> /dev/null

# 检查 ping 命令的退出状态
if [ $? -eq 0 ]; then
    echo "$1 是在线的。"
else
    echo "$1 不在线。"
fi
