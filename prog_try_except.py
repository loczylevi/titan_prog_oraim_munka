

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



        
        
    





