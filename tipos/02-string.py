nombre_curso = "Ultimate Python"
#               0123456789.....
descripcion_curso = """Ultimate Python
este curso es muy util tendra muchas cosas utiles
en gran parte del ambito laboral"""
#                   ☝️las triples comillas sirven para textos muy largos
#                   que se dividen en varias lineas 💪

#     ⬇️Funcion Len sirve para obtener la longitud de un string
print(len(nombre_curso))
print(nombre_curso[8])
#                 ☝️acceder a un caracter en especial ejemplo indice U seria 0
#* cortar el string ⬇️
print(nombre_curso[0:8]) #dede el caracter 0 al caracter 8
print(nombre_curso[9:])# desede el caracter 9 hasta el final
print(nombre_curso[:8]) # desde el caracter 0 hasta el 8
print(nombre_curso[:]) # copia total del string