FROM python:3.8

RUN apt -y update; apt -y install uwsgi

COPY django_project/ /home/web/django_project

WORKDIR /home/web/django_project
RUN pip install -r requirements.txt

ADD deployment/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
