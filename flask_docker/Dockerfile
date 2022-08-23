#Pasos para que la aplicacion funcione

#primer paso instalar la imagen correspondiente
FROM alpine:3.10

#luego instalar python junto con pip
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip 

#luego crearemos una carpeta
WORKDIR /app

#copiar todos nuestros archivos a /app
COPY . /app

#luego instalar las dependencias
RUN pip3 --no-cache-dir install -r requirements.txt

#comando que se ejecutara en el cmd 
CMD ["python3", "app.py"]