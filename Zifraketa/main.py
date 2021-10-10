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


freq_sp = {'e':16.78, 'a':11.96, 'o':8.69, 'l':8.37, 's':7.88, 'n':7.01, 'd':6.87, 'r':4.94, 'u':4.80, 'i':4.15,
           't':3.31, 'c':2.92, 'p':2.776, 'm':2.12, 'y':1.54, 'q':1.53, 'b':0.92, 'h':0.89, 'g':0.73, 'f':0.52,
           'v':0.39, 'j':0.30, 'ñ':0.29, 'z':0.15, 'x':0.06, 'k':0.00, 'w':0.00}

emaitza = Counter(alfabeto_mayus)

texto_plano = text.replace(",","").replace(".","").replace(" ","").replace("[","").upper()

for i in letters:
    if alfabeto_mayus.__contains__(i):
        emaitza[i] = round((letters[i] / len(texto_plano)) * 100,3)

print(emaitza)

deszifratuta = texto_plano.replace("X", "E").replace('E', 'A').replace('K', 'O').replace('I', 'L').replace('C', 'S').replace(
    'J', 'N').replace('T', 'D').replace('A', 'R').replace('R', 'U').replace('Z', 'I').replace('H', 'T').replace('N', 'C') \
    .replace('P', 'P').replace('D', 'M').replace('O', 'Y').replace('Q', 'Q').replace("B","B").replace("Ñ","H").replace('W', 'G').replace("Y","F").replace("S","V")\
    .replace("G","J").replace("V","Ñ").replace("U","Z").replace("M","X").replace("F","K").replace("L","W")

print("TEXTO DESCIFRADO: "+deszifratuta)
