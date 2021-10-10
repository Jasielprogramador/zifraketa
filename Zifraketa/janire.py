import sys
from pprint import pprint

text =sys.argv[1]

newtext = text.replace('"','').replace(' ','').replace('.','').replace(',','').upper()
newtext = ''.join([i for i in newtext if not i.isdigit()])

freq_sp = {"e":16.78, "a":11.96, "o":8.69, "l":8.37, "s":7.88, "n":7.01, "d":6.87, "r":4.94, "u":4.80, "i":4.15, "t":3.31, "c":2.92, "p":2.776, "m":2.12, "y":1.54, "q":1.53, "b":0.92, "h":0.89, "g":0.73, "f":0.52, "v":0.39, "j":0.30, "ñ":0.29, "z":0.15, "x":0.06, "k":0.00, "w":0.00}

freq_text = {}

for key in newtext:
    if key in freq_text:
        freq_text.update({key:round(freq_text[key]+100/len(newtext),3)})
    else:
        freq_text[key] = round(100/len(newtext),3)

cont = True
plaintext = text
changes = []
while cont:
    print("\nSpanish letter frquency: ", freq_sp)
    print("\nText's letter frequency: ")
    pprint(freq_text)
    print("\nThis is the actual text: ", plaintext)
    print("\nThese are the changed letters: ", changes)
    print("Do you want to change any letter? (Y/N): ")
    answer = input().upper()
    while not(answer == "Y" or answer == "N"):
        print("\nType your answer again: ")
        answer = input.upper()
    if (answer == "Y"):
        print("What letter do you want to change?: ")
        letter = input().upper()
        while not(letter.isalpha()):
            print("\nThat's not a letter, type it again: ")
            letter = input().upper()
        print("What letter do you want to put instead?: ")
        new_letter = input().upper()
        while not(new_letter.isalpha()):
            print("\nThat's not a letter, type it again: ")
            new_letter = input().upper()
        for i in range(len(plaintext)):
            if ((plaintext[i] == letter) and (plaintext[i] == text[i])):
                plaintext = plaintext[:i] + new_letter.lower() + plaintext[i+1:]
                changes.append(text[i] + "-->" + new_letter)
                changes = list(dict.fromkeys(changes))

    elif answer == "N":
        cont = False
