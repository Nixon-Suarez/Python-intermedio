numeros = [1, 27, 3, 4, 38, 5, 7, 8, 9, 6]

#        ⬇️sort ordena los numeros de menor a mayor
# numeros.sort()
# numeros.sort(reverse=True) #👈 ordena de mayor a menor 
numeros2 = sorted(numeros) # 👈sorted genera una nueva lista igual
numeros2 = sorted(numeros, reverse=True)  #👈 ordena de mayor a menor 

print(numeros)
print(numeros2)

usuarios = [[4, "Juan"], 
            [1, "Carvi"], 
            [5, "diabetico"]
]
usuarios.sort() # sort solo ordena elementos del inicio ordenables
print(usuarios)

print("---🥵---")
#----ordenar elementos no ordenables
def ordena(elemento):
    return elemento[1]

usuarios = [["Juan", 4], 
            ["Carvi", 1], 
            ["diabetico", 5]
]
usuarios.sort(key=ordena)
print(usuarios) 

print("---🥵---")
#!---------funcion anonima o funcion lambda-----

#                 parametros      el=elemento
#                        ⬇️  ⬇️➡️contenido de la funcion - valor de retorno 
usuarios.sort(key=lambda el: el[1])
print(usuarios) 

#!UTILIZAR LAS FUNCIONES LAMBDA MUCHAS VECES EN EL MISMO CODIGO ES CONSIDERADO UNA MALA PRECTICA
