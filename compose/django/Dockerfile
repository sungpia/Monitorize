FROM python:3

ENV PYTHONUNBUFFERED 0

ADD    wait-for-it.sh /
CMD ["chmod", "+x", "/wait-for-it.sh"]

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app

ADD    .    /app/
RUN    pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
