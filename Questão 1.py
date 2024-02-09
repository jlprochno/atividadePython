#--------------------------------QUESTÃO 1--------------------------------

print('Seja Bem-vindx a loja da Jenyffer Laura Prochno Pereira')
#Imprime na tela a saudação da loja e o nome da proprietária.

v_unitario = float(input('Entre com o valor do produto: '))
#Define a variável v_unitario para o valor do produto e solicita ao usuário que entre com o valor do produto.

quantidade = int(input('Entre com o valor da quantidade: '))
#Define a variável quantidade para o valor da quantidade e solicita ao usuário que entre com o valor da quantidade.

valor_frete = 0
# A variável valor_frete receberá o valor do frete, porém, ela dependerá da quantidade de produtos inseridos.

if 0 <= quantidade < 11:
   valor_frete = 30
elif 11 <= quantidade < 101:
   valor_frete = 60
elif 101 <= quantidade < 1001:
   valor_frete = 120
else:
   valor_frete = 240
#Estrutura condicional baseada na tabela do enunciado da Questão 1


valor_sem_frete = float(v_unitario * quantidade)
#Define a variável valor_sem_frete a qual recebe a multiplicação da v_unitário pela quantidade.

valor_com_frete = float(valor_sem_frete + valor_frete)
#Define a variável valor_com_frete a qual recebe a soma da variável valor_com_frete mais a variável valor_frete.

print('O valor sem frete foi: R$ {:.2f}'.format(valor_sem_frete))
#Imprime o valor da compra sem frete, formatando o valor com duas casas decimais depois do ponto.

print('O valor com frete foi: R$ {:.2f} '.format(valor_com_frete) + '(frete de R$ {:.2f})'.format(valor_frete))
#Imprime o valor da compra com frete, formatando o valor com duas casas decimais depois do ponto.

