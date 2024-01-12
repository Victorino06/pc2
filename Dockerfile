
# Usa una imagen base de Python
FROM python:3.7.7-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos
COPY practica_creativa2/bookinfo/src/productpage/requirements.txt ./

# Instala las dependencias de Python
RUN pip3 install -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY practica_creativa2/bookinfo/src/productpage/ ./

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 9080

# Define la variable de entorno
ENV GRUPO_NUMERO 29

# Comando para ejecutar la aplicación
CMD ["python3", "./productpage_monolith.py", "9080"]
