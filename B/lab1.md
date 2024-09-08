# lab1



## Shell spelunkingShell spelunking

### 3.

```
pwd
```

### 4.

```shell
cat .secret
```

### 5.

```
ls | args cat
```

### 6.

```
rm -r nonsense/
```

### 7.

grep 'pattern' <filename> 

在file中匹配pattern

```
grep -E -B 2 "https?" <filename>
或者
grep -B 2 "https" <filename>

```

## 8.

```
chmod u+x a_script
```

`chmod u+x a_script` 是用来为文件添加权限的命令。我们可以逐一解释每个参数的含义：

- `chmod`：**Change Mode**，这个命令用来更改文件或目录的权限。
- `u`：代表 **user**，即文件的所有者。你可以使用以下字符来指定权限的范围：
  - `u`：文件所有者（user）
  - `g`：文件所属的组（group）
  - `o`：其他用户（others）
  - `a`：所有用户（包括文件所有者、组成员和其他用户）
- `+x`：表示**添加执行权限**（`x` 表示执行权限）。这里的 `+` 是操作符，表示要给指定范围（即 `u`，文件所有者）添加权限。其他常用操作符：
  - `+`：添加权限
  - `-`：移除权限
  - `=`：赋予指定权限，并移除其他未指定的权限
- `a_script`：这是要修改权限的**文件名**。在这个命令中，表示你想要为名为 `a_script` 的文件添加执行权限。

## 9.

```
echo "hello ,filament" > hello_world
cat hello_world
```

## General Questions 一般问题

###### 1.Linux/OSX is开源 and  Unix-like and Windows is 是专有系统

2.**命令行**：文本输入、精确控制、适合自动化和高级操作。

**图形界面**：视觉化操作、直观易用、适合日常任务和多媒体处理。

3.root 是没有根目录的目录

4.查看文件大小并按最后编辑日期排序，最旧的文件位于顶部

```
ls -lSrt

```

`-l`：以长格式显示文件信息，包括大小、权限、所有者等。

`-S`：按文件大小排序（默认是从大到小）。

`-r`：反转排序顺序，这样最旧的文件会排在顶部。

`-t`：按修改时间排序。

5.输出前x行

```

awk 'NR<=x' <filename>
NR:number of record 

head -n x <filename> 

sed -n '1,x p' <filename>
```

###### 6.cat  <file1> >  <file2>会覆盖文  cat <file1> >> <file2>会追加文本

echo , cat is the same at this function

### Culture Questions 文化问题

1.宽松许可证提供更多自由，而版权共享许可证确保软件及其派生版本也保持开源。

2.MIT licence

3.Linux  and WSL
