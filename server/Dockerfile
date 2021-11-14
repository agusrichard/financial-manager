FROM python:3.8

LABEL agusrichard "agus.richard21@gmail.com"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/server

COPY . /app/server

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]