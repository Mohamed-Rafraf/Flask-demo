FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install psycopg2-binary

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]



