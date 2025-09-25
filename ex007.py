import random

def adivinhar_numero(computer, user):
    while computer != user:
        if computer > user:
            user = int(input('Muito baixo. Tente novamente: '))
        else:
            user = int(input('Muito alto. Tente novamente: '))
    print(f'Parabéns! Você acertou o número {computer}')

computer = random.randint(1,100)
try:
    user = int(input('Tente adivinhar o número (1-100): '))
    while user < 1 or user > 100:
        user = int(input('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100: '))
except ValueError:
        print('Entrada inválida, digite apenas números')
        exit()

adivinhar_numero(computer, user)