import random, string

lista_caracteres = string.ascii_letters + string.punctuation + string.digits

numeros_de_caracteres = int(input('Digite o número de caractereres para sua senha: '))
senha = random.choices(lista_caracteres,k=numeros_de_caracteres)
print(f'Senha gerada: {"".join(senha)}')