# Comando comentado para limpar o banco de dados (remover todos os dados)
# sudo docker compose run web python manage.py flush

# Cria novas migrações baseadas nas alterações nos modelos
sudo docker compose run web python manage.py makemigrations

# Aplica as migrações ao banco de dados
sudo docker compose run web python manage.py migrate
