lista1 = (1, 2, 3, 4)
# print(lista1) #imprime una lista
# print(*lista1) #imprime como 1, 2, 3, 4 como argumentos - esto tambien sirve con las tuplas

lista2 = [5, 6]

# combinar listas
combinada = ["Holaaasss", *lista1, "carenalga", *lista2, "pspspss"]
print(combinada)

# conbinar diccionarios 
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = { **punto1, "la": "la", **punto2, "z": "hL"}
print(nuevoPunto)