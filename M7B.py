nimet = set()
jatka = True
while jatka:
    nimi = input("Kerro nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    elif nimi not in nimet and nimi != "":
        print("Uusi nimi.")
        nimet.add(nimi)
    if nimi == "":
        jatka = False

for i in nimet:
    if i != "":
        print(i)