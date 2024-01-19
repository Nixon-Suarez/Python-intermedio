#sirve para iterar una lista, buscar elementes, operaciones matematicas, etc.

#              ⬇️nos da una secuencia de numeros que comienza desde el cero hasta el numero indicado menor uno (o, 1, 2, 3, 4)
#*for numero in range (5):
#     ☝️esta variable tomar el valor de cada uno de los elementos que se encuentran indicados 
    #* print(numero)
    #* print(numero ** 99)
    #* print(numero * "Hola BB")

#--------for else---------

buscar = 4      #⬇️iterable
for numero in range (5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
#   ☝️break nos permite detener la ejecucion
    else:
        print("no lo encontre😩")

for chat in ("Hola"):
    print(chat)
