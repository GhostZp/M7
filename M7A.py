vuodenaika = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausinumero = int(input("Kerro kuukauden numero(1-12): "))

if kuukausinumero in (12, 1, 2):
    print(f"{vuodenaika[0]}")

elif kuukausinumero in (3, 4, 5):
    print(f"{vuodenaika[1]}")

elif kuukausinumero in (6, 7, 8):
    print(f"{vuodenaika[2]}")

elif kuukausinumero in (9, 10, 11):
    print(f"{vuodenaika[3]}")
else:
    print("Virheellinen kuukausi")
