FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install psutil
RUN pip install roundrobin
RUN pip install requests
ENV NAME Kurt and Roman
CMD ["python", "app.py"]
