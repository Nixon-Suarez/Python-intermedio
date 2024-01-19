usuarios = [
        ["Juan", 4], 
        ["Carvi", 1], 
        ["diabetico", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuarios[0])
# print(nombres)

# ☝️esto es lo mismo que esto⬇️ pero mas elegante🥵
#? ⬇️map
nombres = [usuario[0] for usuario in usuarios]
# sintaxis ⬇️
# nombres = [expression for item in items]
print(nombres)

#-----fALTRAR------
#? ⬇️filter
nombres = [ usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

#--- transformar y filtara ----

nombres = [ usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

#!--- MAP transformar----
nombres = list(map(lambda usauario: usauario[0], usuarios))
#nombres es una nueva lista(list) que va a transformar(map) a los usuarios el cual resive una funcion lambda a la cual tenemos 
# que pasar un item(usuario) y el elemento que queremos retornar (usuario[0]) despues indicamos que es lo que queremos iterar(usuarios)
print(nombres)

#!------FILTER filtrar----
menosUsuarios = list(filter(lambda usauario: usauario[1] > 2,usuarios))
print(menosUsuarios)