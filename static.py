# class Matematyka:

#     @staticmethod
#     def dodawanie(a,b):
#         return a + b
    
# m = Matematyka.dodawanie(5,6)
# print(m)


class Matematyka:
    szerokosc = 0
    dlugosc = 0

    def __init__(self, szerokosc, dlugosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc


    def mydecorator(func):
        def wraper(self):
            print(f"Uzyto funkcji")
            print(func(self)) 
            print(f"Koniec funkcji")
        return wraper


    @classmethod
    def kwadrat(cls, bok):
        return cls(bok, bok)
    
    @mydecorator
    def pole(self):
        return self.szerokosc * self.dlugosc
    

m = Matematyka(4,5)
m.pole()


