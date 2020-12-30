# Parte que determina si es resolvible - - - CREO QUE ES TODO
def determinador(lista_b):
    x = 0
    for i in lista_b:
        if i == True:
            x += i
    if x >= 3:
        return True
    else:
        return False