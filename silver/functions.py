# Función que se encarga de ver si se puede resolver
def scan(lista_variables):
    """
    La función 'scan' se encarga de aceptar la lista de las variables y verifica si este sistema en específico
    es resolvible. Funciona contando el número de variables que se tienen. Si se tienen 3 variables o más, es 
    posible resolverlo.
    """
    cuenta_variable = 0 # Asignamos el contador inical a 0
    
    for variable in lista_variables:
        if variable.estado == True:
            cuenta_variable += 1 # sumamos ja (contamos xd)

    # Salida
    if cuenta_variable >= 3:
        return True
    else:
        return False