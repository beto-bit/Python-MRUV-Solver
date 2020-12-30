import elector
import solver

lista_texto = ["Velocidad Final", "Velocidad Inicial", "Aceleración", "Tiempo", "Distancia"]
lista_bool = [False, False, False, False, False]
lista_numeros = [0, 0, 0, 0, 0]

print()
print("====: ¡Bienvenido, Usuario! :====================")

print("""
   +------------------------+
   | Velocidad Final:     1 |
   | Velocidad Inicial:   2 |
   | Aceleración:         3 |
   | Tiempo:              4 |
   | Distancia:           5 |
   +------------------------+\n
    """)

# Parte que se encarga de meter el valor del índice, y asegurarse de que se introduzcan valores funcionales
lista_comprobacion = ["1", "2", "3", "4", "5"]
indice_malo = input("Introduzca el índice de la variable que busca: ")
while True:
    if indice_malo in lista_comprobacion:
        break
    indice_malo = input("Por favor, introduzca un índice válido: ")
indice = int(indice_malo)

# Parte que imprime las instrucciones
print()
print("~~~~~~~~~~~~~~~~: Instrucciones :~~~~~~~~~~~~~~~~")
print("Introduzca los valores de las variables que posee.\nSi posee la variable introduzca un \"+\".\nEn caso no posea la variable, introduzca un \"-\".")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Parte que se encarga de preguntar si se tienen las variables
j = 0
while True:
    print()
    print("¿Posee la variable de" ,lista_texto[j], "?",end=": ")
    lista_bool[j] = str(input(""))
    while True:
        if lista_bool[j] == "+":
            break
        elif lista_bool[j] == "-":
            break
        lista_bool[j] = str(input("Por favor, introduzca un símbolo válido: "))
    if lista_bool[j] == "+":
        lista_bool[j] = True
    elif lista_bool[j] == "-":
        lista_bool[j] = False
    j += 1
    if j > 4:
        break

# Print de separación
print("\n=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=")

# Verificador de solucionabilidad mediante el elector
if lista_bool[indice - 1] == True:
    print("\n¡Pero si ya tienes resuelto el problema! Revisa bien tus datos.")
else:
    if elector.determinador(lista_bool) == False:
        print("No es posible determinar una solución debido a que no hay suficientes datos.")
    else:
        k = 0
        while True:   # la parte que se encarga de meter valores
            if lista_bool[k] == True:
                print()
                print("Introduzca el valor de", lista_texto[k], end=": ")
                lista_numeros[k] = float(input(""))
            k += 1
            if k > 4:
                break
        RES = solver.buscar(indice, lista_bool, lista_numeros)
        print("\n================================================================================\n")
        print("El valor de la variable", lista_texto[indice-1], "es: ", RES)
        print("\n================================================================================\n")

pepe = input("Presione \"Enter\" para terminar. ¡Muchas Gracias!")