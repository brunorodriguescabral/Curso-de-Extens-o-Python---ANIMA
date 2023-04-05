print("Utilize ponto no lugar de virgula\n")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))
sexo = input("Digite seu sexo \"M\" ou \"F\": ").casefold()

while sexo != "m" and sexo != "f":
    sexo = input("Digite seu sexo \"M\" ou \"F\": ").casefold()

if sexo == "m":
    print("\nSelecionado: Masculino\n")
    ideal = 72.7 * altura - 50
else:
    print("\nSelecionado: Feminino\n")
    ideal = 62.1 * altura - 44.7

diferenca = peso - ideal
if diferenca > 0:
    print(f"Você está acima do seu peso ideal \"{ideal:.2f}\", precisa perder peso\n")
elif diferenca < 0:
    print(f"Você está abaixo do seu peso ideal \"{ideal:.2f}\", precisa ganhar peso\n")
else:
    print(f"Parabéns, você está exatamente no seu peso ideal \"{ideal:.2f}\"\n")