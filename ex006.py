import random

def jokenpo(user, computer):
    if user == computer:
        print(f'Computador escolheu {computer}')
        print('Empate!')
    elif ((user == 'pedra' and computer == 'tesoura') or 
        (user == 'papel' and computer == 'pedra') or 
        (user =='tesoura' and computer == 'papel')):

        print(f'O computador escolheu {computer}')
        print('Você venceu!')
    else:
        print(f'O computador escolheu {computer}')
        print('Você Perdeu!')
        

opcoes = ['pedra', 'papel','tesoura']
user = input('pedra, papel ou tesoura? Escolha: ').strip().lower()
while user not in opcoes:
    print('Opção inválida!')
    user = input('pedra, papel ou tesoura? Escolha: ').strip().lower()
computer = random.choice(['pedra','papel','tesoura'])
jokenpo(user,computer)