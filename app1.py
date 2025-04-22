Temp1 = int(input("igite a temperatura: "))

print("Escolha a unidade de origem:")       
Unidaade_origem = input("Digite C para Celsius ou F para Fahrenheit: ").upper()

if Unidaade_origem == "C":
    Temperatura_convertida = (Temp1 * 9/5) + 32
    print(f"{Temp1} graus Celsius é igual a {Temperatura_convertida} graus Fahrenheit.")
elif Unidaade_origem == "F":
    Temperatura_convertida = (Temp1 - 32) * 5/9
    print(f"{Temp1} graus Fahrenheit é igual a {Temperatura_convertida} graus Celsius.")
else:
    print("Unidade de origem inválida. Por favor, digite C ou F.")