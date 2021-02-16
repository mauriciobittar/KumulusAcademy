import requests

#Receber nome do usuário
usuario = input("Digite o usuário: ")

#Guardar o url em uma variável
url = "https://api.github.com/users/" + str(usuario) + "/repos"

#Baixar a pagina de repositórios e guardar em uma variável
r = requests.get(url)

#Listar o nome de cada repositório
print("Aqui estão os repositórios deste usuário:")
for i in r.json():
    if isinstance(i, dict):
        print(i["name"])
