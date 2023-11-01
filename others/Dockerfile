# 使用官方的 Python 基础镜像
FROM python:3.8

# 设置工作目录为 /app
WORKDIR /app

# 拷贝当前目录下的所有文件到Docker镜像的/app目录下
ADD . /app

# 使用 pip 安装依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 指定容器启动时运行的命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]