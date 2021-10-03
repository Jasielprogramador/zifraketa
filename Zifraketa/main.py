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
print(len(text))

alfabeto_mayus = []
alfabeto_minus = []
for i in range(65, 91):
    alfabeto_mayus.append(chr(i))

for i in range(97, 123):
    alfabeto_minus.append(chr(i))

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
emaitza = Counter(abc)

print(letters)
kont = 0

for i in letters:
    if alfabeto_mayus.__contains__(i):
        kont = kont + letters[i]
        emaitza[i] = (letters[i] / len(text)) * 100

print(emaitza)

deszifratuta = text.replace("X", "E").replace('E', 'A').replace('K', 'O').replace('I', 'L').replace('C', 'S').replace(
    'J', 'N').replace('T', 'D').replace('A', 'R').replace('R', 'U').replace('Z', 'I').replace('H', 'T').replace('N', 'C') \
    .replace('P', 'P').replace('D', 'M').replace('O', 'Y').replace('Q', 'Q').replace('Ñ', 'H').replace('W','G').replace('Y','F') \
    .replace('S', 'V').replace('G', 'J').replace('V', 'Ñ').replace('U', 'Z').replace('M', 'X').replace('F','K').replace('L','W')

# print(deszifratuta)
