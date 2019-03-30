print('''
Q1 - No Phyton como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variavel
c - uma caixa de sapatos
''') 
resposta = input().lower()


if resposta == "a":
    print (" Não - texto é um tipo de dado :( ")

elif  resposta == "b":
    print(" Correto! :) ")

elif resposta == "c":
    print(" Não seja estúpido! :( ")  

else:
    print(" Você não escolheu a, b ou c :( ")
    
print("Obrigado por jogar!")    
