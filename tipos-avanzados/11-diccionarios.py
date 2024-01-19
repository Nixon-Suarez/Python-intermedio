#coleccion de datos que se agrupan por una llave y un valor 

#         ⬇️llave = solo strings
punto = {"x": 25, "y": 50}
#             ☝️   ↖️otra llave y su contenido      
#            contenido  
print(punto)

#*---- acceder a un valor que contiene la llave---------
print(punto["x"])
print(punto["y"])

#*------agregar una nueva llave----
punto["z"] = 75
print(punto)

#*--- preguntar si un valor existe---
# metodo 1
if "lala" in punto:
    print("encontre lala", punto["lala"])

# metodo 2
print(punto.get("x"))
print(punto.get("lala"))

#*----eliminar alguna llave----
#metodo 1
del punto["x"]
#metodo 2 con funcion del
del (punto["z"])
print(punto)

punto["x"] = 25
#*-----iterar llaves con for 
#metodo 1 = itera el valor y la llave

for valor in punto:
    print(valor, punto[valor])

#metodo 2 = nos entrega tuplas
for valor in punto.items():
    print(valor)

#metodo 3 = itera el valor y la llave
for llave, valor in punto.items():
    print(llave, valor)

#*------uso realista de las diccionarios--------------
usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "David"},
    {"id": 3, "nombre": "Elias"},
    {"id": 4, "nombre": "Jens"},
]
for usuario in usuarios:
    print(usuario["nombre"])
