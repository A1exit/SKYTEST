FROM python:3.10

WORKDIR /sky_test

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY sky_test/entrypoint.sh .

COPY sky_test .

ENTRYPOINT ["sh", "entrypoint.sh"]
