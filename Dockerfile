FROM python:3.10

WORKDIR /sky_test

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY sky_test .

CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn sky_test.wsgi -b :8000 --reload
