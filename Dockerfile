FROM alphine:latest
RUN apk update && apk add bash

WORKDIR /app
COPY repeat.sh /app

FROM python::3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["python", "app.py"]

