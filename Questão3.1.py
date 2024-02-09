#função metragem da limpeza

def metragem_limpeza():

   metragem = input("Qual a metragem da porção a ser limpa? ")

   try:

       metragem = int(metragem)

       if not 30 <= metragem < 700:

           metragem_limpeza()

       else:

           metragem = int(metragem)

           if 30 <= metragem < 300:

               valor_metragem = 60 + 0.3*metragem

           else:

               valor_metragem = 120 + 0.5*metragem

           return valor_metragem

   except:

       metragem_limpeza()

#função tipo de limpeza

def tipo_limpeza():

   tipo = input ("Qual o tipo de limpeza será feita? Digite B para básica e C para completa. ")

   if tipo == "B":

       multiplicador = 1.00

   elif tipo == "C":

       multiplicador = 1.30

   else:

       tipo_limpeza()

   return multiplicador

#função adicional da limpeza

def adicional_limpeza():

   aux = 0

   print (tipos_adicional)

   while True:



       adicional = input ("Digite o número do adicional que deseja. ")

       if int(adicional) == 0:

           break

       elif int(adicional) in tipos_adicional:

           aux = aux + valor_adicional[int(adicional)]

       else:

           continue

   return aux

#tabela adicionais

tipos_adicional = {0: "Sem adicionais",

                  1: "Passar 10 peças de roupa",

                  2: "Limpeza de Forno/Microondas",

                  3: "Limpeza de Freezer/Geladeira"}

valor_adicional = [0, 10.00, 12.00, 20.00]

# programa

valor = metragem_limpeza()

tipo_limpeza = tipo_limpeza()

adicionais = adicional_limpeza()

total = (valor*tipo_limpeza) + adicionais

print(f"R$ {total:,.2f}")

#Observe que o .2f permite que o programa imprima um valor com duas casas decimais, referente aos centavos.