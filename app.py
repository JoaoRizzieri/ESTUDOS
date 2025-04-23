

# Digite o primeiro número: 10
# Digite o segundo número: 0
# Digite a operação (+, -, *, /): /
# Erro: não é possível dividir por zero.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
digite_a_operação = input("Digite a operação (+, -, *, /): ")

if digite_a_operação == "+":
    resultado = numero1 + numero2
    print("Resultado: ", resultado)
elif digite_a_operação == "-":
    resultado = numero1 - numero2
    print("Resultado: ", resultado)
elif digite_a_operação == "*":
    resultado = numero1 * numero2
    print("Resultado: ", resultado)
elif digite_a_operação == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado: ", resultado)
    else:
        print("Erro: seu idiota, vc é burro?.")
        print("git status")
        print("git status")
