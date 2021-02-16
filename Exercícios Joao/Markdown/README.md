# exercicio-python

Este programa extrai os repositórios de um usuário do GitHub e os exibe.

## Requisitos
É necessário ter python 3.X instalado.

## Intalação
Este programa não necessita instalação. Siga as intruções abaixo para executá-lo.

## Execução
Navegue pelo shell até o diretório na qual o arquivo `exercicio-python.py` se encontra e execute o comando `py exercicio-python.py`. O programa é auto-explicativo, e portanto não é necessário um tutorial de como utilizá-lo. Existem exemplos na próxima seção.

## Exemplos
```
PS C:\Users\joao.monteiro\Documents> py exercicio-python.py
Digite o usuário: Mike
Aqui estão os repositórios deste usuário:
mike.github.io
```
```
PS C:\Users\joao.monteiro\Documents> py exercicio-python.py
Digite o usuário: John
Aqui estão os repositórios deste usuário:
acts-as-taggable-on
acts_as_commentable_with_threading
AlphaVantageRB
amplifyapp
backup
(...)
geocoder
hello-world-golang
homebrew
```
```
PS C:\Users\joao.monteiro\Documents> py exercicio-python.py
Digite o usuário: NotARealUser999
Aqui estão os repositórios deste usuário:
```
Neste último caso o usuário não existe e o programa entende como se ele não tivesse nenhum repositório.