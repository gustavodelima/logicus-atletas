# Coloque aqui o nome da aplicação/módulo que deseja criar
aplicacao=""

# Executa o comando para criar uma nova aplicação Django usando Docker Compose
sudo docker compose run web python manage.py startapp $aplicacao
