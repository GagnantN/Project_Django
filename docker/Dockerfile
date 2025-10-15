FROM python:3

RUN pip install django mysqlclient

COPY entrypoint /entrypoint

RUN chmod +x /entrypoint

ENTRYPOINT [ "/bin/bash", "/entrypoint" ]