def main():
    print("\n========= Bem vindo ao programa para Cálculo de IMC =========\n")
    peso = float(input("Digite o seu peso em KG: "))
    altura = float(input("Digite a sua altura: "))

    imc = calcular_imc(peso, altura)
    exibir_imc(imc)

def calcular_imc(peso, altura):
    return peso / (altura **2)
    
def exibir_imc(imc):
    if imc < 18.5:
        print(f"\nSeu IMC é {imc:.2f}, Abaixo do Peso\n")
    
    elif imc >=18.5 and imc <=24.9:
        print(f"\nSeu IMC é {imc:.2f}, Peso Normal\n")

    elif imc >=25 and imc <=29.9:
        print(f"\nSeu IMC é {imc:.2f}, Sobrepeso\n")

    elif imc >=30 and imc <=34.9:
        print(f"\nSeu IMC é {imc:.2f}, Obesidade Grau 1\n")

    elif imc >=35 and imc <=39.9:
        print(f"\nSeu IMC é {imc:.2f}, Obesidade Grau 2\n")

    else:
        print(f"\nSeu IMC é {imc:.2f}, Obesidade Grau 3 (Mórbida)\n")

    print("\n==== Fim do cálculo. Obrigado por utilizar meu programa ====\n")

main()