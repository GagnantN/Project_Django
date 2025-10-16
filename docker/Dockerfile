FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY docker/entrypoint /entrypoint

RUN chmod +x /entrypoint

ENTRYPOINT [ "/bin/bash", "/entrypoint" ]