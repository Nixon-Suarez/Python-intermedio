numeros = [1, 2, 3, 4, 5]

#! fe0 !
# primer = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
#! Bueno ⬇️
primero, segundo, tercero, cuarto, quinto = numeros 
print(primero, segundo, tercero)

#--- enpaquetar datos----
#          ⬇️ esto hace que el resto de las elementos eseptuando al primero y el segundo se enpaquete en una variable llamada otros
primero, segundo, *otros = numeros
print(primero, segundo, otros)

#-- acceder al primero y al ultimo dato ---

primero, *otros, ultimo = numeros
print(primero, ultimo, otros)

# accede al penultimo dato 
primero, *otros, penu, ultimo = numeros
print(primero, penu, otros, ultimo)
