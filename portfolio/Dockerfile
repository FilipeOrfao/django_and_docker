FROM python:3.12.6-alpine3.20
# prevent Python form writing .pyc files
ENV PYTHONDONTWHITEBYTECODE 1
# ensure Python output is sent directly ot the terminal without buffering
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]