# lab8

## Symmetric Cryptography 对称加密

- 随机创建一个文件 FILE_1.txt

- ```shell
  echo "THIS IS FILE_1" > FILE_1.txt
  ```

- ```shell
  gpg --symmetric FILE_1.txt
  ```

- ```shell
  gpt --decrypt FILE_1.txt.gpg
  ```

## Lab Checkoff 实验验收

- ```shell
  ocfdeacl
  $ gpg --decrypt file1.txt.gpg
  gpg: AES.CFB encrypted data
  gpg: encrypted with 1 passphrase
  Quack
  ```

- ```shell
  #导入文件
  gpg --import <key_name>
  ```

- ```shell
  #公钥
  gpg --export -a "USR" > publickey.asc
  #私钥
  gpg --export-secret-keys -a "USR" > privatekey.asc
  
  ```

- ```sh
  gpg --list-keys
  ```

- ```sh
  #导入
  gpg --import lab8privkey
  gpg: key 82DDDAA6869E6CEC: public key "lab8privkey" imported
  gpg: key 82DDDAA6869E6CEC: secret key imported
  gpg: Total number processed: 1
  gpg:               imported: 1
  gpg:       secret keys read: 1
  gpg:   secret keys imported: 1
  
  #解密
  gpg --decrypt file2.txt.gpg
  gpg: Note: secret key 83ADADD521C1D38D expired at Sat Oct 31 03:00:59 2020 CST
  gpg: encrypted with 2048-bit RSA key, ID 83ADADD521C1D38D, created 2018-10-31
        "lab8privkey"
  Woof
  ```



## Hashing (Checksums)

- ```sh
  $md5sum file3.txt
  24802658092989e4861d5d73b8634f6f  file3.txt
  ```

- ```sh
  $ sha1sum file3.txt
  c8623620076795ed96d3791fbbcc5208586d975d  file3.txt
  ```

## File Security

- ```sh
  -rw-r--r--  file4.txt
  #普通文件 
  #USR:rw- 读写
  #Group:r-- 只能读
  #Other:r-- 只能读
  
  ```

- ```sh
  #更改前
  -rw-r--r--  1 phrink phrink 8640 Oct 16 20:31 file5
  #更改后
  -rwxr-xr-x  1 phrink phrink 8640 Oct 16 20:31 file5
  ./file5
  aching flair
  ```

- ```sh
  3.
  sudo chown phrink file6.txt
  ```

- ```sh
  4.
  sudo chmod 400 file7.txt
  ```

- ```sh
  5.
  #原本
  -r--------  1 nobody phrink	file7.txt
  sudo chown root:root file7.txt
  sudo chmod 400 file7.txt
  #之后
  -r--------  1 root   root 	file7.txt
  ```

- ```sh
  sudo chown 040 file9.txt
  ```

- 

- 

- 