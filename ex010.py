try:
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= 0:
        print("Valor inválido. O valor do saque deve ser positivo.")
    elif valor_saque % 2 != 0:
        print("Valor inválido. O valor do saque deve ser um número multiplo de 2.")
    else:
        notas_100 = int(valor_saque // 100)
        valor_saque -= notas_100 * 100

        notas_50 = int(valor_saque // 50)
        valor_saque -= notas_50 * 50

        notas_20 = int(valor_saque // 20)
        valor_saque -= notas_20 * 20

        notas_10 = int(valor_saque // 10)
        valor_saque -= notas_10 * 10

        notas_5 = int(valor_saque // 5)
        valor_saque -= notas_5 * 5

        notas_2 = int(valor_saque // 2)
        valor_saque -= notas_2 * 2

        print("Notas necessárias para o saque:")
        if notas_100 > 0:
            print(f"Notas de 100: {notas_100}")
        if notas_50 > 0:
            print(f"Notas de 50: {notas_50}")
        if notas_20 > 0:
            print(f"Notas de 20: {notas_20}")
        if notas_10 > 0:
            print(f"Notas de 10: {notas_10}")
        if notas_5 > 0:
            print(f"Notas de 5: {notas_5}")
        if notas_2 > 0:
            print(f"Notas de 2: {notas_2}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")