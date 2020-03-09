


class Person():

    def __init__(self, imie, nazwisko, wiek, wzrost, waga):
        self.wiek=wiek
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga

    def name(self):
        print("my name is",self.imie,self.nazwisko)

    def set_date(self):




pracownik= Person("kozak","kozakowski", 23,187,87)
pracownik.name()

pracownik.plec='M'
print(pracownik.__dict__)