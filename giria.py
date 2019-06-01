dicionario = {
    "rs"    :   "risos" ,
    "tmb"   :   "também",
    "vc"    :   "você",
    "véi"   :   "Meu pai",
    "sepah" :   "se rolar",
    "nóix"  :   "nós",
    "vei"   :   "Meu pai",
    "tc"    :   "vamos conversar",
    "qq"    :   "qualquer",
    "qlqr"  :   "qualquer",
    "vlw"   :   "valeu",
    "flw"   :   "falou",
    "t+"    :   "até mais",
    "tmj"   :   "estamos juntos",
    "hj"    :   "hoje"
 }


sentenca = input("Insira uma frase para traduzir\n").lower()

paraTraduzir = sentenca.split()

traducao = ""

for palavra in paraTraduzir:
    if palavra in dicionario:
        traducao += dicionario[palavra] + " "
    else:
        traducao += palavra + " "

print("Traduzindo:")
print(traducao)
