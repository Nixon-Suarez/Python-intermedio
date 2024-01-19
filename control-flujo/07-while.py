# numero = 1
# while numero < 100: <-
#     print(numero)     |  ejecuta hasta que se deja de cumplir la condicion inicial
#     numero *= 2     ---


comando = ""

#              ⬇️se utiliza el metodo upper para evitar errores de escritura
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

#--------loop infinito----------
comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower == "salir":  # en los loops infinitos siempre debes poner una salida 
        break