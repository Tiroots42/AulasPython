nome = 'Tiago'
idade  = str(33)
print ('Meu nome é ' + nome + ' e tenho ' + idade + ' anos de idade')

nome = 'tiago'
sobrenome = 'ribeiro'
profissao = 'DEV'
texto = f'O {nome} {sobrenome} é um ótimo {profissao}'
print(texto)

nome = input('Qual o seu nome? ')
print ('O nome digitado é '  + nome + '.')

ano_nascimento = input('Em que ano voce nasceu?')
idade = 2021 - int(ano_nascimento)
print (idade)

mensagem = 'Eu adoro comida Caseira' 
print (mensagem.upper()) #DEIXA LETRAS TUDO EM MAIUSCULAS

mensagem = 'eu adoro comida Caseira' 
print (mensagem.capitalize()) #DEIXA A PRIMEIRA LETRA MAIUSCULA

mensagem = 'eu adoro comida Caseira' 
print (mensagem.find('c')) #PROCURA LETRA OU PALAVRA NA POSIÇÃO DO INDEX (0123456789...)

mensagem = 'eu adoro comida Caseira' 
print (mensagem.replace('a', 'e')) #ALTERA LETRAS 'A' PELA 'E'

mensagem = 'eu adoro comida Caseira' 
print (mensagem.replace('Caseira', 'feito em casa')) #ALTERA PALAVRAS

mensagem = '     eu adoro comida Caseira' 
print (mensagem.strip()) #REMOVE ESPAÇOS ANTES DO PRIMEIRO CARACTERE

numero = 50
chute = int(input('Digite um numero: '))
if chute == numero:
    print('Você acertou!')
else: 
    print('Você errou!')    

nome = input('Digite um nome: ')
if nome == 'Tiago':
    print('Você acertou!')
else:
    print('Você errou')

data_atual = int(input('Digite a data atual: '))
ano_nascimento = int(input('Digite o ano nascimento: '))
idade = data_atual - ano_nascimento
print(f'Sua idade atual é {idade} anos')

numero_magigo = 10
numero_escolhiido = int(input('Digite um número: '))
if(numero_escolhiido == numero_magigo):
    print('Você acertou')
elif(numero_escolhiido > numero_magigo):
    print('Número acima')
elif(numero_escolhiido < numero_magigo):
    print('Número abaixo')        

numero_sorte = 10
numero_usuario = int(input('Digite um numero: '))
certo = numero_usuario == numero_sorte
acima = numero_usuario > numero_sorte
abaixo = numero_usuario < numero_sorte
if (certo):
    print('Você acertou')
elif(acima):
    print('Está acima')
elif(abaixo):
    print('Está abaixo')

renda_acima_5mil = True
nome_limpo = True
if renda_acima_5mil and nome_limpo:
    print("Aprovado")
else:
    print("Reprovado")

renda_acima_5mil = True
nome_limpo = True
if renda_acima_5mil or nome_limpo:
    print("Aprovado")
else:
    print("Reprovado")

#Mecardo-finaceiro Dividendos
valor_ativo = float(input('Digite valor do ativo: '))
quantidade = int(input("Digite quantidade de ativos: "))
valor_dividendo = float(input("Digite o valor do dividendo: "))
total = valor_ativo * quantidade
total_dividendo = valor_dividendo * quantidade
print(f'O Valor de "{quantidade} Ações" é R${total:,.2f} e o Valor de Dividendos á receber é de ${total_dividendo:,.2f} por mês')

valor = 19
if 20 <= valor <= 40:
    print ('Produto aceito')
else:
    print('Produto não aceito')

for numero in range(1, 20, 2):
    print(numero)

palavra = 'Google'
for letra in palavra:
    print(letra)

palavra = 'Google'
for letra in palavra:
    print(f'{letra} esta dentro da palavra Google')

palavra = 'Tiago'
for letra in palavra:
    print(f'{letra} está dentro da palavra {palavra}')

