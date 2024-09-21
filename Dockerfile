FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./input_text.py /app

CMD ["python", "input_text.py"]