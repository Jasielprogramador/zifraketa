import string
from collections import Counter

text = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX," \
       " E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK " \
       "ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX," \
       " E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ " \
       "EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX" \
       " IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN " \
       "DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ" \
       " KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX " \
       "HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX" \
       " JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ " \
       "UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN " \
       "TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT " \
       "OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE " \
       "AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT" \
       " DINHXKCIK HKCZJOI OKEJSZCNHE"

letters = Counter(text)

alfabeto_mayus = []
for i in range(65, 91):
    if(i == 79):
        alfabeto_mayus.append('Ñ')
    alfabeto_mayus.append(chr(i))


prob = Counter(alfabeto_mayus)

texto_plano = text.replace(",","").replace(".","").replace(" ","").replace("[","").upper()

for i in letters:
    if alfabeto_mayus.__contains__(i):
        prob[i] = round((letters[i] / len(texto_plano)) * 100,3)

print(prob)

lista = ["A"]*len(texto_plano)

for i in range(len(texto_plano)):
    if(texto_plano[i] == "X"):
        lista[i] = "E"
    elif (texto_plano[i] == "E"):
        lista[i] ="A"
    elif(texto_plano[i] == "K"):
        lista[i] = "O"
    elif (texto_plano[i] == "I"):
        lista[i] = "L"
    elif (texto_plano[i] == "C"):
        lista[i] = "S"
    elif (texto_plano[i] == "J"):
        lista[i] = "N"
    elif (texto_plano[i] == "T"):
        lista[i] = "D"
    elif (texto_plano[i] == "A"):
        lista[i] = "R"
    elif (texto_plano[i] == "R"):
        lista[i] = "U"
    elif (texto_plano[i] == "Z"):
        lista[i] = "I"
    elif (texto_plano[i] == "H"):
        lista[i] = "T"
    elif (texto_plano[i] == "N"):
        lista[i] = "C"
    elif (texto_plano[i] == "D"):
        lista[i] = "M"
    elif (texto_plano[i] == "O"):
        lista[i] = "Y"
    elif (texto_plano[i] == "Ñ"):
        lista[i] = "H"
    elif (texto_plano[i] == "W"):
        lista[i] = "G"
    elif (texto_plano[i] == "Y"):
        lista[i] = "F"
    elif (texto_plano[i] == "S"):
        lista[i] = "V"
    elif (texto_plano[i] == "G"):
        lista[i] = "J"
    elif (texto_plano[i] == "V"):
        lista[i] = "Ñ"
    elif (texto_plano[i] == "U"):
        lista[i] = "Z"
    elif (texto_plano[i] == "M"):
        lista[i] = "X"
    elif (texto_plano[i] == "F"):
        lista[i] = "K"
    elif (texto_plano[i] == "L"):
        lista[i] = "W"



print(lista)
