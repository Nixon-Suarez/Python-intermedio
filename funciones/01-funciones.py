
#! crear nuestra propia funcion 
def hola():
    print("Hola")
    print("Hola!!!!!!!!!!")
#                             |   se tienen que dejar dos espacios depues de la creacion de la funcion                       
# ⬇️asi se llama la funcion   | 
hola()

#         ⬇️ esto se llama un parametro
def ha(nombre):
    print("Ha")
    print(f"bienvenido {nombre}")

#     ⬇️argumentos se debe poner un valor esto es obligatorio
ha("Juanzzz")
ha("Marrano")

#-----------poner mas de un parametro
def hl(nombre, apellido):
    print("Hl")
    print(f"como estas {nombre} {apellido} ??")

hl("Juan", "ramirez")
hl("😩", "😁")

#-----------poner parametros opcionales 
def hol(nombre, apellido="😎"):
    print("Hol")
    print(f"como estas {nombre} {apellido} ??")

hol("Juan", "ramirez")
hol("😩")

#-------------argumentos nombrados
# ejemplo no recuerdo el orden de los argumentos entonces lo puede pasar 
# simplemente nombro los argumentos con el parametro correspondiente 
hol(apellido="Hernandes", nombre="Elias")
