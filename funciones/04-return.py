# return sirve para almacenar datos en una variable y guardarlos para utilizarlos depues en otra funcion
def suma(a, b):
    resultado = a + b
    return resultado
#     ☝️ almacena un dato en una variable para utilizarlo nuevamente
c = suma(1, 2)
d = suma(c, 2)

print(d)