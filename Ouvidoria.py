
dados = []
opcao = 1
reclamacao2 = []
elogio2 = []
print('-------------Seja Bem-vindo(a)-------------')

while opcao != 7:
    print()
    print('1)Enviar reclamação\n')
    print('2)Enviar elogio\n')
    print('3)Ver lista de ocorrências\n')
    print('4)Remover ocorrências\n')
    print('5)Consultar por ID\n')
    print('6)Editar ocorrências\n')
    print('7)Sair\n')
    print()

    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print()
        reclamacao = input('Descreva seu problema: ')
        reclamacao2.append(reclamacao)
        dados = reclamacao2
        print()
        print('Registrado com sucesso!')

    elif opcao == 2:
        print()
        elogio = input('Elogio a ser feito: ')
        elogio2.append(elogio)
        dados = elogio2
        print('Registrado com sucesso!')

    elif opcao == 3:
        if len(dados) == 0:
            print('Não existem novas ocorrências!')
        elif len(dados) >= 1:
            tipo = int(input('O que deseja exibir? \n1)Reclamações \n2)Elogios \n3)Ambos \nDigite: '))
            if tipo == 1:
                print("---------Reclamações---------")
                print()
                for i in range(len(reclamacao2)):
                    print(str(i + 1) + 'º reclamação', reclamacao2[i])
            elif tipo == 2:
                print("---------Elogios---------")
                print()
                for i in range(len(elogio2)):
                    print(str(i + 1) + 'º elogio', elogio2[i])
            elif tipo == 3:
                print("---------Reclamações---------")
                print()
                for i in range(len(reclamacao2)):
                    print(str(i + 1) + 'º reclamação', reclamacao2[i])
                print("---------Elogios---------")
                print()
                for i in range(len(elogio2)):
                    print(str(i + 1) + 'º elogio', elogio2[i])
            else:
                print('Opção inválida!')
                
    elif opcao == 4:
        remover = int(input('Que tipo de ocorrência deseja remover? \n1)Reclamações \n2)Elogios \n3)Apagar tudo \nDigite: '))
        if remover == 1:
            if len(reclamacao2) == 0:
                print('Não existem reclamações registradas!')
            else:
                for i in range(len(reclamacao2)):
                    print(str(i + 1)+ 'º reclamação', reclamacao2[i])
                apagar = int(input('Qual ocorrência deseja remover?: '))
                if apagar > len(reclamacao2) or apagar <0:
                    print('Opção inválida!')
                else:
                    reclamacao2.pop(apagar - 1)
                    print('Removido com sucesso!')
        elif remover == 2:
            if len(elogio2) ==0:
                print('Não existem elogios registrados!')
            else:
                for i in range(len(elogio2)):
                    print(str(i + 1)+ 'º elogio', elogio2[i])
                apagar = int(input('Qual ocorrência deseja remover? \nDigite: '))
                if apagar > len(elogio2) or apagar <0:
                    print('Opção inválida!')
                else:
                    elogio2.pop(apagar - 1)
                    print('Removido com sucesso!')
        elif remover == 3:
            if len(dados) == 0:
                print('Não existem ocorrências para remover!')
            else:
                print()
                dados.clear()
                elogio2.clear()
                reclamacao2.clear()
                print('Registros apagados com sucesso!')
        else:
            print('Opção inválida!')


    elif opcao == 5:
        if len(dados) == 0:
            print('Não existem ocorrências a serem exibidas!')
        elif len(dados) >= 1:
            tipo = int(input('Que tipo de ocorrência deseja exibir? \n1)Reclamação \n2)Elogio \nDigite: '))
            if tipo == 1:
                if len(reclamacao2) == 0:
                    print('Não existem reclamações registradas!')
                elif len(reclamacao2) >= 1:
                    for i in range(len(reclamacao2)):
                        print(str(i + 1) + 'º reclamação', reclamacao2[i])
                    valor = int(input('Informe o ID de sua ocorrência: '))
                    if valor > len(reclamacao2) or valor <0:
                        print('Opção inválida!')
                    else:    
                        print('A ocorrência é:', reclamacao2[valor - 1])
            elif tipo == 2:
                if len(elogio2) == 0:
                    print('Não existem elogios registrados')
                else:
                    for i in range(len(elogio2)):
                        print(str(i + 1) + 'º elogio', elogio2[i])
                    valor = int(input('Informe o ID de sua ocorrência: '))
                    if valor > len(elogio2) or valor <0:
                        print('Opção inválida!')
                    else:    
                        print('A ocorrência é:', dados[valor - 1])
            else:
                print('Opção inválida!')


    elif opcao == 6:
        if len(dados) == 0:
            print('Não existem ocorrências registradas!')
        elif len(dados) >= 1:
            tipo = int(input('O que deseja Editar? \n1)Reclamação \n2)Elogio \nDigite: '))
            if tipo == 1:
                if len(reclamacao2) == 0:
                    print('Não existem reclamações registradas!')
                else:
                    for i in range(len(reclamacao2)):
                        print(str(i + 1)+ 'º reclamação', reclamacao2[i])
                    valor = int(input('Informe o ID da reclamação que deseja editar: '))
                    if valor > 0 and valor <= len(reclamacao2):
                        nova_reclamacao = input('Digite a nova descrição da reclamação: ')
                        reclamacao2[valor - 1] = nova_reclamacao
                        print('Reclamação editada com sucesso!')
                    else:
                        print('ID de reclamação inválido!')
            if tipo == 2:
                if len(elogio2) == 0:
                    print('Não existem elogios registrados!')
                else:
                    for i in range(len(elogio2)):
                        print(str(i + 1)+ 'º elogio', elogio2[i])
                    valor = int(input('Informe o ID do elogio que deseja editar: '))
                    if valor > 0 and valor <= len(elogio2):
                        novo_elogio = input('Digite a nova descrição do elogio: ')
                        elogio2[valor - 1] = novo_elogio
                        print('Elogio editado com sucesso!')
                    else:
                        print('ID de elogio inválido!')
        else:
            print('Opção inválida!')

    elif opcao == 7:
        print('Obrigado por utilizar nosso sistema!')
    else:
        print('Erro: Operação Inválida!')

