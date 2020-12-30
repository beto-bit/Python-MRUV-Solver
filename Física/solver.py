# Este es el programa que se encarga de gestionar las posibles soluciones que se pueden dar a una ecuación

# Búsqueda de VF
def busc_VF(listaBo, listaNum):
    vf = listaNum[0]
    vo = listaNum[1]
    a = listaNum[2]
    t = listaNum[3]
    x = listaNum[4]

    if listaBo[1] == False:
        return a*t/2 + x/t
    elif listaBo[2] == False:
        return 2*x/t - vo
    elif listaBo[3] == False:
        return (vo**2 + 2*a*x)**0.5
    elif listaBo[4] == False:
        return vo + a*t        

# Busqueda de VO
def busc_VO(listaBo, listaNum):
    vf = listaNum[0]
    vo = listaNum[1]
    a = listaNum[2]
    t = listaNum[3]
    x = listaNum[4]

    if listaBo[0] == False:
        return x/t - a*t/2
    elif listaBo[2] == False:
        return 2*x/t - vf
    elif listaBo[3] == False:
        return (vf**2 - 2*a*x)**0.5
    elif listaBo[4] == False:
        return vf - a*t

# busqueda de aceleración
def busc_A(listaBo, listaNum):
    vf = listaNum[0]
    vo = listaNum[1]
    a = listaNum[2]
    t = listaNum[3]
    x = listaNum[4]

    if listaBo[0] == False:
        return 2*(x - vo*t)/(t**2)
    elif listaBo[1] == False:
        return 2*(vf*t - x)/(t**2)
    elif listaBo[3] == False:
        return ((vf**2)-(vo**2))/(2*x)
    elif listaBo[4] == False:
        return (vf - vo)/t

# Busqueda de Tiempo
def busc_T(listaBo, listaNum):
    vf = listaNum[0]
    vo = listaNum[1]
    a = listaNum[2]
    t = listaNum[3]
    x = listaNum[4]

    if listaBo[0] == False:
        return (-vo + (vo**2 + 2*a*x)**0.5) / a
    elif listaBo[1] == False:
        return (vf + (vf**2 - 2*a*x)**0.5) / a
    elif listaBo[2] == False:
        return 2*x/(vf + vo)
    elif listaBo[4] == False:
        return (vf - vo)/a

# Buscando la posición
def busc_X(listaBo, listaNum):
    vf = listaNum[0]
    vo = listaNum[1]
    a = listaNum[2]
    t = listaNum[3]
    x = listaNum[4]

    if listaBo[0] == False:
        return vo*t + a*(t**2)/2
    elif listaBo[1] == False:
        return vf*t - a*(t**2)/2
    elif listaBo[2] == False:
        return t*(vf + vo)/2
    elif listaBo[3] == False:
        return ((vf)**2 - (vo)**2) /(2*a)



# La función principal
def buscar(indice, listaBool, listaNumeros):
    if indice == 1:
        return busc_VF(listaBool, listaNumeros)
    elif indice == 2:
        return busc_VO(listaBool, listaNum)
    elif indice == 3:
        return busc_A(listaBool, listaNumeros)
    elif indice == 4:
        return busc_T(listaBool, listaNumeros)
    elif indice == 5:
        return busc_X(listaBool, listaNumeros)