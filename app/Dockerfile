FROM python:3.11.7

# Definir directorio de trabajo 
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Puerto a exponer para la api 
EXPOSE 8050

# Comandos a ejecutar al correr el contenedor 
CMD ["python", "app.py"]
