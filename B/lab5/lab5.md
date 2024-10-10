# Lab 5

## Questions

- **Question 1:** HTTP uses TCP  
  Discord uses TCP for text and UDP for voice.  
  Skype is the same.

- **Question 2:** MAC Address  
  `52:54:00:d7:ce:cc`  
  `52:54:00` is Realtek.

- **Question 3:** Host Count Calculation

  - $$
    \text{主机数量} = 2^{\text{主机位}} - 2
    $$

  - 本文的问题: `127.0.0.0/8`, the host bits are 24:  
    $$
    \text{主机数量} = 2^{32-8} - 2 = 2^{24} - 2
    $$
    
    
  - `127.0.0.0/8` 表示一个网络，其中 `/8` 指定了网络部分的位数，后24位是主机位。  
    主机数量 = \(2^{Host bits} - 2\)  
    减去广播地址和网络地址。

  - **广播地址和网络地址分别是多少呢?**  
    举例：`124.4.4.78/3`  
    
    网络位为3，主机位是29。  
    
    124.4.4.78` 转换成二进制：  
    `01111100.00000100.00000100.01001110`  
    
    保留网络位即前三位 `011`，然后计算地址：  
    
    网络地址: 主机位全是0  
    `01100000.00000000.00000000.00000000`  转换成十进制: `96.0.0.0`  
    
    广播地址: 主机位全是1  
    `01111111.11111111.11111111.11111111`  
    转换成十进制: `127.255.255.255`

- **Question 4:** DNS Lookup

  ```bash
  nslookup facebook.com
  Server:         10.255.255.254
  Address:        10.255.255.254#53
  
  Non-authoritative answer:
  Name:   facebook.com
  Address: 128.242.250.155
  Name:   facebook.com
  Address: 2a03:2880:f112:83:face:b00c:0:25de
  ```

## Coding

### 1.

**ehh0:host:172.17.27.213**
**127.0.0.1**

```sh
#!/bin/bash

# 检查是否提供了主机名或IP地址
if [ -z "$1" ]; then
    echo "用法: $0 <host>"
    exit 1
fi

ping -c 1 "$1" &> /dev/null

if [ $? -eq 0 ]; then
    echo "$1 是在线的。"
else
    echo "$1 不在线。"
fi

```

### 2.

```sh
ip link show eth0:
#得到以下
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:15:5d:b4:45:c4 brd ff:ff:ff:ff:ff:ff
只需要提取其中的link/ether 因为他是MAC地址 而brd是brodcast广播地址


```

```shell
#!/bin/bash

#使用以下来修正unix的换行问题
#sed -i 's/\r$//' mac.sh
#或者在安装了dos2unix之后 使用 dos2unix <filename>

mac_address=$(ip link show eth0 | awk '/link\/ether/ {print $2}')

if [ -n "$mac_address" ] ; then
	echo "MAC_ADDRESS IS $mac_address"
else
	echo "FAIL TO ACCESS MAC_ADDRESS"
fi
```



