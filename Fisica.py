from silver import classes
from silver import demoman
from silver import functions


# El que imprime la interfaz de inicio
print("""\n
|===========: Buenos Días :===========|
<><><><><><><><><><><><>><><><><><><><>
╔═════════════════════════════════════╗
║   Nombre Variable ------- Índice    ║
╠═════════════════════════════════════╣ 
║   Velocidad Final --------- VF      ║
║   Velocidad Inicial ------- VI      ║
║   Aceleración ------------- A       ║
║   Tiempo ------------------ T       ║
║   Distancia --------------- X       ║
╚═════════════════════════════════════╝\n
 """)



# Definimos los objetos a partir de la clase "Variable"
vF = classes.Variable("Velocidad Final", False, None, "VF")
vI = classes.Variable("Velocidad inicial", False, None, "VI")
a = classes.Variable("Aceleración", False, None, "A")
t = classes.Variable("Tiempo", False, None, "T")                                                  
x = classes.Variable("Distancia", False, None, "X")


lista_variables = classes.Variable.lista_var # Creamos la lista de las instancias
lista_corto = classes.Variable.lista_corto # Creamos la lista de los nombres cortos juasjuas 



# Verifica que se introduzca un índice válido
while True:
    try:
        indice = str(input("Ingrese el índice de la variable: ")).upper()
        if indice in lista_corto:
            break
    except:
        print("Por favor introduzca un índice válido. ¡ERROR404!.")
    print("Por favor introduzca un índice válido.")



# Pregunta si o no y Mete Valores
for variable in lista_variables: # Pregunta por todas las variables


    # Esto Pregunta
    if indice != variable.corto: # Excluye la variable que se busca
        # La pregunta si o no
        si0no = str(input("\n¿Posee la variable {}?. Responda Sí o No: ".format(variable.nombre))).upper()
        

        # Verifica que se respondió (tiene tilde)
        if si0no == "SI" or si0no == "SÍ" or si0no == "YES" or si0no == "ASIES":
            variable.estado = True


    # Esto mete valores (y se asegura que no hayan errores) PRUEBA
            while True:
                try:
                    variable.valor = float(input("\nIntroduzca el valor de la {}:".format(variable.nombre)))
                    break
                except:
                    print("\nPor favor introduzca un número ;D.")



#La maquina Resolviendo problemas (de hecho delega a otras partes del código a resolverlo) SI


solvable = functions.scan(lista_variables) # Averiguamos si se puede resolver

if solvable == False:
    print("No es posible la resolucion de este problema.")    

else:
    res = demoman.burning_down_the_house(indice, lista_variables)
    print(    
        f"""\n
        ╔═══════════════════════════════════════════════════╗ 
        ║                    RESULTADO                      ║
        ╠═══════════════════════════════════════════════════╣
        ║    El valor de la variable <{indice}> es: {res}   ║
        ╚v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v╝/n
        
        
        """)









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