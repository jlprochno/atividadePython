# --------------------------------QUESTÃO 3--------------------------------

# Início da função metragem_limpeza.
def metragem_limpeza():
    print('----------------------------- Menu 1 de 3 - Metragem Limpeza ----------------------------- ')
    # Imprime na tela do usuário uma divisão entre os menus 1, 2 e 3.
    while True:
        try:
            metragem = int(input("Entre com a metragem da casa: "))
            if (metragem >= 30) and (metragem < 300):
                print('Será necessário um colaborador para a limpeza!')
                return 60 + 0.3 * metragem  # Retorna o valor da metragem caso ela seja entre 30 a 300 metros.
            elif (metragem > 299) and (metragem < 700):
                print('Serão necessários dois colaboradores para a limpeza!')
                return 120 + 0.5 * metragem  # Retorna o valor da metragem caso ela seja entre 301 a 700 metros.
            else:
                print("!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!")
                # Imprime na tela uma mensagem de erro caro o usuário digite a metragem abaixo ou acima do esperado.
                continue  # Retorna para a pergunta inicial caso o usuário digite a opção errada.
        except ValueError:  # Caso o usuário não digite um número inteiro o programa solicitará que o usuário corrija sua escolha.
            print('Por gentileza, adicione um número inteiro!')


# Fim da função metragem_limpeza.

# Início da função tipo_limpeza.
def tipo_limpeza():
    print('----------------------------- Menu 2 de 3 - Tipo Limpeza --------------------------------- ')
    # Imprime na tela do usuário uma divisão entre os menus 1, 2 e 3.
    while True:
        tipoL = input('Entre com o tipo da limpeza: \n' +
                      'B – Básica - Indicada para sujeiras semanais ou quinzenais. \n' +
                      'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras. \n' +
                      '>> ')
        tipoL = tipoL.upper()  # Solução para que o usuário possa digitar maiúsculo ou minúsculo.
        tipoL = tipoL.strip()  # Solução para que o usuário possa digitar espaços.
        if tipoL == 'B':
            print('Você selecionou a limpeza BÁSICA')
            return 1.00
        # Retorna o valor de 1.00 que futuramente será multiplicado pelo valor da metragem. Caso o usuário seleciona essa opção ao pedido.
        elif tipoL == 'C':
            print('Você selecionou a limpeza COMPLETA')
            return 1.30
        # Retorna o valor de 1.30 que futuramente será multiplicado pelo valor da metragem. Caso o usuário seleciona essa opção ao pedido.
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue  # Retorna para o início do laço (Retorna para a pergunta).


# Fim da função tipo_limpeza.

# Início da função adicional_limpeza.
def adicional_limpeza():
    print('----------------------------- Menu 3 de 3 - Adicional Limpeza ---------------------------- ')
    # Imprime na tela do usuário uma divisão entre os menus 1, 2 e 3.
    acumulador = 0
    # Define a variável acumulador, a qual receberá o valor do adicional, porém, ela dependerá do pedido do usuário.
    while True:
        adicionais = input('Deseja mais algum adicional? \n' +
                           '0- Não desejo mais nada (encerrar) \n' +
                           '1- Passar 10 peças de roupas - R$ 10.00 \n' +
                           '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                           '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                           '>> ')
        # Imprime na tela as opções de adicionais e solicita ao usuário a fazer a escolha do mesmo.
        if adicionais == '0':
            return acumulador
            # Retorna o valor total do serviço sem adicionais.
        elif adicionais == '1':
            acumulador = acumulador + 10
            # Soma R$10,00 ao total do valor do pedido já realizado. Caso o usuário seleciona esse adicional ao pedido.
            continue
        elif adicionais == '2':
            acumulador = acumulador + 12
            # Soma R$12,00 ao total do valor do pedido já realizado. Caso o usuário seleciona esse adicional ao pedido.
            continue
        elif adicionais == '3':
            acumulador = acumulador + 20
            # Soma R$20,00 ao total do valor do pedido já realizado. Caso o usuário seleciona esse adicional ao pedido.
            continue
        else:
            print('!!!!!!! Adicional inválido !!!!!!!')
            continue
            # Caso o usuário solicite a opção errada, imprime uma mensagem de erro na tela e retorna a pergunta inicial.


# Fim da função adicional_limpeza.

print('      Bem-vindx ao Programa de Serviços de Limpeza da Jenyffer Laura Prochno Pereira')
# Imprime na tela a saudação da empresa e o nome da proprietária.
print('******************************************************************************************')
metragem = metragem_limpeza()  # Chama a função metragem_limpeza()
tipoL = tipo_limpeza()  # Chama a função tipo_limpeza()
adicionais = adicional_limpeza()  # Chama a função adicional_limpeza()
total = (metragem * tipoL) + adicionais  # Multiplica a metragem, pelo tipo de limpeza escolhido e soma ao adicional.
print('******************************************************************************************')
print('TOTAL R$: {:.2f} (Metragem R$: {:.2f} * Tipo Limpeza R$: {:.2f} + Adicional R$: {:.2f})'.format(total, metragem,
                                                                                                       tipoL,
                                                                                                       adicionais))
print('******************************************************************************************')
# Imprime na tela o valor total do serviço de limpeza e a descrição de cada item.
