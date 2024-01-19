# la tupla es lo mismo que una listas pero no puedes modificar la tupla pero si puedes crear otra tubla con una ya existente 
# se utilizan cuando no se quiere que se eliminen elementos por accidente

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

#-----convertir una lista en una tupla------
punto = tuple([1, 2])
     #  ☝️tuple convierte una lista en una tupla
print(punto)

#------ACCEDE A ELEMENTOS DE LA TUPLA----
#                ⬇️esto genera una nueva tupla la cual se almecena en una nueva variable
menos_numeros = numeros[:2]
print(menos_numeros)

#------desempaquetar tuplas----
primero, segundo, *otros = numeros
print(primero, segundo, otros)

#----iterar las tuplas---
for n in numeros:
    print(n)

#---convertir una tupla a lista y modificar la lista----
listaNumeros = list(numeros)
listaNumeros[0] = "Holaaassss"
print(listaNumeros)
