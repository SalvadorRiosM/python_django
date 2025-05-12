class Bicicleta:
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin
    
    def frenar(self):
        return "La bicicleta esta frenando"
    def avanzar(self):
        return "La bicicleta esta avanzando"
    def girar(self):
        return "La bicicleta esta girando"
    
urbana = Bicicleta("rojo", 8, 27.5)     # Objeto 1
hibrida = Bicicleta("azul", 10, 15.5)   # Objeto 2

print(f"{urbana.avanzar()} y tiene color: {urbana.color}")
