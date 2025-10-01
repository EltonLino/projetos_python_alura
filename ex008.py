def somar(a, b):
    return f'Resultado: {a + b}'

def subtrair(a, b):
    return f'Resultado: {a - b}'

def multiplicar(a, b):
    return f'Resultado: {a * b}'

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    else:
        return f'Resultado: {a / b}'

def calcular(operacao, a, b):
    if operacao == '+':
        return somar(a, b)
    elif operacao == '-':
        return subtrair(a, b)
    elif operacao == '*':
        return multiplicar(a, b)
    elif operacao == '/':
        return dividir(a, b)
    else:
        return "Operação inválida"

try:    
    numer01 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    numer02 = float(input("Digite o segundo número: "))
    resultado = calcular(operacao, numer01, numer02)
    print(resultado)
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira números válidos.")
