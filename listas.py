numeros = [1,2,3]
for i in range(8):
    numeros.append(int(input("Introduce un numero: ")))  # agrega iteracion a la lista de numeros

numeros.sort()      # ordena la lista de numeros

print(f"Los numero ordenados de menor a mayor son: {numeros}")
