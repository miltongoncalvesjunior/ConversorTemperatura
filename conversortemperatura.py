#coding: utf-8
#import realizado, com todas funções.
from matematica_temp import *
#interação com o usuário.
nome = input('Ola,bem-vindo qual é o seu nome?:')
print('Seja Bem vindo!', '\033[5;32m', nome, '\33[m')
print('\n==================================='
'\n      ATENÇÃO,',nome,'(◣_◢)'
'\n>Vamos lá !!!'
'\n>Escolha uma opção de 1 a 13!'
'\n>Insira o valor !'
'\n>Receba sua consulta!'
'\n>Faça uma nova consulta'
'\n===================================')
escolha = 0
while escolha !=13:
 try:
     #menu de escolha , com laço de repetição , e tratando os possiveis erros.#
  escolha = int(input('''
    Menu:
    1 - Celsius para Kelvin
    2 - Celsius para Fahrenheit
    3 - Celsius para Réaumur
    4 - Kelvin para Celsius
    5 - Kelvin para Fahrenheit
    6 - Kelvin para Réaumur
    7 - Fahrenheit para Celsius
    8 - Fahrenheit para Kelvin
    9 - Fahrenheit para Réaumur
    10 - Réaumur para Celsius
    11 - Réaumur para Kelvin
    12 - Réaumur para Fahrenheit
    13 -EXIT
    Selecione de 1 a 13 : '''))
     #if elif e else trabalhando com minhas funções.
  if escolha == 1:
                print(celskel(int(input('Insira o Valor em °C(Celsius) para ser convertido em K(Kelvin):'))))
  elif escolha == 2:
                print(celsfah(int(input('Insira o Valor em °C(Celsius) para ser convertido em °F(Fahrenheit): '))))
  elif escolha == 3:
                print(celsre(int(input('Insira o valor em °C(Celsius) para ser convertido em °Ré(Réaumur)'))))
  elif escolha == 4:
                print(kelcels(int(input('Insira 0 Valor em K(Kelvin) para ser convertido em °C(Celsius): '))))
  elif escolha == 5:
                print(kelfah(int(input('Insira o Valor em K(Kelvin) para ser convertido em °F(Fahrenheit): '))))
  elif escolha == 6:
                print(kelre(int(input('Insira o valor em K(Kelvin) para ser convertido em °Ré(Réaumur)'))))
  elif escolha == 7:
                print(fahcels(int(input('Insira o Valor em °F(Fahrenheit) para ser convertido em °C(Celsius): '))))
  elif escolha == 8:
                print(fahkel(int(input('Insira o Valor em °F(Fahrenheit) para ser convertido em K(Kelvin): '))))
  elif escolha == 9:
                print(fahre(int(input('Insira o valor em °F(Fahrenheit) para ser convertido em °Ré(Réaumur)' ))))
  elif escolha == 10:
                print(recels(int(input('Insira o valor em °Ré(Réaumur) para ser convertido em °C(Celsius)'))))
  elif escolha == 11:
                print(rekel(int(input('Insira o valor em °Ré(Réaumur) para ser convertido em K(Kelvin)'))))
  elif escolha == 12:
                print(refah(int(input('Insira o valor °Ré(Réaumur) para ser convertido em °F(Fahrenheit)'))))
  elif escolha == 13:
                print('Fim Do Programa volte sempre')
  # else tratando as condições de inserção de valor invalido fora do menu de opções .
  #except também tratando a condição de possíveis erros como inserção de letras ....
  else:
       print(nome,'opção invalida escolha de 1 a 13 ')
 except ValueError:
     print(nome,'!!!Valor invalido insira apenas números')
