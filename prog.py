"""2.feladat"""
"""
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


"""

#________________________________________________________________________________

print("________________________________________________________________________________")

while True:
    try:
        hany = int(input("hány diákot szeretne hozzáadni?\t"))
        if type(hany) == int:
            break
    except:
        print("valami nem jó")
    
        
lista = []

meddig = 0
while meddig < hany:
    try:
        diak = input(f"Kérem az {meddig+1}. diák nevét:\t")
        jegy = int(input(f"Kérem a {diak} jegyét:\t"))
        if 0 < jegy < 6:
            lista.append((diak, jegy))
        else:
            print("Rossz intervallum")
        if type(jegy) == int and 0 < jegy < 6:
            meddig += 1
    except:
        print("valami nem jó")


def kiirat():
    bekeres = input("\nSzeretné-e megtekinteni a listát? (igen/nem)")
    if bekeres.lower() == "igen":
        for diak,osztalyzata in lista:
            print(f"Diák neve: {diak} | osztáylzata: {osztalyzata}")
        

bekeres2 = input("\nÁtlag számitás érdekel?\t")

jegyek = [szam[1] for szam in lista]
atlag = sum(jegyek) / len(jegyek)

if bekeres2.lower() == "igen":
    print(f"jegyek: {jegyek}\t|\tÁtlag: {atlag:.2f}")
    

bekeres3 = input("\nLegnagyobb és legkisebb elemet kiirjam? (igen/nem)\t")

legnagyobb = jegyek[0]
legkisebb = jegyek[0]
    
for szam in jegyek:
    if szam > legnagyobb:
        legnagyobb = szam
    if szam < legkisebb:
        legkisebb = szam
        
if bekeres3.lower() == "igen":      
    print(f"Legnagyobb jegy: {legnagyobb}\nLegkisebb jegy: {legkisebb}")


eltavolitas = input("\nEltávolitsak diákot?\t")

if eltavolitas.lower() == "igen":
    diak_neve = input("Kérem a diák nevét:\t")
    index = 0
    for diak,jegy in lista:
        if diak_neve.lower() == diak.lower():
            lista.pop(index)
            print(f"{diak_neve} eltávolitva!")
        index += 1
        
kiirat()



        
        
    





