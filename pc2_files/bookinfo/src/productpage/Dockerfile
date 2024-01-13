FROM python:3.7.7-slim

WORKDIR /productpage

COPY . /productpage

RUN pip install -r requirements.txt

ENV GRUPO_NUMERO=29

EXPOSE 9080

CMD ["python","productpage.py", "9080"]
