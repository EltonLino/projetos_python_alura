#Contagem de vogais em um texto
def contar_vogais(txt):
    vogais = 'AEIOUÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙ'
    quantidade_vogais = 0
    for letra in frase:
        if letra in vogais:
            quantidade_vogais += 1
    print(f'A quantidade de vogais na frase é: {quantidade_vogais}')

frase = input('Digite um texto: ').upper()
contar_vogais(frase)


