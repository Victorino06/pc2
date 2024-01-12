FROM python:3.7.7-slim

WORKDIR /productpage

COPY practica_creativa2/bookinfo/src/productpage/requirements.txt ./

RUN pip3 install -r requirements.txt

COPY practica_creativa2/bookinfo/src/productpage/ ./

EXPOSE 9080

CMD ["python", "./productpage.py", "9080"]
