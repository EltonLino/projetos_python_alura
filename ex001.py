#Calculando a gorjeta em um restaurante
def calcular_gorjeta(conta, gorjeta):
        return conta * (gorjeta/100)


conta = float(input('Digite o valor da conta: '))
gorjeta = float(input('Digite a porcentagem da gorjeta: '))
print(f'Valor da gorjeta: R$ {calcular_gorjeta(conta,gorjeta):.2f}')
print(f'Total a pagar: R$ {conta + gorjeta:.2f}')
