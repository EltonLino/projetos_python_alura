def analisar_frase(texto):
    quantidade_maior_que_dez = 0
    palavras_maiores_que_dez = []
    for palavra in texto:
        if len(palavra) > 10:
            quantidade_maior_que_dez += 1
            palavras_maiores_que_dez.append(palavra)
    if quantidade_maior_que_dez == 0:
        print('Nenhuma palavra longa foi encontrada no texto.')
    else:
        print('Palavras longas encontradas: ', end='')
        print(', '.join(palavras_maiores_que_dez))


texto = input('Digite um texto: ').strip().split()
analisar_frase(texto)

