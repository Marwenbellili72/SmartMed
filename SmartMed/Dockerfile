FROM python:3.9

ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

RUN pip install --upgrade pip 
COPY ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt

COPY . $APP_HOME

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput --clear

EXPOSE 8000


