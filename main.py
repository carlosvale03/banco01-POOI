from random import randint
from conta import Conta, Cliente

def numeroConta():
    x = randint(100, 1000)
    return x


josefino = dict()
while True:
    print('''\nEscolha uma das opições abaixo: \n1-Criar conta \n2-Listar contas 
3-Sacar valor \n4-Depositar valor \n5-Excluir conta \n6-Transferir \n7-Extrato \n8-Quantidade de contas \n9-Sair''')
    op = int(input('Operação: '))
    print('')

    if op == 1:
        print('<<' * 5, ' CRIAR CONTA ', '>>' * 5)
        numero = numeroConta()
        name = input('Digite o nome do titular da conta: ')
        sNome = input('Digite o sobrenome: ')
        cpf = str(input('CPF: '))
        cliente = Cliente(name, sNome, cpf)
        josefino[numero] = Conta(numero, cliente)
        print(f'''Conta criada com sucesso \nNúmero da conta: {numero}''')

    elif op == 2:
        print('<<' * 9, ' LISTAGEM DAS CONTAS ', '>>' * 9)
        
        for i in josefino.keys():
            josefino[i].listar()

    elif op == 3:
        print('<<' * 9, ' SACAR VALOR ', '>>' * 9)
        n = int(input('Digite o número da conta que deseja fazer a operação: '))
        v = float(input('Digite o valor que vai sacar: '))
        juverdina = josefino[n].sacar(v)
        if juverdina == True:
            print('Saque realizado com sucesso! :)')
            josefino[n].historico.add_transacoes(f'Saque no valor de R${v:0.2f} realizado com sucesso!')
        else:
            josefino[n].historico.add_transacoes('Falha na operação de saque! :(')
            print('Falha na operação, valor invalido! :(')

    elif op == 4:
        print('<<' * 8, ' DEPOSITAR VALOR ', '>>' * 8)
        n = int(input('Digite o número da conta que deseja fazer a operação: '))
        v = float(input('Digite o valor que vai depositar: '))
        juverdina = josefino[n].depositar(v)
        if juverdina == True:
            print('Deposito realizado com sucesso! :)')
            josefino[n].historico.add_transacoes(f'Deposito no valor de R${v:0.2f} realizado com sucesso!')
        else:
            print('Falha na operação, valor invalido! :(')
            josefino[n].historico.add_transacoes('Falha na operação de saque! :(')

    elif op == 5:
        print('<<' * 9, ' EXCLUIR CONTA ', '>>' * 9)
        n = int(input('Digite o número da conta que deseja fazer a operação: '))
        print(f'A conta de {josefino[n].titular} foi excluida com sucesso!')
        josefino.pop(n)

    elif op == 6:
        print('<<' * 8, ' TRANSFERIR VALOR ', '>>' * 8)
        n = int(input('Digite o número da conta de onde será transferido o valor: '))
        v = float(input('Digite o valor que vai ser transferido: '))
        c2 = int(input('Digite o número da conta de destino: '))
        juverdina = josefino[n].sacar(v)
        juverdina2 = josefino[c2].depositar(v)
        if juverdina and juverdina2 == True:
            print('Transferência realizada com sucesso! :)')
            josefino[n].historico.add_transacoes(f'Transferência para a conta de {josefino[c2]._titular.nome} no valor de R${v:0.2f} realizada com sucesso!')
        else:
            print('Falha na operação, valor invalido! :(')
            josefino[n].historico.add_transacoes('Falha na operação de transferência! :(')

    elif op == 7:
        print('<<', ' EXTRATO ', '>>\n')
        n = int(input('Digite o número da conta na qual deseja ver o extrato: '))
        josefino[n].exibir()

    elif op == 8:
            print(f'O banco tem {Conta.num_contas} conta(s) cadastrada(s)!')

    elif op == 9:
        print('<<', 'VOLTE SEMPRE! :)', '>>\n')
        print('Programa encerrado!')
        break

    
    else:
        print('Valor invalido! :(')
