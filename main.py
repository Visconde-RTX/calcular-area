from retangulo import Retangulo

def main():

    while True:
        und = int(input("1-Calcular em m², 2 - Calcular em cm²: "))
        if und == 1 or und == 2:
            break
        else:
            print("Opção inválida")

    base = int(input("Digite o valor da base: "))
    altura = int(input("Digite o valor da altura: "))

    result = Retangulo(base, altura)

    if und == 1:
        result.exibir_resultado("m²")
    elif und == 2:
        result.exibir_resultado("cm²")

if __name__ ==  "__main__":
    main()