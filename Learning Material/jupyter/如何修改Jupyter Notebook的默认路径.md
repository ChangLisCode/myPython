1. 运行Terminal，
2. 查看Jupyter使用的配置文件在哪个目录：
```jupyter --config-dir```
3. 切换到该目录，检查是否存在配置文件：
```jupyter_notebook_config.py```
4. 如果不存在，使用以下命令创建一个：
```jupyter notebook --generate-config```
5. 在配置文件jupyter_notebook_config.py中，添加以下配置内容(自行设定默认路径）：
```## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'd:\\learning'
```

现在`d:\learning`为新的Jupyter目录，可以替换成你自己的目录。

7. 重新运行
`Jupyter notebook`
