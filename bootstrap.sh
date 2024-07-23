# Executa o script shell database-clean.sh que limpa e reseta o banco de dados
bash database-clean.sh

# Constrói (ou reconstrói) os serviços definidos no arquivo docker-compose.yml
docker compose build

# Executa o script shell migrate.sh que aplica as migrações do banco de dados
bash migrate.sh

# Executa o comando para criar um superusuário no Django usando Docker Compose
sudo docker compose run web python manage.py createsuperuser

# Executa o script shell start.sh que inicia a aplicação ou serviços necessários
bash start.sh
