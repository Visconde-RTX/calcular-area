class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def exibir_resultado(self, und):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()

        print(f"\nA área do retângulo é: {area:.2f}{und}")
        print(f"O perímetro do retângulo é: {perimetro:.2f}{und.replace('²','')}")