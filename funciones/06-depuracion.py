def largo(texto):
    resultado = 0
    for _ in texto: # por cada caracter en el texto 
        resultado += 1 # sumar uno a resultado
    return resultado

print("Chanchito") 
l = largo("Holassss")
print(l)