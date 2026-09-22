FROM python:3.12-slim

WORKDIR /app

COPY app.py .

COPY input ./input

RUN mkdir -p /app/output

VOLUME ["/app/output"]

CMD ["python", "app.py"]