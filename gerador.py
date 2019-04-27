from random import *

adjetivos = ["maravilhoso","excelente","acima da média" ]

hobbies = ["andar de bicicleta","programar","desenhar","fazer chá"]

cumprimentos = ["excelente trabalho", "realmente muito bem feito!" ,
                "suas habilidades e programação são muito,muito boas!",
                "Você é um humano excelente."]

print("Gerador de Cumprimentos")
print("___________________________________")

nome = input("Qual é o seu nome?")

#imprime um item aleatório da lista 'cumprimentos'
print(nome, choice(cumprimentos))
print("Vc é", choice(adjetivos))
print("Incrível ao", choice(hobbies))

print("De nada!")
