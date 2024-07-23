# essa instrução faz a gente usar um container com python 3
FROM python:3

# esses "ENV" é para passar valores para algumas variáveis do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# é para onde dentro do container serão enviados nossos arquivos
WORKDIR /code

# copiar o arquivo de dependencias do python para dentro do container
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# pegar o código em geral e copiar para dentro do container em /code
COPY . /code/

