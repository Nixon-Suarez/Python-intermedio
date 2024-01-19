# xargs sirven para cuando no sabemos la cantidad de argumentos que le debemos poner a una funcion 
#       ⬇️tranforma el parametro en iterables
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 4) 
suma(2, 4)
suma(2, 5, 44, 3, 74)

