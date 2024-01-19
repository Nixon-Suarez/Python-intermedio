# and, or, not 

#* and
# x > 5 y > 10 
# True    True   = True
# False    True  = False
# True    False  = False 
# False   False  = False 

gas = True
encendido = True 

if gas and encendido:
    print("El coche se enciende") 

#* or 
# x > 5 y > 10
# True     True  = True   
# True     False = True
# False    True  = True
# False    False = False

gas = True
encendido = False

if gas or encendido:
    print("El coche se enciende") 

#* not 
# negacion de un valor 

gas = False
encendido = False  

if not gas or encendido:
    print("El coche se enciende") 

#---------------------------
 # and, or y not

gas = False
encendido = True 
edad = 18

#              ⬇️ejecuta primero por que esta en parentesis 
if not gas and (encendido or edad > 17):
    print("El coche se enciende")
