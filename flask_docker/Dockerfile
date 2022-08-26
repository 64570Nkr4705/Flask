#Pasos para que la aplicacion funcione

#primer paso instalar la imagen correspondiente
FROM alpine:3.10

#El comando RUN ejecutara un comando en la terminal de alpine
#en este caso instalara python y pip
#con el administrador de paquetes de alpine
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip 

#Con este comando crearemos una carpeta llamada app
WORKDIR /app

#Con este comando copiaremos todos nuestros archivos a /app
COPY . /app

#con pip freeze > requirements.txt genraremos un archivo .txt con todos 
#los requerimientos que necesita nuestra app para funcionar 
#luego ejecutaremos este comando para instalar estos requerimientos
RUN pip3 --no-cache-dir install -r requirements.txt

#comando que se ejecutara en el cmd 
CMD ["python3", "app.py"]