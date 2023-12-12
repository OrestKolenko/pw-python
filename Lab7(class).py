import json

def read_from_file(nazwa_pliku, nazwa):
    try:
        with open(nazwa_pliku, "r", encoding="utf8") as file:
            dane = json.load(file)
            if nazwa == dane["nazwa"]:
                return dane
    except FileNotFoundError:
        return False
    

def pokaz_przepis(przepis):
    print(f"Przepis na ciasto {przepis['nazwa']}")
    for skladniki, dane in przepis['skladniki'].items():
        print(f"- {skladniki}: {dane['ilosc']} {dane['jednostka']}")

def save_to_file(nazwa_pliku, przepis):
    with open(nazwa_pliku, 'w') as file:
        return json.dump(przepis, file, indent=4)
    
def dodaj_ciasto(ciasto, nazwa):
    ciasto["nazwa"] = nazwa

def dodaj_skladnik(nazwa, skladnik, ilosc, jednostka):
    ciasto[nazwa]["skladniki"][skladnik] = {
            "ilosc": ilosc,
            "jednostka": jednostka
        }

# przepis = read_from_file("ciasto.json", "Jablecznik")
# pokaz_przepis(przepis)
ciasto = {}
dodaj_ciasto(ciasto, "Czekoladowe")
dodaj_skladnik(ciasto, "Czekolada", "1", "sztuk")
dodaj_skladnik(ciasto, "Mleko w proszki" ,"1", "sztuk")
save_to_file("czekolada", ciasto)



# pppp = PrzepisNaCiasto("Jablecznik")
# ppp.dodaj_skladniki()
# ppp.dodaj_skladnik()
# ppp.save_to_file()
