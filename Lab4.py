import re
txt = "Dopasowuje pozycje, ktora nie jest granica slowa"
x = re.search("^Dopasowuje.*slowa.$", txt)
print(x)

# findall - Zwraca liste zawierajaca wszystkie wystapienis
# search - Zwraca obiekt match, jesli w dowolnym miejscu znajdzie dopasowanie
# split - zwraca liste w ktorej ciagu znakow zostal podzielony przy kazdym 

# sub - zastepuje jedno lub wiecej wystapien

# [a-Z] - zwraca dopasowania pasujace do wzoru od a-z, male litery
# [a-k] - 
# [a-zA-Z]
# [0-9] -
# [678] -
# [^michal] -> c 
# 00-62
# [0-6][0-9] ->56 / 72
# [+]



txt = "Dopniewuje nie poznieycje, ktora nie jest non nic grannieica nie slowa"
x = re.findall("nie", txt)
print(x)

x=re.split("\s", txt)
print(x)


x=re.split("\s", txt,1)
print(x)


x=re.sub("nie", "WOW",txt)
print(x)


x=re.sub("nie", "WOW",txt,1)
print(x)

x=re.findall(r'\bnie\b', txt)
print(x)


x=re.findall(r'\w', txt)
print(x)


x=re.findall(r'[\w\.]+', txt)
print(x)

mail = "orest.kolenko@gmail.com"

x=re.split("@",mail)
print(x)

x = re.match("^[\w\.]+@[\w\.]+",mail)
print(bool(x))



txt1 = "Rok 2023 bedzie lepszy."

x = re.sub("\d",'X' , txt1)
print(x)


x = re.findall(r"\b[n]\w+",txt)
print(x)

kot = "Nasz kot ma 6 lat i wazy 4 kg."
x = re.findall(r"\d+", kot)
print(x)


x = re.search(r"kg$", kot)
print(x)

x = re.search(r"nasz", kot, re.IGNORECASE)
print(x)

tel = "moj numer to 123-456-7890."
x = re.search(r"\d+-\d+-\d+", tel)
print(x)

x = re.search(r"\d{3}-\d{3}-\d{4}", tel)
print(x)

