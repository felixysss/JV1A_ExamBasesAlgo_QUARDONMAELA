myTable = [14,25,73,84,57]
numeroCase = 0
valeurMax = 0

print(myTable)

#1)

myTable.insert(0,myTable[1])
myTable.pop(2)

myTable.insert(1,myTable[0])
myTable.pop(1)

print(myTable)


#2) et 3)

for i in range(len(myTable)):
    if(valeurMax<myTable[i]):
        valeurMax = myTable[i]
        numeroCase = i

myTable.pop(numeroCase)
myTable.append(valeurMax)

print(myTable)

myTable2=myTable[0:4]
numeroCase=0
valeurMax=0

for j in range(len(myTable2)) :
    if(valeurMax<myTable2[j]):
        valeurMax = myTable2[j]
        numeroCase = j

myTable.pop(numeroCase)
myTable.insert(3,valeurMax)

print(myTable)

myTable3=myTable[0:3]
numeroCase=0
valeurMax=0

for k in range(len(myTable3)) :
    if(valeurMax<myTable3[k]):
        valeurMax = myTable3[k]
        numeroCase = k

myTable.pop(numeroCase)
myTable.insert(2,valeurMax)

print(myTable)

myTable4=myTable[0:2]
numeroCase=0
valeurMax=0

for l in range(len(myTable4)) :
    if(valeurMax<myTable4[l]):
        valeurMax = myTable4[l]
        numeroCase = l

myTable.pop(numeroCase)
myTable.insert(1,valeurMax)

print(myTable)

#4) Le tri à bulles est considéré comme très lent car 
# on doit prendre le temps d'adapter le code à chaque fois, tout en remettant à zéro les variables. 
# On peut estimer son ordre de grandeur par le nombre d'éléments de la liste.