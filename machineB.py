# Matěj Pokorný, leden 2021

from random import randint

def main():
    # 1. Domluveni se na modulu m a zakladu z
    m = input("Zadejte modulo urcene strojem A: ")
    z = input("Zadejte zaklad urceny strojem A: ")
    print("Modulo je " + str(m) + "\nZaklad je " + str(z))

    # 4. Vyber tajneho cisla b
    print("\nVybiram si tajne cislo b")
    b = randint(1,10000)
    print("Me tajne cislo je "+ str(b))

    # 5. Odeslat hodnotu y, y=z^b mod m
    y = divmod(pow(int(z), int(b)), int(m))[1]
    print("\nPredejte stroji A hodnotu y: " + str(y))

    # 3. Prijeti hodnoty x, x = z^a mod m
    x = input("\nZadejte hodnotu x od stroje A: ")

    # 6. Urcit klic k, k=x^b mod m
    k = divmod(pow(int(x), int(b)), int(m))[1]
    print("\nKlic je: " + str(k))

    return 0

if __name__ == "__main__":
    main()