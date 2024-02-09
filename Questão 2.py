#--------------------------------QUESTÃO 2--------------------------------

print ('Seja bem-vindx a Sorveteria da Jenyffer Laura Prochno Pereira')
#Imprime na tela a saudação da Sorveteria e o nome da proprietária.

print('______________________________________________Cardápio_________________________________________')
print('| Código |       Descrição      | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')
#Imprime o cardápio na tela do usuário.

acumulador = 0
#Define a variável acumulador, a qual receberá o valor do sorvete, porém, ela dependerá do pedido do usuário.

while True:
    tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ') #Define a variável tamanho e solicita ao usuário.
    tamanho = tamanho.upper() #Solução para que o usuário possa digitar maiúsculo ou minúsculo.

    codigo = input('Entre com o Código do sabor desejado (TR/ES/PR): ')#Define a variável codigo e solicita ao usuário.
    codigo = codigo.upper() #Solução para que o usuário possa digitar maiúsculo ou minúsculo.

    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('!!!!!!! TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!')
        continue
    elif codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('!!!!!!! TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!!!')
        continue
    #Caso o usuário digite o tamanho ou codigo inválido ele recebe uma mensagem de erro e o programa retorna ao início.

    if codigo == 'TR' and tamanho == 'P':
        print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 6
        #Soma R$6,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'TR' and tamanho == 'M':
        print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 10
        #Soma R$10,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'TR' and tamanho == 'G':
        print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 18
        #Soma R$18,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'ES' and tamanho == 'P':
        print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 7
        #Soma R$7,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'ES' and tamanho == 'M':
        print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 12
        #Soma R$12,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'ES' and tamanho == 'G':
        print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 21
        #Soma R$21,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'PR' and tamanho == 'P':
        print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 8
        #Soma R$8,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'PR' and tamanho == 'M':
        print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 14
        #Soma R$14,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    elif codigo == 'PR' and tamanho == 'G':
        print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
        print('-----------------------------------------------------')
        acumulador = acumulador + 24
        #Soma R$24,00 ao total do valor do pedido já realizado. Caso o usuário adicione esse sorvete ao pedido.

    pedir_mais = input('Deseja pedir mais alguma coisa? (S/N): ')#Define a pedir_mais e questiona o usuário.
    pedir_mais = pedir_mais.upper() #Solução para que o usuário possa digitar maiúsculo ou minúsculo.
    if pedir_mais == 'S': #Caso o usuário queira acrescentar mais sorvetes ao seu pedido, retorna ao início.
        continue
    else: #Caso contrário, é impresso na tela o valor a pagar.
        print('O total a ser pago é de:R$ {:.2f}' . format(acumulador))
        break #Finaliza o programa, para que não fique em loop eterno.