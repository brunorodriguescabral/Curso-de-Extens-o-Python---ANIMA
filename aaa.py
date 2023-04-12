def numero(arg):
    try:
        float(arg)
    except ValueError:
        return False
    return True

n1 = input("Digite: ")

if numero(n1):
    print("é um numero")
else:
    print("Não é")