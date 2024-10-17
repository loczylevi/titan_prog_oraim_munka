"""1. Feladat: Osztás nullával
    Leírás: Írj egy programot, amely két számot kér be a felhasználótól, és elvégzi a második szám osztását az elsővel. Ha a második szám nullával egyenlő, a program ne omoljon    össze, hanem írjon ki egy hibaüzenetet, hogy nullával nem lehet osztani.

    Használd a try-except blokkot a ZeroDivisionError hibára.


2. Feladat: Helytelen adattípus
    Leírás: Készíts egy programot, amely egy számot kér be a felhasználótól, és kiírja annak négyzetét. Ha a felhasználó nem számot ad meg, a program figyelmeztessen, hogy     helytelen adattípust adott meg.




3. Feladat: Fájl olvasása
    Leírás: Írj egy programot, amely megpróbál megnyitni és beolvasni egy data.txt nevű fájlt. Ha a fájl nem található, a program írja ki, hogy a fájl nem létezik.



4. Feladat: Lista elem lekérése index alapján
    Leírás: Készíts egy programot, amely egy listából kér le elemeket egy megadott index alapján. Kérj be egy indexet a felhasználótól, és próbáld meg kiolvasni az adott indexű    elemet a listából. Ha az index kívül esik a lista határain, kezelje a program a hibát.
    
    
"""


print("________________________________________________________________--1#_________________________________________")

try:
    szam1 = int(input("kérem az egyik számot\t"))
    szam2 = int(input("kérem a másik számot\t"))
    osztas = szam1 / szam2
    print(f"{szam1} osztva {szam2} = {osztas}")
except ZeroDivisionError:
    print("Nullával való osztás nem értelmezhető a valós számok halmazán!")
    

print("________________________________________________________________--2#_________________________________________")



try:
    bekeres = int(input("Kérek egy számot\t"))
    print(f"A szám négyzete: {bekeres**2}")
except:
    print("valami nem jó kekszi\nHibás adattipus")
    


#3. Feladat: Fájl olvasása
#Leírás: Írj egy programot, amely megpróbál megnyitni és beolvasni egy data.txt nevű fájlt.
#Ha a fájl nem található, a program írja ki, hogy a fájl nem létezik.
    

try:
    with open("data.txt", "r") as f:
        falj = f.read()
        print(f"{falj}")
except:
    print("hiba nem létezik a fálj")
        


import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        falj = f.read()
        print(f"{falj}")
else:
    print("hiba nem létezik a fálj")
    



#Feladat: Lista elem lekérése index alapján
#Leírás: Készíts egy programot, amely egy listából kér le elemeket egy megadott index alapján.
#Kérj be egy indexet a felhasználótól, és próbáld meg kiolvasni az adott indexű    elemet a listából.
#Ha az index kívül esik a lista határain, kezelje a program a hibát.
    

lista = []
import random
for szam in range(10):
    lista.append(random.randint(0,100))
    
    
print(f"lista:\t{lista}")

try:
    index = int(input("kérek egy indexet 0-99-ig!"))
    lista_elem = lista[index]
    print(f"lista {index+1}. eleme: {lista_elem}")
except:
    print("rossz indexelés")
    
    
    
    



    
    
