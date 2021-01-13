from silver import classes # Importamos las clases (Aquí fue donde hice el cambio xD)


# Creamos los diccionarios 
vf_formu = {
    "VF": "None",
    "VI": "a*t/2 + x/t",
    "A": "2*x/t - vi",
    "T": "(vi**2 + 2*a*x)**0.5",
    "X": "vi + a*t"
}

vi_formu = {
    "VF": "x/t - a*t/2",
    "VI": "None",
    "A": "2*x/t - vf",
    "T": "(vf**2 - 2*a*x)**0.5",
    "X": "vf - a*t"
}

a_formu = {
    "VF": "2*(x - vi*t)/(t**2)", 
    "VI": "2*(vf*t - x)/(t**2)",
    "A": "None",
    "T": "((vf**2)-(vi**2))/(2*x)",
    "X": "(vf - vi)/t"
}

t_formu = {
    "VF": "(-vi + (vi**2 + 2*a*x)**0.5) / a",
    "VI": "(vf + (vf**2 - 2*a*x)**0.5) / a",
    "A": "2*x/(vf + vi)",
    "T": "None",
    "X": "(vf - vi)/a"  
}

x_formu = {
    "VF": "vi*t + a*(t**2)/2",
    "VI": "vf*t - a*(t**2)/2",
    "A": "t*(vf + vi)/2",
    "T": "((vf)**2 - (vi)**2) /(2*a)",
    "X": "None"
}


# Creamos los objetos que almacenen las fórmulas ;)
obj_VF = classes.FormulHaze("VF", vf_formu) # obj_A.VF      Contiene la formula para aceleracion y el .VF dice que es sin VF
obj_VI = classes.FormulHaze("VI", vi_formu)
obj_A = classes.FormulHaze("A", a_formu)
obj_T = classes.FormulHaze("T", t_formu)
obj_X = classes.FormulHaze("X", x_formu)



# RESULEVE LA WEA
# Funcion para tener acceso a esas weas
def burning_down_the_house(indice, lista_variables):
    # Variables pa resolver
    vf = lista_variables[0].valor
    vi = lista_variables[1].valor
    a = lista_variables[2].valor
    t = lista_variables[3].valor
    x = lista_variables[4].valor

    # Falta variables jaja
    lista_falta = []

    # Bucle para llenar listafalta
    for variable in lista_variables:
        if variable.estado == False:
            lista_falta.append(variable)
    
    # XD?
    if len(lista_falta) == 0:
        if indice == "VF":
            res = eval(obj_VF.VI)
        elif indice == "VI":
            res = eval(obj_VI.VF)
        elif indice == "A":
            res = eval(obj_A.VF)
        elif indice == "T":
            res = eval(obj_T.VF)
        elif indice == "X":
            res = eval(obj_X.VF)




    # Final
    return res

        



















#it just works
#lucky, pluck
# ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
# ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
# ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
# ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
# ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
# ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
