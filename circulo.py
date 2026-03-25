class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_areaC(self):
        return  3.14 * (self.raio ** 2)
    
    def calcular_perimetroC(self):
        return 2 * 3.14 * self.raio
    
    def exibir_resultadoC(self, und):
        areaC = self.calcular_areaC()
        perimetroC = self.calcular_perimetroC()

        print(f"A área do circulo é: {areaC}{und}")
        print(f"O perímetro do circulo é: {perimetroC}{und.replace('²','')}")
