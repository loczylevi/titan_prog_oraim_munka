"""
1. Feladat: Egyszerű Osztály Definiálása
    Leírás: Hozz létre egy Dog nevű osztályt, amely a kutyák nevét és életkorát tárolja.
    Az osztálynak legyen egy metódusa, amely kiírja a kutya adatait.

    Feladat:

    Készíts egy osztályt, amelynek van egy __init__ metódusa (konstruktor), amely a kutya nevét és életkorát tárolja.

    Hozz létre egy metódust display_info() néven, amely kiírja a kutya nevét és életkorát.

    Példányosítsd az osztályt, és hívd meg a metódust.
"""



class Dog:
    def __init__(self,neve,eletkor):
        self.neve = neve
        self.eletkor = int(eletkor)
    def display_info(self):
        print(f"kutya neve: {self.neve}")
        print(f"kutya életkora: {self.eletkor}")
        
        
pelda = Dog("Buksi",12)

print(pelda.display_info())
        

"""

2. Feladat: Banki Számla Osztály

    Leírás: Hozz létre egy BankAccount nevű osztályt, amely banki számlákat reprezentál.
    Az osztály képes legyen befizetést és pénzfelvételt végrehajtani, valamint a számla egyenlegét lekérdezni.

    Feladat:

    Hozz létre egy osztályt, amely egy balance változót tárol.

    Készíts metódusokat:

    deposit(amount): hozzáadja az összeget az egyenleghez.

    withdraw(amount): levonja az összeget az egyenlegből, ha van elég pénz a számlán.

    get_balance(): visszaadja az aktuális egyenleget.

    Példányosítsd az osztályt, és végezz rajta befizetést, pénzfelvételt, és kérdezd le az egyenleget.
    
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def desposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
    
    def get_balance(self):
        return self.balance
    
befizetes = BankAccount(1000)
print(befizetes.desposit(400))
print(befizetes.withdraw(200))
print(befizetes.get_balance())




"""

3. Feladat: Diák Osztály és Átlag Számítása
    Leírás: Készíts egy Student nevű osztályt, amely tárolja a diák nevét és jegyeit,
és legyen képes kiszámolni az átlagukat.


    Feladat:

    Az osztály tárolja a diák nevét és egy jegyek listáját.
    Legyen egy metódus add_grade(grade), amely hozzáad egy jegyet a listához.
    Legyen egy metódus get_average(), amely kiszámolja és visszaadja az átlagot.
    Példányosíts egy diákot, adj hozzá jegyeket, és számold ki az átlagát.
    
"""


class Student:
    def __init__(self, nev, jegy):
        self.nev = nev
        self.jegy = jegy
    def add_grade(self, grade):
        self.jegy.append(grade)
        return self.jegy
    def get_avarage(self):
        return sum(self.jegy) / len(self.jegy)
    

emberke = Student("Cumi",[1,2,2,2,4,5])

print(emberke.add_grade(1))

print(emberke.get_avarage())







        
        
    
        
    

        
        
        



        
        
        
    
    


