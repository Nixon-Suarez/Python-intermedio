# set significa grupo o conjunto 
# es una coleccion de datos que no esta ordenada y no se puede repetir
# los sets hacen que los datos nunca se repitan 

#     set elimina los duplicados  
primer= {1, 1, 2, 2, 3, 4} 
print(primer)
#* set se puede trabajar como las listas 
# primer.add(5)
# primer.remove(1)
# print(primer)

#--- crea un set en base de una lista tambien se puede hacer una tupla ---

segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)

#----       ⬇️UNION = unir dos sets-----
print(primer | segundo)
#------     ⬇️interseccion = elementos que se encuentren en el primer y en el segundo set-------
print(primer & segundo)
# Diferencia = restarle los elementos de segundo a primer 
print(primer - segundo)
# diferencia simetrica = elementos que se encuentren en el primero y en el segundo pero no en ambos
print(primer ^ segundo)

#! con los sets no podemos acceder a un dato en especifico 
#--- verificar si un elemento existe ---
if 5 in segundo:
    print("si existe")

