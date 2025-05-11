def suma(a,b,c):
    return a+b+c

resultado_suma = suma(3,4,5)

print(resultado_suma)


def suma2(*args):           # Esto se usa para cuando quieres usar muchos valores de parametros
    s = 0
    for i in args:
        s += i
    return s

resultado_suma2 = suma2(3,4,5,65,45,12,4,3,74)

print(resultado_suma2)