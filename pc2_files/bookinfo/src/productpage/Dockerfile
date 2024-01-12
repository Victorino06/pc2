FROM python:3.7.7-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

ENV GRUPO_NUMERO=29
EXPOSE 9080

CMD ["python","productpage_monolith.py", "9080"]
