# def suma(a,b,c):
#     return a+b+c

# resultado_suma = suma(3,4,5)

# print(resultado_suma)


# def suma2(*args):           # Esto se usa para cuando quieres usar muchos valores de parametros
#     s = 0
#     for i in args:
#         s += i
#     return s

# resultado_suma2 = suma2(3,4,5,65,45,12,4,3,74)

# print(resultado_suma2)


# def lenguaje(nombre,*args):
#     return (f"Hola {nombre} tus lenguajes favoritos son: {args}")

# lenguaje1 = lenguaje("Orlandito", "Python", "C#", "Java")

# print(lenguaje1)


def lenguaje(nombre,**kwargs):
    print(f"Hola {nombre}")
    print("Buscando informacion acerca de tus lenguajes favoritos...")
    print("Cargando informacion... \n")

    print("Informacion: ")
    contador = 0
    print(type(kwargs))
    for clave in kwargs:
        contador += 1
        print(f"Tu lenguaje favorito numero {contador} es: {kwargs[clave]}")

lenguaje("Eduardo", lenguaje1 = "Ruby", lenguaje2 = "Python", lenguaje3 = "Java", lenguaje4 = "PHP")

