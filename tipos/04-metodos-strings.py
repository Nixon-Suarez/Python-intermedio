animal = "  chanchiti feliz  "
print(animal.upper()) # upper es el metodo que trensforma a mayusculas 
print(animal.lower()) # lower es el metodo que trensforma a minusculas 
print(animal.capitalize()) # capitalize es el metodo que trensforma el primer caracter a mayuscula y el resto lo pasq a minuscula
print(animal.title()) # title es el metodo que trensforma el primer caracter a mayuscula de cada palabra y el resto lo pasa a minuscula
print(animal.strip()) # strip es el metodo que remover los espacios que se encuentren a la derecha o a la izquierda del string
print(animal.rstrip()) # strip es el metodo que remover los espacios que se encuentren a la derecha
print(animal.find("ch")) # find es el metodo que busca una cadena de caracteres que indiquemos y nos da el numero del caracter
print(animal.replace("nch","j")) # replace es el metodo que remplaza un caracter por otro
print("nch" in animal) # in es el metodo que busca una cadena de caracteres que indiquemos y nos da un boolean
print("nch" not in animal) # not in es el metodo que busca que una cadena de caracteres no este y nos da un boolean

print(animal.strip().capitalize) #* se pueden encadenar los metodos
 