from random import *

executa = True
adjetivos = ["maravilhoso","excelente","acima da média" ]
hobbies = ["andar de bicicleta","programar","desenhar","fazer chá"]

print("Gerador de Cumprimentos")
print("___________________________________")

nome = input("Qual é o seu nome?")

print('''
Menu
c = obter cumprimento
a = adicionar hobby
d = remover hobby
p = imprimir hobbies
q = sair
''')

while executa == True:

  menuChoice = input("\n>_").lower()

  #'c' para  cumprimento
  if menuChoice == 'c':

    print("Aqui está o seu cumprimento" , nome , ":")
    #obtem um item aleatório de ambas as listas e adiciona-os ao cumprimento
    print(nome," você é" ,choice(adjetivos), "em", choice(hobbies))
    print("De nada!")
