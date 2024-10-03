"""2.feladat"""

import random

lista = []

for szam in range(10):
    veletlen = random.randint(0,100)
    lista.append(veletlen)
    
print(f"lista: {lista}")

print(max(lista))

print(min(lista))

lista.sort()

print(f"sortolás: {lista}")

#lista = [0,12,2,3,4,5,6,7,78,9,"asdasd","asdasdasdasdasd"]
#print(max(lista))
#y = max([i for i in lista if type(i) == int])
#print(y)
def valami(a:list):
    for x in a:
        print(x)     
#print(valami([0,1,2,3,4,5,6,7,8]))
        
        
paros_szamok = [szam for szam in lista if szam % 2 == 0]

print(f"paros számok: {paros_szamok}")



titnya = [0,4,2,5,7]


def valami(titnya:list):
    db = 0
    for szam in titnya:
        if szam == 2:
            return db
        db = db + 1
        
titnya2 = [0,4,2,5,7, 2]

def valami23(titnya2:list):
    db = 0
    kettes = 0
    for szam in titnya2:
        if szam == 2:
            kettes = db

        db = db + 1
    return kettes

def valami_nyunyor(titnya2:list):
    db = 0
    ize = False
    for szam in titnya2:
        if szam == 2 and ize:
            return db
        if szam == 2:
            ize = True

        db = db + 1
    return kettes


    
print(f"2-es indexe: {valami(titnya)}")

print(f"2-es indexe: {valami23(titnya2)}")


print(f"2-es indexe: {valami_nyunyor(titnya2)}")


egyik = ("alma","dinnye","citrom","eper")

masik = ("répa","zoldseg","cékla","gyömbér","alma", "citrom")

print(f"egyik halmaz: ",egyik)

print(f"Másik halmaz: ",masik)

print(f"unio: {egyik | masik}")
