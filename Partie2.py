#1)
morpion1=["□","□","□"]
morpion2=["□","□","□"]
morpion3=["□","□","□"]

print(morpion1)
print(morpion2)
print(morpion3)

#2)
print("Que voulez-vous jouer ?")
touche=input()

if(touche == 'O'):
    print("Où voulez-vous jouer ?")
    choix=input()
    if(choix == '0') :
        choix=0
        morpion1.pop(choix)
        morpion1.insert(0,touche)
    if(choix == '1') :
        choix=1
        morpion1.pop(choix)
        morpion1.insert(1,touche)
    if(choix == '2') :
        choix=2
        morpion1.pop(choix)
        morpion1.insert(2,touche)
    if(choix == '3') :
        choix=0
        morpion2.pop(choix)
        morpion2.insert(0,touche)
    if(choix == '4') :
        choix=1
        morpion2.pop(choix)
        morpion2.insert(1,touche)
    if(choix == '5') :
        choix=2
        morpion2.pop(choix)
        morpion2.insert(2,touche)
    if(choix == '6') :
        choix=0
        morpion3.pop(choix)
        morpion3.insert(0,touche)
    if(choix == '7') :
        choix=1
        morpion3.pop(choix)
        morpion3.insert(1,touche)
    if(choix == '8') :
        choix=2
        morpion3.pop(choix)
        morpion3.insert(2,touche)


if(touche == 'X'):
    print("Où voulez-vous jouer ?")
    choix=input()
    if(choix == '0') :
        choix=0
        morpion1.pop(choix)
        morpion1.insert(0,touche)
    if(choix == '1') :
        choix=1
        morpion1.pop(choix)
        morpion1.insert(1,touche)
    if(choix == '2') :
        choix=2
        morpion1.pop(choix)
        morpion1.insert(2,touche)
    if(choix == '3') :
        choix=0
        morpion2.pop(choix)
        morpion2.insert(0,touche)
    if(choix == '4') :
        choix=1
        morpion2.pop(choix)
        morpion2.insert(1,touche)
    if(choix == '5') :
        choix=2
        morpion2.pop(choix)
        morpion2.insert(2,touche)
    if(choix == '6') :
        choix=0
        morpion3.pop(choix)
        morpion3.insert(0,touche)
    if(choix == '7') :
        choix=1
        morpion3.pop(choix)
        morpion3.insert(1,touche)
    if(choix == '8') :
        choix=2
        morpion3.pop(choix)
        morpion3.insert(2,touche)

print(morpion1)
print(morpion2)
print(morpion3)
