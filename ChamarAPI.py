import requests

link = 'insira o link'
RequerirDados = requests.get(link)
Dicionario = RequerirDados.json #Salvar json

print(RequerirDados) #se vai retornar um erro ou não
print(RequerirDados.json) #converter parra json e mostrar dados
print(Dicionario['total_vendas']) #filtrar por "coluna"