nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
curso = input("Digite seu curso: ")

a = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

print(a)
print(a.get("nome"))