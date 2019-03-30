print(2*8)
print(12,50*12)
print(12.50*12)
print("O resultado é:",10+10)
print("Minha idade em 2025 será:",2025-2006)
print("Idade de nascido em 1998 em 2025:",2025-1998)
print("Idade de nascido hoje em 2050:",2050-2019)
print("-------------------------------------------")

print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)

print("Para qual ano você quer saber a sua idade?")
ano = input()
ano = int(ano)

idade = ano - nascimento

if(idade < 90):
    print("Quem nasceu em ",nascimento,"terá",ano - nascimento,"anos")
else:
    print("Desculpe, mas acho que vc não vai viver até os",idade,"anos")
    

