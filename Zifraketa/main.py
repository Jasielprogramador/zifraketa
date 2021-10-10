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
       " DINHXKCIK HKCZJOI OKEJSZCNHE".upper()

letters = Counter(text)

alfabeto_mayus = []
for i in range(65, 91):
    if(i == 79):
        alfabeto_mayus.append('Ñ')
    alfabeto_mayus.append(chr(i))


prob = Counter(alfabeto_mayus)

texto_plano = text.replace(",","").replace(".","").replace(" ","").upper()

for i in letters:
    if alfabeto_mayus.__contains__(i):
        prob[i] = round((letters[i] / len(texto_plano)) * 100,3)

print(prob)

freq_sp = {"E":16.78, "A":11.96, "O":8.69, "L":8.37, "S":7.88, "N":7.01,
           "D":6.87, "R":4.94, "U":4.80, "I":4.15, "T":3.31, "C":2.92,
           "P":2.776, "M":2.12, "Y":1.54, "Q":1.53, "B":0.92, "H":0.89,
           "G":0.73, "F":0.52, "V":0.39, "J":0.30, "Ñ":0.29, "Z":0.15,
           "X":0.06, "K":0.00, "W":0.00}

lista = ["A"]*len(texto_plano)

frecuencias_generales = list(freq_sp.keys())
frecuencias_texto = list(prob.keys())

solucion = text.upper()

for i in range(len(text)):
    if(text[i] == solucion[i] and text[i].isalpha()):
        index = frecuencias_texto.index(text[i])
        solucion = solucion[:i]+frecuencias_generales[index]+solucion[i+1:]

    else:
        solucion = solucion+text[i]


print(solucion)



