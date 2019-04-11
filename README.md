# zhuabao

使用Python的scapy进行抓包并筛选出dns数据包








# Python 学习资源库

## 设置清华大学PIP镜像源
升级 pip 到最新的版本 (>=10.0.0) 后进行配置  
以管理员身份运行 VSCode， 并在VSCode 终端里运行  
```
pip 官方源：https://pypi.python.org/simple/
pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Windows 环境下

1. 以管理员身份启动 VSCode  
1. VSCode 的终端下运行 Set-ExecutionPolicy RemoteSigned
1. 关闭 VSCode，以普通用户身份再次运行 VSCode
1. 在VSCode里打开目标文件夹，终端里运行 python -m venv .venv
1. 终端里运行 .venv\Scripts\Activate.ps1 进入虚拟环境
1. 在虚拟环境里安装工具包: black, mypy
1. VSCode的用户配置文件里加入以下设置：  
    ````
    "python.venvFolders": [".venv"],  
    "python.linting.mypyEnabled": true,  
    "python.linting.pylintEnabled": false,  
    "python.formatting.provider": "black",  
    "python.jediEnabled": false,
    ````

## .gitignore 文件
一般包含以下内容
```
.venv  
.vscode  
\_\_pycache__  
.mypy_cache
.pytest_cache
```
