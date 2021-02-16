def process_numbers(lista):
    novaLista = []
    if isinstance(lista, list):
        for i in lista:
            if str.isnumeric(str(i)):
                novaLista.append(int(i))
    novaLista.sort()
    return novaLista
    


def process_names(lista):
    novaLista = []
    if isinstance(lista, list):
        for i in lista:
            if str.isalpha(str(i)):
                novaLista.append(str(i))
    novaLista.sort()
    return novaLista
