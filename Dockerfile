FROM python:3.10.7-slim

WORKDIR /app

COPY . .

RUN pip3 install -r /app/requirements.txt

CMD ["python3", "weather_sqlite.py"] 