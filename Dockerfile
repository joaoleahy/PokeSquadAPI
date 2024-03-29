FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=pokemon_project.settings

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

RUN python manage.py test

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
