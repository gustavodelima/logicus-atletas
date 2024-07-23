# Remove recursivamente (e forçadamente) o diretório data/db/ e todo o seu conteúdo
rm -fr data/db/

# Loop através de uma lista de diretórios de migração e remove todos os arquivos de migração que começam com "00"
for migration in {atletas,contratos,desempenho,eventos,fisiologia,treinamentos,nutricao,unidades}
do
    # Remove todos os arquivos de migração que começam com "00" no diretório específico
    rm $migration/migrations/00*.py
done
