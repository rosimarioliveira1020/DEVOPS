# Declara a lista 
lista = []

# Menu Principal
opcao = 2
while opcao != 1:
    print ("Bem-vindo ao menu de Operações! Digite uma opção desejada e aperte o enter no final,")
    opcao = int(input(" 1. Gerenciar Estudantes\n 2. Gerenciar Disciplinas\n 3. Gerenciar Professores\n 4. Gerenciar Turmas\n 5. Gerenciar Matriculas\n 6. Sair\n\n Informe a modalidade desejada: "))
    if opcao == 1:
        print ("\nGerenciar estudantes. Seja bem-vindo\n")
    elif opcao == 2:
        print ("\nGerenciar disciplinas em desenvolvimento\n")
    elif opcao == 3:
        print ("\nGerenciar professores em desenvolvimento\n")
    elif opcao == 4:
        print ("\nGerenciar turmas em desenvolvimento\n")
    elif opcao == 5:
        print ("\nGerenciar matriculas em desenvolvimento\n")
    elif opcao == 6:
        print ("\nSair em desenvolvimento\n")
    else:
        input("\nOpção incorreta!\n")

# Menu Operacional

acao = 1
while acao != 5:
    print ("Bem-vindo ao menu de Operações! Digite uma opção desejada e aperte o enter no final:\n\n")
    acao = int(input(" 1. Incluir\n 2. Listar_registro\n 3. Atualizar registro\n 4. Excluir registro\n 5. Finalizar programa\n\n Informe a modalidade desejada: "))
    nome = ''
    if acao == 1:
        print ("\n Incluir\n")

        # Pergunta o nome
        nome = input ("Digite o nome do estudante: ")
        
        # Adiciona o tempo na lista
        lista.append(nome)
        input("\nPressione enter para continuar\n")

    elif acao == 2:
        print ("\n Listar_registro\n")
        if lista == []:
            print ("Não há estudantes cadastrados.")
        else:
            c = 1
            for item in lista :
                print("NOME {}: {} ".format (c, item))
                c = c + 1
            

    elif acao == 3:
        print ("\n Atualizar registro\n")
        print ("\n Excluir em desenvolvimento\n")
        input()

    elif acao == 4:
        print ("\n Ecluir registro\n")
        print ("\n Excluir em desenvolvimento\n")
        input()

    elif acao == 5:
        print ("\n Finalizar programa\n")
        continue

