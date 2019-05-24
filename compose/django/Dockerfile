FROM python:3

ENV PYTHONUNBUFFERED 0

ADD    wait-for-it.sh /
CMD ["chmod", "+x", "/wait-for-it.sh"]

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app

ADD    requirements.txt    /app/
RUN    pip install --trusted-host pypi.python.org -r requirements.txt

ADD    ./monitorize    /app/monitorize
ADD    ./manage.py     /app/

CMD ["python", "manage.py", "runserver", "0:8000"]
