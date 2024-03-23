# 了解 Python 中的 os 模块

在 Python 中，`os` 模块是一个非常重要的标准库，它提供了许多与操作系统交互的功能。通过 `os` 模块，我们可以执行诸如文件操作、目录操作、进程管理等任务。让我们深入了解一下 `os` 模块的一些常见用法。

**以下代码省略 `import os` 。**

### 文件和目录操作

**1、获取当前工作目录：**

```python
cwd = os.getcwd()
print("当前工作目录:",cwd)
```

**2、创建目录：**

```python
os.mkdir("新目录")
```

**3、列出目录内容：**

```python
files = os.listdir(".")
for file in files:
    print(file)
```

**4、删除文件或目录：**

```python
os.remove("文件名")
os.rmdir("目录名")
```

### 进程管理

**1、执行系统命令：**

```python
os.system("ls -l") # 在 Unix/Linux 系统中列出当前目录的文件信息
```

**2、获取环境变量：**

```python
path = os.getenv("PATH")
print("PATH 环境变量:", path)
```

### 其他常用功能

**1、路径操作：**

```python
filepath = "/path/to/file.txt"
basename = os.path.basename(filepath) # 获取文件名
os.path.dirname(filepath) # 获取目录路径
```

**2、判断路径是否存在：**

```python
exists = os.path.exists("/path/to/something")
isdir = os.path.isdir("/path/to/directory")
# 返回布尔值(True & False)
```

**3、文件权限操作：**

```python
os.chmod("filename", 0o755)  # 修改文件权限为 rwxr-xr-x
```

通过 `os` 模块，Python 提供了丰富的操作系统级别的功能，让我们可以轻松地 **与操作系统交互** ，执行各种操作。无论是 **文件操作** 、**目录操作**还是 **进程管理** ，`os` 模块都能帮助我们高效地完成任务。

总的来说，`os` 模块是 Python 编程中不可或缺的一部分，熟练掌握其用法将有助于提升编程效率和灵活性。

希望本文对你理解 Python 中的 `os` 模块有所帮助！
