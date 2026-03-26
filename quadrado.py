class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_areaQ(self):
        return self.lado ** 2
    
    def calcular_perimetroQ(self):
        return self.lado * 4
    
    def exibir_resultadoQ(self, und):
        areaQ = self.calcular_areaQ()
        perimetroQ = self.calcular_perimetroQ()

        print(f"\nA área do quadrado é: {areaQ}{und}")
        print(f"O perímetro do quadrado é: {perimetroQ}{und.replace('²','')}")
