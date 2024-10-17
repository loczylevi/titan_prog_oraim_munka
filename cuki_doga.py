# A
    
while True:
    try:
        hany_allat = int(input("Hány állatot szeretne hozzáadni?\t"))
        
        if type(hany_allat) == int:
            break
    except:
        print("Hiba")



lista = []

amig = True
while amig:
    try:      
        for szam in range(1, hany_allat+1):
            if len(lista) == hany_allat:
                amig = False
                break
            nev = input(f"{szam}. Kérem az állat nevét:\t")
            pontszam = int(input(f"{szam}. Kérem a(z) {nev} pontszámát:\t"))
            if type(pontszam) == int:
                lista.append((nev,pontszam))
            
        
    except:
        print("hiba")
    
latni_e = input("Szeretné-e látni az állatok pontszámát és nevét? (igen/nem)\t")

if latni_e.lower() == "igen" or latni_e.lower() == "i":
    for nev, pontszam in lista:
        print(f"|Állat neve: {nev} | Pontszáma: {pontszam}")
              

atlag_e = input("Érdekel-e az állatok átlagos pontszáma? (igen/nem)\t")


try:
        
    if atlag_e.lower() == "igen" or atlag_e.lower() == "i":
        ossz = 0
        for nev, pontszam in lista:
            ossz += pontszam
        if len(lista) > 0:
            atlag = ossz / len(lista)
            print(f"Átlag:\t{atlag:.2f}")
            
except:
    print("hiba")
    

