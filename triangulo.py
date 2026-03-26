class Triangulo:
    def __init__(self, b, h, lado3):
        self.b = b
        self.h = h
        self.lado3 = lado3

    def calcular_areaT(self):
        return (self.b * self.h) / 2
        
    def calcular_perimetroT(self):
        return self.b+ self.h + self.lado3
    
    def exibir_resultadoT(self, und):
        areaT = self.calcular_areaT()
        perimetroT = self.calcular_perimetroT()

        print(f"A área do triangulo é: {areaT}{und}")
        print(f"O perímetro do triangulo é: {perimetroT}{und.replace('2','')}")