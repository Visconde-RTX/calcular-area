from retangulo import Retangulo
from circulo import Circulo

def main():

    forma = int(input("1-Retangulo, 2- Circulo: "))

    while True:
        und = int(input("1-Calcular em m², 2 - Calcular em cm²: "))
        if und == 1 or und == 2:
            break
        else:
            print("Opção inválida")

    if forma == 1:

        base = int(input("Digite o valor da base do retangulo: "))
        altura = int(input("Digite o valor da altura do retangulo: "))

        result = Retangulo(base, altura)

        if und == 1:
            result.exibir_resultado("m²")
        elif und == 2:
            result.exibir_resultado("cm²")

    if forma == 2:
        raio = int(input("Digite o valor do raio (Diametro dividido por 2): "))

        result = Circulo(raio)

        if und == 1:
            result.exibir_resultadoC("m²")
        elif und == 2:
            result.exibir_resultadoC("cm²") 

if __name__ ==  "__main__":
    main()