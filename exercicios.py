"""km=float(input('o numero da tabuada'))
d=int(input('o numero '))
a=(km * 0.15) + (d * 60)
print('voce tera que pagar {:.2f}'.format(a))
"""
"""importando bibliotecas em python
import math 
ceil -  arredondamento para cima, 
floor para baixo. 
trunc - tira virgula , 
pow - potência
sqrt -  raíz quadrada , factorial"""
# ====================
"""import math
m=float(input('o numero '))
n=math.trunc(m)
print('o numero é {}'.format(n)) """
# ==================
"""import random
n1=str(input("digite um nome "))
n2=str(input("digite um nome "))
n3=str(input("digite um nome "))
n4=str(input("digite um nome "))
lista = [n1,n2,n3,n4]
escolhido=random.choice(lista)
emb=random.shuffle(lista)
print("o escolhido foi {} e o embaralhamento da lista é {}".format(escolhido,lista))
"""
""" Análise com len(), count(), find(), 
transformações com replace(), 
upper(), lower(), capitalize(), 
title(), strip(), junção com join().
"""
"""Exercícios envolvendo strings 
1- nome=str(input("digite seu nome")).strip() #tira os espaços
    print("analisando seu nome")
    print("analisando seu nome é em maiusculo {}".format(nome.upper()))
    print("analisando seu nome é em minusculo {}".format(nome.upper())))
    print("analisando seu nome tem {}".format(len(nome) - nome.count(' ')) #nome count, conta espaços para subtrair
    separa= nome.split()
    print("analisando seu nome primeiro nome tem {} letras".format(nome.find(' '))
     
2- Exercício  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome=str(input("digite seu nome completo"))
print('seu primeiro nome é {}'.format('silva' in nome.lower)))
3- Exercício Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
nome=str(input("digite uma palavra contendo a letra a")).upper()
print('a palavra a apareceu {} vezes na frase'.format(frase.count('A')))
print('a primeira palavra a apareceu {} vezes e apareceu na posição {} .format(nome.find('A')+1))
print('a última palavra a apareceu {} vezes e apareceu na posição {} .format(nome.rfind('A')+1))
4- Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro 
e o último nome separadamente.
nome=str(input("digite uma palavra contendo a letra a"))
print("analisando seu nome primeiro nome é {} ".format(nome[0]))
print("analisando seu nome último nome é {} letras".format(nome[len(nome]-1))
====================================================
1 -Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
    from random import randint
computador=randint(0,5)
print('===*==='*20)
print('advinhe qual numero o computador advinhou')
print('===*==='*20)
n=int(input('digite o numero'))
if n<0:
    n = int(input('digite um numero inteiro entre 0 e 5 :'))
elif n==computador:
    print("voce acertou")
elif n!=computador:
    print("voce errou")
 
 
2 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d=float(input('digite a distancia da viagem em Km'))
if d<=200:
    p=d*0.50
elif d>200:
    p=d*0.45
print('voce tera que pagar {}'.format(p))

3 - d=float(input('digite a distancia da viagem em Km'))
if d<=200:
    p=d*0.50
elif d>200:
    p=d*0.45
print('voce tera que pagar {}'.format(p))

CONDICIONAIS -
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
v=float(input('digite o valor da casa'))
c=float(input('digite o seu salário'))
d=int(input('digite quantos anos para pagar a casa'))
p=v/(d*12)
t=(c*0.30)
if p >t:
    print("seu empréstimo foi negado")
else:
    print('seu empréstimo foi aceito')


Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
   mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

v=int(input('digite o valor do inteiro'))
c=int(input('digite o valor do segundo inteiro'))
if v>c:
    print("o primeiro número {} é maior que o segundo {}".format(v,c))
elif c>v:
    print("o segundo número {} é maior que o primeiro {}".format(c,v))
else:
    print('Não existe valor maior, os dois são iguais')

Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

p=150
print('Selecione a forma de pagamento 10% de desconto')
print('Digite 1 para valor à vista com 5% de desconto')
print('Digite 2 para à vista no cartão')
print('Digite 3 para parcelar em 2x com preço formal ')
print('Digite 4 para parcelar em 3x ou mais com 20% de juros')
v=int(input('digite a forma de pagamento : '))
if v==1:
    c=((p*10)/100)-p
    print("vocÊ vai pagar {} com o desconto".format(c))
elif v==2:
    c = (p * 0.05) - p
    print("vocÊ vai pagar {} com o desconto".format(c))
elif v==3:
    print("vocÊ vai pagar {}".format(p))
elif v==4:
    c = (p * 0.20) + p
    print("vocÊ vai pagar {} com juros".format(c))
else:
    print('digite um valor de 1 a 4')
    v=int(input('digite a forma de pagamento : '))
    
    print ('[1]- pedra')
print ('[2] - papel')
print ('[3] - tesoura')
from random import randint
jogador = int(input ('escolha  '))
while True:
    computador = randint(1,3)
    while jogador > 3:
        print ('escolha uma opção entre 1 e 3')
        jogador = int(input ('escolha  '))
    while jogador < 1:
        print ('escolha uma opção entre 1 e 3')
        jogador = int(input ('escolha  '))
    if jogador == 1:
        print ('voce escolheu PEDRA')
    elif jogador == 2:
         print ('voce escolheu PAPEL')
    elif jogador == 3:
            print ('voce escolheu TESOURA')
    if computador == 1:
     print ('o comp escolheu PEDRA')
    elif computador == 2:
     print ('o comp escolheu PAPEL')
    elif computador == 3:
     print ('o comp escolheu TESOURA')

    if jogador == computador:
     print ('empate')
    else:
     if jogador == 1:
         if computador == 2:
            print ('comp venceu')
         elif computador == 3:
            print ('voce venceu')
     if jogador == 2:
         if computador == 1:
            print ('voce venceu')
         elif computador == 3:
            print ('comp venceu')
     if jogador == 3:
         if computador == 1:
            print ('comp venceu')
         elif computador == 2:
             print ('voce venceu')
    print ('[1]- pedra')
    print ('[2] - papel')
    print ('[3] - tesoura')
    jogador = int(input ('escolha  '))
    
ESTRUTURA DE REPETIÇÃO

Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de 
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


Exercício Python 47: Crie um programa que mostre na tela todos os números 
pares que estão no intervalo entre 1 e 50

print('===============contagem===============')
for i in range (1,51):
    if i%2==0:
        print('par = {}'.format(i))
    else:
        print('ímpar = {}'.format(i))
print('===============BOOOOOOOOOOOOOOM===============')

Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for i in range (1,501):
    if i%3==0:
        cont = cont + 1
        soma = soma + i
print('a soma é {} e tem {} numeros'.format(soma,cont))

Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.

cont = 0
soma = 0
p=int(input('digite o primeiro termo da p.a'))
r=int(input('digite a razaão da p.a'))
for i in range (10):
    soma = soma + r
    print('{} , '.format(soma),end='->')

Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
p=int(input('digite um numero'))
for i in range (1, p+1):
    if p % i == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{}  '.format(i),end='')
print('o  numero {} foi divisivel {} vezes '.format(i,tot),end='')
if tot == 2:
    print ('é primo')
else:
    print('não é primo')
 Exercício Python 53: Crie um programa que leia uma frase qualquer e 
 diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
 
 frase=str(input('digite uma frase')).strip().upper()
palavras=frase.split()
print(palavras)
junto= ''.join(palavras)
print(junto)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(junto,inverso)
if inverso == junto:
    print('é palíndromo')
else:
    print('não é palíndromo')

frase=str(input('digite uma frase')).strip().upper()
palavras=frase.split()
print(palavras)
junto= ''.join(palavras)
print(junto)
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(junto,inverso)
if inverso == junto:
    print('é palíndromo')
else:
    print('não é palíndromo')


REPETIÇÃO WHILE

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

print("programa para ver seu sexo, digite 'M' para masculino e 'F' para feminino")
n=str(input('digite seu sexo : ')).strip().upper()
while n not in 'mMfF':
    n=str(input('digite seu sexo novamente : ')).strip().upper()
print(n)

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer.

from random import randint
computador=randint(0,10)
cont=0
print("sou seu computador,vou pensar em um numero de 0 a 10")
print("sera que voce consegue acertar?")
acertou=False
while not acertou:
    n=int(input('digite o numero que o pc advinhou :'))
    cont = cont + 1
    if n == computador :
        acertou = True
    else:
        if n < computador:
            print('digite um valor maior')
        elif n> computador:
            print("digite um valor menor")
print("você acertou e teve {} palpites".format(cont))

Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
Fn = Fn - 1 + Fn - 2
t1=0
t2=1
cont=3
n=int(input("digite o numero de inteiros para a sequencia de fibonacci"))
print('{} -> {} '.format(t1,t2), end='')
while cont <= n:
    t3=t1+t2
    print('->{} '.format(t3), end='')
    t1=t2
    t2=t3
    cont = cont + 1

 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 
 usuário digitar o valor 999, que é a condição de parada. No final, 
 mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
 
 cont = 0
soma = 0
n= 0
n1= 0
n = int(input('digite o número que seja maior que zero e menor que 1000'))
while n != 999:
    soma += n
    cont = cont + 1
    n = int(input('digite o número que seja maior que zero e menor que 1000'))
print('acabou , vc digitou {} numeros e a soma entre eles é {}'.format(cont,soma))

Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = 0
soma = 0
n= 0
maior = menor =0
r='s'
while r in 'sS':
    n = int(input('digite o número inteiro  :'))
    soma += n
    cont = cont + 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('deseja continuar ? [S/N]')).upper().strip()[0]
media = soma/cont
print('acabou , vc digitou {} numeros e a soma entre eles é {} e a media é {} '.format(cont,soma,media))
print('o maior numero digitado foi {} e o menor foi {}'.format(maior,menor))


Como interromper whiles

usando break

Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

r='s'
cont =c=c1=c2=c3= 0
contH=0
while True:
    idade=int(input('digite sua idade :  '))
    sexo=str(input('digite seu sexo :  ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo :  ')).upper().strip()[0]
    if idade >=18:
        c +=1
    if sexo =='M':
        contH +=1
    elif sexo == 'F' and idade < 20:
        c1 +=1
    cont += 1
    r=str(input('deseja continuar ? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('deseja continuar ? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print('foram registradas {} pessoas, {} pessoas tem mais de 18 anos e existem {} mulheres com menos de 20 anos'.format(cont,c,c1))
print(f'existem {contH} homens')


Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

maior=menor=0
c=c1=c2=c3=0
total=0
while True:
    nome=str(input('digite o nome do produto :  '))
    preço=float(input('digite o preço do produto :  '))
    c3+=1
    if preço > 1000:
        c += 1
    if c3==1:
            menor = preço
    total += preço
    r=str(input('deseja continuar ? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('deseja continuar ? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'o total que você gastou foi {total} e {c} produtos são maiores que 1000')
print(f'o mais barato é {menor}')

Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor=int(input('digite o valor inteiro a ser sacado'))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total -=ced
        totced +=1
    else:
        if totced > 0:
            print(f'existem total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced=0
        if total == 0:
            break
            
====================================TUPLAS==================================
variáveis compostas
não podem ser alteradas
são como listas
lanche = ('1hamburguer','suco','pizza','pudim')
print(lanche[1])
suco
print(lanche[-2])
pizza
print(lanche[1:3])
suco,pizza
print(lanche[2: ])
pizza,pudim
print(len(lanche))
4
for comida in lanche
    print(lanche)
-hamburguer
-suco
-pizza
-pudim
for contador in range(0,len(lanche)):
iria de 0 a 3
print(lanche(contador))
de 0 a 3, mas mostraria todos

for pos comida in enumerate(lanche)
mostra a posição e o dado
print(sorted(lanche))

a=(2,5,4)
b=(3,5,6,8)
c= a+b
print(c)
2,5,4,3,5,6,8
print(c.count(5))
2 vezes - conta quantas vezes apareceu-
print(c.index(5))
1 - posição e print(c.index(5,1)) a partir da posição 1

Exercício Python 72: Crie um programa que tenha uma 
dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num=('zero','um','dois''três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
     'catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('digite um número de zero a 20'))
    if   0<= n <=20:
        break
print(f"você digitou o número {num[n]}")

Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
 Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.

num=('corinthians','palmeiras','são paulo''santos','cruzeiro','chapecoense','vasco',
     'grêmio','internacional','atlético mineiro','barcelona','real madrid','liverpool','psg',
     'atlético de madrid','argentina','brasil','chelsea','tottenham','bayer','once caldas')



print(f'os 5 primeiros times são{num[0:5]}')
print(f'os 4 últimos times são{num[-4:]}')
print(f'times em ordem alfabética {sorted(num)}')
print(f"chapecoense está na posição {num.index('chapecoense')+1}")

Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar 
em uma tupla. Depois disso, mostre a listagem de números gerados e também indique
 o menor e o maior valor que estão na tupla.

from random import randint
n = (randint (1,10),randint (1,10),randint (1,10),randint (1,10),randint (1,10))
print(f'a lista dos números sorteados é {n}')
print(f'o maior numero sorteado foi {max(n)}  e o menor foi {min(n)}')

Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.



Exercício Python 076: Crie um programa que tenha uma tupla única com
 nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

n = ('lápis',1.75,'caderno',2.50,'neymar',250.00)
for pos in range(0,len(n)):
    if pos 2 % == 0:
        print(f'{n[pos]:.<30}')
    else:
        print(f'{n[pos]:.>30}')
        
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
(não usar acentos). Depois disso, você deve mostrar, 
para cada palavra, quais são as suas vogais.

n=('vaga','enemy','carl','stefany','amanda','pato','gato')
for i in n:
    print(f"\nna palavra {i} temos  ",end=' ')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            
=========================LISTAS=================
letras.append() --> adiciona na lista
letras.insert(0,'')-->insere na posição 0
del letras[3]--> elimina
letra.pop(3)--> elimina
letra.remove('escreve o valor da lista')
valores= list(range(4,11))
valores=[8,1,3,2)
valores.sort()
valores.sort(reverse=True)
len(valores)
valores=list()
for cont in range (0,5)
    valores.append(int(input('digite valores na lista'))
    
for c,v in enumerate(valores)
    print(f'na posicação {c} encontrei o valor {v}')
    
a=[1,2,3]
b=a
as duas listas são iguais,o python faz uma ligação entre elas,se modificar uma a outra7
tbm sera modificada
b=a[:]
cria uma cópia de a dentro de b e n existe ligação


Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum=[]
maior=0
menor=0
for c in range (0,5):
    listanum.append(int(input(f'digite valores na lista NA POSIÇÃO {c}  ')))
    if c==0:
        maior=menor=listanum[c]
    else:
        if listanum[c]>maior:
            maior=listanum[c]
        if listanum[c]<menor:
            menor=listanum[c]
print(f'voce digitou os valores {listanum}')
print(f'o maior foi {maior} e o menor foi {menor}')

Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

n=list()
while True:
    s=int(input(f'digite valores na lista   '))
    if s not in n:
        n.append(s)
    else:
        print('valor duplicado')
    r=str(input('deseja continuar ?[S/N]?  ')).upper().strip()[0]
    if r in 'N':
        break

n.sort()
print(f'voce digitou os valores {n}')

Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
 
 lista=[]
for i in range(0,5):
    n=int(input('digite um valor  :'))
    if i==0 or n> lista[len(lista)-1]:
        lista.append(n)
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1
print(f'os valores digitados foi {lista}')

Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                
  Depois disso, mostre:                                                                                
A) Quantos números foram digitados.  
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
 
n=[]
c=b=d=0
while True:
    n.append(int(input(f'digite valores na lista   ')))
    d += 1
    r = str(input('deseja continuar ?[S/N]?  ')).upper().strip()[0]
    if r in 'N':
        break

if 5 not in n:
    print(f'o valor 5 não foi digitado ou não está na lista')
else:
    print(f'o valor 5 foi digitado ou está na lista')
n.sort(reverse=True)
print(f'foram digitados {d} números e o a lista foi {n}')

Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.
 
 n=[]
p=[]
i=[]

while True:
    ('digite valores na lista')
    n.append(int(input(f'digite valores na lista   ')))
    r = str(input('deseja continuar ?[S/N]?  ')).upper().strip()[0]
    if r in 'N':
        break
for d,v in enumerate(n):
    if v %2==0:
        p.append(v)
    else:
        i.append(v)
print(f'lista geral {n} a lista par e ímpar {p} {i}')

Exercício Python 083: Crie um programa onde o 
usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
 deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
 
expr=str(input('digite valores na lista   '))
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha)==0:
    print('sua expressão esta valida')
else:
    print('sua expressão esta errada ')
    
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, 
                                     
guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

n=[]
c=0
maior=menor=0
princ=[]
while True:
    print('digite seu nome e seu peso')
    n.append(str(input(f'digite seu nome   ')))
    n.append(int(input(f'digite seu peso  ')))
    if len(princ)==0:
        maior=menor=n[1]
    else:
        if n[1] > maior:
            maior=n[1]
        elif n[1] < menor:
            menor=n[1]
    princ.append(n[:])
    n.clear()
    r = str(input('deseja continuar ?[S/N]?  ')).upper().strip()[0]
    c +=1
    if r in 'N':
        break
print(f'os dados foram {len(princ)}')
print(f'o maior peso é {maior}')
print(f'o menor peso é {menor}')

Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.
 
 n=[[],[]]
valor=0
par=impar=0
for c in range(1,8):
    print('digite 7 valores numéricos')
    valor=(int(input(f'digite :   ')))
    if valor%2==0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n.sort()
print(n)


Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
n=[[0,0,0],[0,0,0],[0,0,0]]
valor=0
par=impar=0
for linha in range(0,3):
    for coluna in range (0,3):
        n[linha][coluna] = int(input(f'digite um valor para [{linha},{coluna}]:  '))
print('-='*30)
for linha in range(0,3):
    for coluna in range (0,3):
        print(f'[{n[linha][coluna]:^5}]',end='')
    print()
    
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

n=[[0,0,0],[0,0,0],[0,0,0]]
valor=0
par=impar=spar=scol=slinha=maior=menor=0
for linha in range(0,3):
    for coluna in range (0,3):
        n[linha][coluna] = int(input(f'digite um valor para [{linha},{coluna}]:  '))
print('-='*30)
for linha in range(0,3):
    for coluna in range (0,3):
        print(f'[{n[linha][coluna]:^5}]',end='')
        if n[linha][coluna]%2==0:
            spar+=n[linha][coluna]
    print()
print(f'a soma dos valores pares são {spar}')
for linha in range(0,3):
    scol+=n[linha][2]
print(f'a soma dos valores da terceira coluna é {scol}')
for coluna in range (0,3):
    if coluna == 0:
        maior=n[1][coluna]
    elif n[1][coluna] > maior:
        maior = n[1][coluna]
    elif n[1][coluna] < menor:
        menor = n[1][coluna]
print(f'o maior valor da segunda linha é {maior} e o menor {menor}')


Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
num = randint(1,60)
lista =list()
jogos=list()
print('-'*30)
print('       MEGA SENA        ')
print('-'*30)
q = int(input('quantos jogos vocÊ quer fazer ?  '))
totaldejogos=1
d=0
while totaldejogos<=q:
    cont=0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    sorted(set(lista))
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totaldejogos+=1
print('-='*3,f'sorteando {q} jogos', '-='*3)
for indice,l in enumerate(jogos):
    print(f'jogo {indice+1}: {l}')
    sleep(2)
print('-='*5,f'BOA SORTE CACHORRO', '-='*5)

Exercício Python 089: Crie um programa que leia nome e duas notas de
 vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
 contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
 
n=list()
while True:
    print('digite seu nome e sua nota')
    nome=str(input(f'digite seu nome   '))
    nota1=float(input(f'digite sua primeira nota  '))
    nota2=float(input(f'digite sua segunda nota  '))
    media=(nota1+nota2)/2
    n.append([nome,[nota1,nota2],media])
    r = str(input('deseja continuar ?[S/N]?  ')).upper().strip()[0]
    if r in 'N':
        break
print('-='*30)
print('         BOLETIM        ')
print(f'{"n°":<4}{"NOME":<10}{"MEDIA":<8}')
print('-='*30)
for i,l in enumerate(n):
    print(f'{i+1:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    opc=int(input('mostrar as notas de qual aluno ? se não digite 999'))
    if opc==999:
        break
    print('-=' * 30)
    print('         FINALIZANDO      ')
    if opc <= len(n)-1:
        print(f'notas de {n[opc][0]} são {n[opc][1]}')
print('-='*30)
print('         VOLTE SEMPRE      ')

===============================DICIONARIOS==================================
 Os dicionários são variáveis compostas que permitem armazenar 
 vários valores em uma mesma estrutura, acessíveis por chaves literais.
 dicionarios=dict{}
 dados={'nome':'pedro','idade':25}
 print(dados['nome']) --> vai ser pedro
 ---- para adicionar algum dado é só fazer
 dados['sexo']='M'
 ----- para remover
 deldados['idade']
 =----
 filmes={'titulo':'star wars','ano':1977,'diretor':'jorge'}
 print(filmes.values())
 retorna os valores , star wars,1977 e jorge
 print(filmes.keys())
 retorna os dados, titulo,ano e diretor
 print(filmes.items())
 retorna os dois.
exemplo
for k,v in filme.items(): -- similar ao enumerate
    print(f'{k} é {v}
    
def elogio():
    print('\n Para a mulher mais linda do mundo...')
    print('\033[32m\n Minha heroína e razão do meu viver ! \033[33m\n Duas em uma mulher \033[36m\n Te amo para sempre\n')

def coracao():
    print(f'\033[47;31m   {"ooo ooo":^48}')
    print(f'  {"o   o   o":^49}')
    print(f'   {"o     o":^48}')
    print(f'     {"o o":^44}\033[m')

elogio()
coracao()

brasil=[]
estado1={'uf':'Rio de janeiro','sigla':RJ}
estado2={'uf':'São Paulo','sigla':SP}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])

ou seja,adc dentro da lista os dicionários e se eu quiser mostrar individualmente

estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('unidade federativa'))
    estado['sigla'] = str(input('unidade federativa'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k,c in e.items:
        print(f'o campo {k} tem valor {c}')
 Exercício Python 090: Faça um programa que leia nome e média de 
 um aluno, guardando também a situação em um dicionário. 
 No final, mostre o conteúdo da estrutura na tela.
aprovado=[]
reprovado=[]
aluno=dict()
aluno['nome']=str(input('digite seu nome :  '))
aluno['media']=float(input(f'a media de {aluno["nome"]} :  '))
if aluno['media']>=7:
    aluno['situação']='aprovado'
elif 5<= aluno['media']:
    aluno['situação']='reprovado'
else:
    aluno['situação']=reprovado
print(aluno)
print('-='*30)
for k,v in aluno.items():
    print(f' - {k} é igual a {v}')
Exercício Python 091: Crie um programa onde 4 jogadores joguem um 
dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem,
 sabendo que o vencedor tirou o maior número no dado.
 
 from random import randint
from time import sleep
from operator import itemgetter
maior=0
jogo={'jogador1':randint(1,6),
'jogador2':randint(1,6),
'jogador3':randint(1,6),
'jogador4':randint(1,6)}
ranking=list()
for k,v in jogo.items():
    print(f'{k} tirou o número {v} no dado')
    sleep(1)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(ranking)
print('-='*15, 'ranking' ,'-='*15)

for i,l in enumerate(ranking):
    print(f'{i+1}° lugar: {l[0]} com {l[1]}')
 
 Exercício Python 092: Crie um programa que leia nome, ano de 
 nascimento e carteira de trabalho e cadastre-o (com idade)
  em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
  o dicionário receberá também o ano de contratação e o salário.
   Calcule e acrescente, 
 além da idade, com quantos anos a pessoa vai se aposentar.
 
 from datetime import datetime

pessoa = dict()
pessoa['nome'] = str(input('digite seu nome :  '))
nasc = int(input('digite seu ano de nascimento :  '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('digite sua carteira de trabalho :  (digite 0 se n tiver)'))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('digite o ano da sua contratação :  '))
    pessoa['salário'] = float(input('digite o seu salário :  '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k,v in pessoa.items():
    print(f' - {k} tem o valor {v}')
    
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

pessoa = dict()
partidas=list()
pessoa['nome'] = str(input('digite o nome do jogador :  '))
p = int(input('quantas partidas ele jogou :  '))
for i in range(0,p):
    partidas.append(int(input(f'digite quantos gols ele fez na partida {i+1}  :  ')))
pessoa['gols']=partidas[:]
pessoa['total']=sum(partidas)
print('-='*30)
print(pessoa)
print('-='*30)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
print('-='*30)
print(f'o jogador {pessoa["nome"]} jogou {p} partidas e fez {pessoa["total"]} gols ')
for i,v in enumerate(pessoa['gols']):
    print(f' --> na partida {i} ,fez {v} gols')

Exercício Python 094: Crie um programa que leia nome, sexo e idade de
 várias pessoas, guardando os dados de cada
  pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
 A) Quantas pessoas foram cadastradas 
 B) A média de idade
  C) Uma lista com as mulheres 
  D) Uma lista de pessoas com idade acima da média
  
galera=list()
pessoas=dict()
soma=media=0
while True:
    pessoas.clear()
    pessoas['nome']=str(input('digite seu nome   :  '))
    while True:
        pessoas['sexo']=str(input('digite seu sexo  :   ')).upper()[0]
        if pessoas['sexo'] not in 'fFmM':
            print('erro digite seu sexo')
        else:
            break
    pessoas['idade']=int(input('digite sua idade  : '))
    soma += pessoa['idade']
    galera.append(pessoas.copy())
    while True:
        r=str(input('deseja continuar ?  :')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! DIGITE S OU N')
    if r == 'N':
        break
print(f'ao todo temos {len(galera)} pessoas ')
media= soma / len(galera)
print(f'a soma é {media:5.2f} anos ')
print('o numero de mulheres é ', end='')
for p in galera:
    if p['sexo']=='F':
        print(f'{p["nome"]}', end='')
print()
print(' a media das pessoas :',end='')
for p in galera:
    if p['idade']>=media:
        print('  '*3)
        for k,v in p.items():
            print(f'{k}={v}',end='')
        print()
        
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com 
vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

while True:
    time=list()
    pessoa = dict()
    partidas=list()
    pessoa['nome'] = str(input('digite o nome do jogador :  '))
    p = int(input('quantas partidas ele jogou :  '))
    partidas.clear()
    for i in range(0,p):
        partidas.append(int(input(f'digite quantos gols ele fez na partida {i+1}  :  ')))
    pessoa['gols']=partidas[:]
    pessoa['total']=sum(partidas)
    time.append(pessoa.copy())
    print('-='*30)
    while True:
        r = str(input('deseja continuar ?  :')).upper()[0]
        if r in 'SN':
            break
        print('ERRO !! digite S ou N !!')
    if r == 'N':
        break
print('-='*30)
print('cod  ',end='')
for i in pessoa.keys():
    print(f'{i:<15}',end='')
print()
print('-=' * 30)
for k,v in enumerate(time):
    print(f'{k:3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('=-'*30)
while True:
    busca=int(input('digite qual jogador vc quer (999 cancela) :'))
    if busca==999:
        break
    if busca>=len(time):
        print('erro !! jogador nao existe')
    else:
        print(f'--- levantamento do jogador {time[busca]["nome"]} :')
        for i,g in enumerate (time[busca]['gols']):
            print(f'   no jogo {i+1} fez {g} gols')


=================FUNÇÕES PYTHON =============
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
para criar uma função é necessário um espeaço de duas linhas entre
a função e o programa principal
-----
função contador
def contador(*num)
    tam=len(num)
    print(f'Recebi os valores {num} e são todos {tam} numeros')
    

#programa principal
contador(2,3,4)
contador(5,4,5,6,9)
contador(1) --> criam tuplas.

----------------
criando função de dobramento
def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *=2
        pos=pos+1


valores=[1,4,5,6,7,9]
dobra(valores)
print(valores)
-----------
função soma
def soma(*valores)
    s=0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')
    
    
    
soma(5,2)
soma(9,3,2)
-------------- EXERCICIOS -------
Exercício Python 096: Faça um programa que 
tenha uma função chamada área(), que receba as dimensões de um 
terreno retangular (largura e comprimento) e mostre a área do terreno.

#Função area
def area(largura,comprimento):
    a=largura*comprimento
    print(f'a area de um terreno {largura}m x {comprimento}m é de {a}m²')


#Programa principal
print('CONTROLE DE TERRENOS')
print('-='*30)
largura=float(input('digite sua largura em metros : '))
comprimento=float(input('digite o comprimento em metros : '))
area(largura,comprimento)
-------
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e 
mostre uma mensagem com tamanho adaptável.
Ex:                                                                                                                                                                        
escreva(‘Olá, Mundo!’) Saída:
                                                                                                                          
~~~~~~~~~
Olá, Mundo!                         
                                                                                                                                 
~~~~~~~~~        

#Função area
def escreva(msg):
    tam=len(msg) + 4
    print('~' *tam)
    print(f'  {msg}')
    print('~' *tam)


#Programa principal
escreva('Vinicius Gomes')
escreva('Curso de python')
escreva('rato')

Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

from time import sleep
#Função area
def contador(i,f,p):
    if p<0:
        p+= -1
    if p==0:
        p=1
    print(f'contagem do {i} até o {f} em {p}')
    sleep(2.5)
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont}',end=' ', flush=True)
            sleep(0.5)
            cont +=p
        print('  fim')
    else:
        cont=i
        while cont>=f:
            print(f'{cont}', end=' ' , flush=True)
            sleep(0.5)
            cont -= p
        print('  fim')



#Programa principal
contador(1,10,1)
contador(10,0,2)
print('-='*40)
print('agora é sua vez de personalizar')
ini=int(input('inicio  : '))
tam=int(input('tamanho  : '))
pas=int(input('passo  : '))
contador(ini,tam,pas)

-------------------------

Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. Seu programa tem que 
analisar todos os valores e dizer qual deles é o maior.

from time import sleep
#Função area
def maior(*num): #usa-se o * pois vai receber varios valores
    cont=maior=0
    print('\nanalisando os valores...')
    for valor in num:
        print(f'{valor}',end=' ',flush=True)
        sleep(0.5)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior = valor
        cont+=1
    print(f'foram informados {valor} valores ao todo')
    print(f'e o maior valor é {maior}')





#Programa principal
maior(1,10,1)
maior(10,0,2)
maior(10,0,2,5,6,7,8)
maior(1098,0,2)




-------------------------
Exercício Python 100: Faça um programa que tenha uma lista chamada números
 e duas funções chamadas sorteia() e somaPar(). A primeira função vai
 sortear 5 números e vai colocá-los dentro da lista e a segunda função 
 vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
 
 from random import randint
from time import sleep
def sorteia(lista):
    print('SORTEANDO 5 VALORES NA LISTA !!',end='')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print(f' {n} ',end='',flush=True)
        sleep(0.3)
    print('PRONTO !!')

def sompar(lista):
    soma=0
    for valor in lista:
        if valor %2==0:
            soma+=valor
    print(f'somando os valores pares da {lista}, temos {soma}')
    
--------------- FUNÇÕES PARTE 2

  help() --> função de "ajuda" do python console
  print(input.__doc__)
  help(input)
  
  ----docstring----
  def contador(i,f,p):
    c=i
    while c<=f:
        print(f'{c}',end='')
        c+=1
    print('fim')
    
    
    
contador(2,10,2)
e se nao soubermos oq é 2,10 e 2?
só escrever um rabisco oq cada um funciona e dar help(contador)
:parametro i- inicio da contagem
:parametro f- fim da contagem
:parametro p- passo da contagem
:return:- sem retorno

help(contador)

parâmetros opcionais
def somar(a,b,c=0)
ou seja,caso eu necessite apenas do a e b, o c tem q ser igual a zero para nao dar erro.
podemos por todos como parâmetros opcionais
def somar(a=0,b=0,c=0)        

----------ESCOPO DE VARÍAVEIS
uma variavel dentro de uma função tem um valor, no entanto a mesma variavel no programa principal
tem outro valor

def funcao():
    n1=4
    print(f'N1 dentro vale{n1}')
    
n1=2
funcao()--> chamada de função
print(f'N1 fora vale {n1}')

dentro=4 e fora=2

------------Retornando valores

só quer q manda o resultado

def somar(a=0.b=0,c=0)
    s=a+b+c
    return s
    
r1=somar(3,2,5)
r2=somar(2,2)
r3=somar(6)

print(f'os resultados foram {r1},{r2} e {r3}')

def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f *=c
    return f

n=int(input('digite o número:  '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
#ou
f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()
print(f'os resultados são {f1},{f2} e {f3}')

def par(b=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num=int(input('digite um numero:  '))
if par(num):
    print('é par!')
else:
    print('é ímpar!')
    

Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um 
valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f'com {idade} anos:  NÃO VOTA !!'
    elif 16<= idade <18 or idade >65:
        return f'com {idade} anos : VOTO OPCIONAL !!'
    else:
        return f'com {idade} anos :  VOTO OBRIGATÓRIO'
        
        

#Programa principal    
nasc= int(input('em que ano vocÊ nasceu?? : '))
print(voto(nasc))

Exercício Python 102: Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular 
e outro chamado show, que será um valor lógico 
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n,show=False):
 -->por 3->( "" )
    --> Calcula o fatorial de um numero
    :paramentro n: o numero a ser calculado
    :paramentro show: (opcional) mostra ou não a conta
    :return: o valor do fatorial de um numero n
   -->por 3->( "" )
    f=1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(f'{c} x ',end='')
            else:
                print(' = ',end='')
        f +=c
        return f


#programa principal
print(fatorial(5,show=True))
#help(fatorial)--> doc string


Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
 que receba dois parâmetros opcionais: o nome de um jogador e 
 quantos gols ele marcou. O programa deverá ser
 capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>',gols=0):
    print(f'o jogador {nome} fez {gols} gols no campeonato')


n=str(input('nome do jogador:  '))
g=str(input('número de gols:   '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)
    


Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
 def leiaInt(num):
    ok=False
    valor=0
    while True:
        n=str(input(num))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\O33[0;31mERRO!! DIGITE UM NUMERO INTEIRO VÁLIDO.\033[m  ')
        if ok:
            break
        return valor


n=leiaInt('digite um número:  ')
print(f'Você acabou de digitar o numero {n}  ')
 
 
 
 Exercício Python 105: Faça um programa que tenha uma função notas() 
 que pode receber várias notas de alunos e vai 
 retornar um dicionário com as seguintes informações:

– Quantidade de notas
 – A situação (opcional) 
– A média da turma
– A situação (opcional)

def notas(*n,sit=False):
    ----
     --> BOLETIM
    :paramentro n: todas as notas
    :paramentro sit: (opcional) situação do aluno
    :return: retorna o dicionário
    -----
    r=dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['situação']='BOA'
        if r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r



#programa principal
resp=notas(9,10,5.5,2.5,8.5)
#resp=notas(9,10,5.5,2.5,8.5,sit=True)
print(resp)
#help(notas)

Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
 O usuário vai digitar o comando e o manual vai aparecer.
 Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
 
 from time import sleep
cores=('\033[m',       #0 sem cor
       '\033[0;30;41m',#1 vermelho
       '\033[0;30;42m',#2 verde
       '\033[0;30;43m',#3 amarelo
       '\033[0;30;44m',#4 azul
       '\033[0;30;45m',#5 roxo
       '\033[0;30m' #6 branco
 )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(cores[5],end='')
    help(com)
    print(cores[5], end='')
    sleep(2)

def titulo(msg,cor=0):
    tam=len(msg) + 4
    print(cores[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)

#programa principal
comando=''
while True:
    titulo('sistema de ajuda pyHELP',2)
    comando=str(input('função ou biblioteca, fim para desligar:  '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!',1)
 
 
 ----------------------------Módulos e Pacotes------
 
 Modularização
 foco em dividir um programa
 aumentar a legibilidade
 facilita a manutenção
 
 -basicamente,criar as funções dentro de um arquivo chamado "-uteis.py"
 import uteis
 
 num=int(input('digite um valor:  '))
fat=uteis.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print(f'o dobro de de {num} é {uteis.dobro(num)}')
  """

