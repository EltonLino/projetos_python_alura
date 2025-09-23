#Validando um CPF
def validar_cpf(cpf):
    if len(cpf) != 11:
        return print('ERRO: O CPF deve ter exatamente 11 dígitos.')
    elif not cpf.isdigit():
        print('Erro: O CPF deve conter apenas números.')
    else:
        print('CPF válido')


cpf = input('Digite o seu CPF:').strip()
validar_cpf(cpf)
