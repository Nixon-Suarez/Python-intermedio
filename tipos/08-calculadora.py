n1 = int(input("escriba el primer numero: "))
n2 = int(input("escriba el segundo numero: "))

suma = n1 + n2
resta= n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}, 
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {multi}.
el resultado de la divicion es {div}.
"""
print(mensaje)