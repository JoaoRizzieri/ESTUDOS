print("para saber seu aumento salarial, digite seu salario atual abaixo")

salario = float(input("qual, seu salario atual: "))

if salario <= 1499.99:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print(f"seu novo salarioé: {novo_salario:.2f}")
elif salario >= 1500 and salario <= 2999.99:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"seu novo salarioé: {novo_salario:.2f}")
elif salario > 3000:
    aumento = salario * 0.1
    novo_salario = salario + aumento
    print(f"seu novo salarioé: {novo_salario:.2f}")