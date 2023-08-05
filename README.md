# 电子书 tiny_python_projects 的练习代码

### 测试代码
```bash
pytest -xv test.py
```

### 关于打包二进制

```bash
# 安装依赖
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

# 打包
pyinstaller -F src/run.py

# The +x will add an “executable” attribute to the file.
chmod +x ./dist/run
# 或者修改权限
chmod 777 ./dist/run

```

### 关于依赖

```bash
# 获取环境中所有安装的包
pip freeze > ./requirements.txt

# 根据某一个项目的 import 语句来生成依赖
pip install pipreqs
pipreqs ./ --force

# 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```