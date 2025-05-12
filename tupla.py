# Crea una tupla con numeros, luego pedir un numero por teclado e indicar
# cuantas veces se repite

numeros = (5,6,7,8,5,5,6,90,12,14,12)

numero = int(input("Dame un numero: "))

veces_repetidas = numeros.count  # Variable que cuenta las veces que se repite
                                 # un numero en la tupla
print(f"El numero se repite: {veces_repetidas(numero)} veces") #Cuenta las veces que se repite el numero que le diste

