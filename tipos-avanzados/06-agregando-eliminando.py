mascotas = [
    "sky", 
    "zafiro", 
    "zafiro", 
    "iris", 
    "zafiro", 
    "alika"
]
#    insert sirve para agregar elementos a un listado 
#         ⬇️          ⬇️➡️ valor el cual se quiere agragar en ese indice 
mascotas.insert(1, "carvi")
#              ☝️indice donde se agragara el elemento 
mascotas.append("red ball") #👈 append sirve para agregar un alemento al final de la lista 


#---- remove sirve para eliminar elementos -----
#         ⬇️     ⬇️➡️ elemento que queremos eliminar
mascotas.remove("zafiro")
mascotas.pop() #👈 pop sirve para eliminar el ultimo elemento
mascotas.pop(4) #👈 pero si le ponemos un argumento este es el que sera eliminado

#⬇️del tambien sirve para eliminar
del mascotas[0]
#           ☝️indice del elemento a eliminarç

#         ⬇️ clear elimina todo el arreglo
mascotas.clear()
print(mascotas)