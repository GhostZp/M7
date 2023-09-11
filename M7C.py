lentokentta = {}

print("1)Syötä uusi lentokenttä")
print("2)Hae lentokenttiä")
print("3)Lopeta")

toiminto = input("Valitse toiminto (1,2,3): ")

while toiminto in ("1", "2"):
    if toiminto == "1":
        icao = input("Kerro lentokentän icao koodi: ")
        nimi = input("Kerro lentokentän nimi: ")

        lentokentta[icao] = nimi

    elif toiminto == "2":
        icao = input("Kerro lentokentän icao koodi: ")

        print(lentokentta[icao])

    print("1)Syötä uusi lentokenttä")
    print("2)Hae lentokenttiä")
    print("3)Lopeta")

    toiminto = input("Valitse toiminto (1,2,3): ")