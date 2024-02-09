#--------------------------------QUESTÃO 4--------------------------------

#---------- Início das Variáveis Globais ----------
lista_funcionario = []
#Define a lista onde ficarão os funcinárixs cadastradxs.
id_funcionario = 0
#Define a variável id_funcionario, a qual receberá o id de cada funcionário, porém, ela dependerá da sequência de cadastro.
#------------ Fim das Variáveis Globais -----------

#Início função cadastrar_funcionario
def cadastrar_funcionario(id):
    print('----------------------------- MENU CADASTRAR FUNIONÁRIX -----------------------------')
    print('ID Funcionárix: {}'.format(id))
    nome = input('Por favor entre com o NOME do funcionárix: ')
    setor = input('Por favor entre com o SETOR do funcionárix: ')
    salario = int(input('Por favor entre com o SALÁRIO do funcionárix R$: '))
    #Define as variáveis id, nome, setor e salário e solicita essas informações ao usuário.
    dicionario_funcionario = {'id'      : id,
                              'Nome'    : nome,
                              'Setor'   : setor,
                              'Salário' : salario}
    #Define o dicionario_funcionario que receberá as chaves e valores utilizadas na consulta dos funcionárixs.
    lista_funcionario.append(dicionario_funcionario.copy())
    #Cria uma cópia do dicionário.
#Fim função cadastrar_funcionario

#Início função consultar_funcionario
def consultar_funcionario():
    print('----------------------------- MENU CONSULTAR FUNIONÁRIX -----------------------------')
    while True:
        menu_consultar = input('Escolha a opção desejada: \n' +
                               '1-Consultar TODOS os funcionárixs \n' +
                               '2-Consultar funcionárix por ID \n' +
                               '3-Consultar funcionárix por SETOR \n' +
                               '4-Retornar\n' +
                               '>> ')
        #Solicita ao usuário que escolha como deseja consultar o funcionárix, se ele que todos, por ID ou Setor.
        if menu_consultar == '1':
            print('Você escolheu a opção Consultar TODOS os funcionárixs:')
            for funcionario in lista_funcionario: #funcionario vai varrer toda a lista_funcionario
                print('-' * 85) #Imprime na tela 85 vezes o caracter '-'.
                for key, value in funcionario.items():
                    print('{}: {}' .format(key, value)) #Varrer todos os conjuntos chave e valor do dicionario funcionario.
                print('-' * 85) #Imprime na tela 85 vezes o caracter '-'.
        #Esse if consulta a lista de todos os funcionárixs.
        elif menu_consultar == '2':
            print('Você escolheu a opção Consultar funcionárix por ID:')
            valor_desejado = int(input('Digite o ID do funcionárix: '))
            #Solicita ao usuário o ID do funcionárix.
            for funcionario in lista_funcionario:
                if funcionario['id'] == valor_desejado:
                    #O valor do campo ID desse dicionário deve ser igual ao valor_desejado para retornar na consulta.
                    print('-' * 85)#Imprime na tela 85 vezes o caracter '-'.
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))  # Varrer todos os conjuntos chave e valor do dicionario funcionario.
                    print('-' * 85)#Imprime na tela 85 vezes o caracter '-'.
        #Esse elif consulta o funcionárix pelo ID.
        elif menu_consultar == '3':
            print('Você escolheu a opção Consultar funcionárix por SETOR:')
            #Solicita ao usuário o SETOR do funcionárix.
            valor_desejado = input('Digite o SETOR do(s) funcionárix(s): ')
            for funcionario in lista_funcionario:
                if funcionario['Setor'] == valor_desejado:
                    #O valor do campo SETOR desse dicionário deve ser igual ao valor_desejado para retornar na consulta.
                    print('-' * 85)#Imprime na tela 85 vezes o caracter '-'.
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))#Varrer todos os conjuntos chave e valor do dicionario funcionario.
                    print('-' * 85)#Imprime na tela 85 vezes o caracter '-'.
        #Esse elif consulta o funcionárix pelo SETOR.
        elif menu_consultar == '4':
            return #Sai da função consultar_produto e retorna para o menu principal
        else:
            print('Opção inválida, tente novamente!')
            continue
        #Caso o usuário solicite a opção errada, imprime uma mensagem de erro na tela e retorna a pergunta inicial.

#Fim função consultar_funcionario

#Início função remover_funcionario
def remover_funcionario():
    print('------------------------------ MENU REMOVER FUNIONÁRIX ------------------------------')
    valor_desejado = int(input('Digite o ID do funcionárix a ser removido: '))
    for funcionario in lista_funcionario:
        if funcionario['id'] == valor_desejado:
            lista_funcionario.remove(funcionario)
            print('Funcionárix removido com sucesso!')
    #Essa função remove o funcionárix pelo ID.
#Fim função remover_funcionario

#Início Menu Principal

print('       Bem-vindx ao Controle de Funcionárixs da Jenyffer Laura Prochno Pereira')
#Imprime na tela a saudação da empresa e o nome da proprietária.

while True:
    print('*' * 85)#Imprime na tela 85 vezes o caracter '*'.
    print('----------------------------------- MENU PRINCIPAL ----------------------------------')
    menu_principal = input('Escolha a opção desejada: \n' +
                           '1-Cadastrar funcionárix \n' +
                           '2-Consultar funcionárix \n' +
                           '3-Remover funcionárix \n' +
                           '4-Sair \n' +
                           '>> ')
    #Solicita ao usuário que escolha o que deseja que o programa faça, entre cadastrar, consultar ou remover um funcionárix.
    if menu_principal == '1':
        id_funcionario = id_funcionario + 1 #Cria em sequência o ID do funcionárix.
        cadastrar_funcionario(id_funcionario)
    elif menu_principal == '2':
        consultar_funcionario() #Chama a função consultar_funcionario()
    elif menu_principal == '3':
        remover_funcionario() #Chama a função remover_funcionario()
    elif menu_principal == '4':
        break
        #Caso o usuário solicite a opção 4 encerra o laço principal e o programa finaliza.
    else:
        print('Opção inválida, tente novamente!')
        continue
        #Caso o usuário solicite a opção errada, imprime uma mensagem de erro na tela e retorna a pergunta inicial.
#Fim Menu Principal

