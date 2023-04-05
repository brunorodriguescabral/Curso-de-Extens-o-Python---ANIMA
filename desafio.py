# joao.coghi@animaeducacao.com.br

import random

combustivel = ""
while combustivel != "1" and combustivel != "2":
    combustivel = input("\nEscolha: \n1- Álcool\n2- Gasolina\n\n")

amount = 0
while amount < 1 or amount > 52:
    amount = int(input("Digite a quantidade de combustivel entre \"1\" e \"52\": "))

alcoolprice = random.uniform(2, 4)
gasolinaprice = random.uniform(4, 6)

if combustivel == "1":
    if amount <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

if combustivel == "2":
    if amount <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

if combustivel == "1":
    price = amount * alcoolprice * (1 - desconto)
else:
    price = amount * gasolinaprice * (1 - desconto)

print(f"\nValor total a ser pago: R$ {price:.2f}\n")
        




