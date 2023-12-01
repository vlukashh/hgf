FROM python:latest
COPY . /app
WORKDIR /app
RUN pip3 install django pillow django-bootstrap4
CMD python manage.py runserver 0.0.0.0:8080