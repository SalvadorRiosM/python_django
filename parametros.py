# Parametros *args

def datos_de_usuario(*args):
    print(args)

datos_de_usuario("Orlando", "Rios", 5, "Fom. 51")  # Se crea una tupla en el output


# Paratros **kwargs

def datos_de_usuario(**kwargs):
    print(kwargs)
    
diccionario = datos_de_usuario(nombre="Orlando", apellido="Rios", edad=5, colonia="Fom. 51")