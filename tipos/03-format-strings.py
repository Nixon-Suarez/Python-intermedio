nombre = "Nixon"
apellido = "sua"
# nombre_completo = nombre + " " + apellido 
# forma eneficiente             ☝️el mas es el signo de concatenecion o formatear
nombre_completo = f"{nombre} {apellido}"
#*               ☝️la f es el operador de formateo
nombre_c = f"{nombre[0]} {5 + 6}"
#             output primer caracter y 11
print (nombre_completo)
print (nombre_c)