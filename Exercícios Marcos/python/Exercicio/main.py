# Marcos Pratis Medice 15/02/2020

from repository_model import RepositoryModel
from repository_controller import RepositoryController
import json

URL = "https://api.github.com"

def main():
    is_running = True
    
    while is_running:
        user_name = str(input("Buscar repositórios do usuário: "))

        repository_controller = RepositoryController(URL)
        response = repository_controller.get_user_repositories(user_name)

        if not hasattr(response, 'status_code'):
            continue

        if response.status_code != 200:
            continue

        response_json = bynary_to_json(response._content)

        user = RepositoryModel(user_name)
        user.set_repositories(response_json)

        print_repositories(user)

        is_valid_input = False
        while not is_valid_input:
            print("\nEntre com o valor 1 para procurar repositórios de outro usuário")
            print("Entre com o valor 0 para parar a execução do código")
            
            try:
                input_value = int(input("\nComando: "))

                if input_value != 0 and input_value != 1:
                    print("VALOR INVALIDO")
                    continue

                elif input_value == 0:
                    is_valid_input = True
                    is_running = False
                    continue

                else:
                    is_valid_input = True

            except ValueError as error:
                print("COMANDO INVÁLIDO")

    print("FINALIZANDO EXECUÇÃO")
    exit()



def bynary_to_json(response_bynary):
    response_string = response_bynary.decode('utf8').replace("'", '"')

    return json.loads(response_string)

def print_repositories(user):
    print("\nUser name: ", user.get_name())
    print("Repositories: ")
    for repository in user.get_repositories():
        print("-> {} - {}" .format(repository["name"], repository["html_url"]))

if __name__ == "__main__":
    main()