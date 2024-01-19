# Keyword arguments sirve para indicar el nombre especifico del parametro y hacerlo las veces que desee 

def get_product(**datos):
    print(datos["id"], datos["name"])
#               ☝️asi se  accede a un valor especifico (["nombre del parametro"])
#            ⬇️en kwarg siempre se debe indicar el nombre del parametro el cual va a ser asignado
get_product(id="id",
            name="joge",
            desc="Hot")
# se pueden pasar el numero de parametros y argumentos que queramos