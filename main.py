from retangulo import Retangulo
from circulo import Circulo
from triangulo import Triangulo

def main():

    forma = int(input("1-Retangulo, 2-Circulo, 3-Triangulo: "))

    while True:
        und = int(input("1-Calcular em m², 2 - Calcular em cm²: "))
        if und == 1 or und == 2:
            break
        else:
            print("Opção inválida")

    if forma == 1:

        base = int(input("\nDigite o valor da base do retangulo: "))
        altura = int(input("Digite o valor da altura do retangulo: "))

        result = Retangulo(base, altura)

        if und == 1:
            result.exibir_resultado("m²")
        elif und == 2:
            result.exibir_resultado("cm²")

    if forma == 2:
        raio = int(input("\nDigite o valor do raio (Diametro dividido por 2): "))

        result = Circulo(raio)

        if und == 1:
            result.exibir_resultadoC("m²")
        elif und == 2:
            result.exibir_resultadoC("cm²") 

    if forma == 3:
        b = int(input("\nDigite o valor da base do triangulo: "))
        h = int(input("Digite o valor da altura do triangulo: "))
        lado3 = int(input("Digite o valor do terceiro lado do triangulo (sem ser a base ou altura): "))

        result = Triangulo(b, h ,lado3)

        if und == 1:
            result.exibir_resultadoT("m²")
        elif und == 2:
            result.exibir_resultadoT("cm²")

if __name__ ==  "__main__":
    main()