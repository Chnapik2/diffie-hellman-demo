# Matěj Pokorný, leden 2021

from random import randint

def main():
    # 1. Domluveni se na modulu m a zakladu z
    m = randint(1,10000)
    z = randint(1,10000)
    print("Modulo je " + str(m) + "\nZaklad je " + str(z))
    print("Predejte tyto hodnoty stroji B")

    # 2. Vyber tajneho cisla a
    print("\nVybiram si tajne cislo a")
    a = randint(1,10000)
    print("Me tajne cislo je "+ str(a))

    # 3. Odeslani hodnoty x, x = z^a mod m
    x = divmod(pow(z, a), m)[1]
    print("\nPredejte stroji B hodnotu x: " + str(x))

    # 5. Prijmout hodnotu y od B
    y = input("\nZadejte hodnotu y od stroje B: ")

    # 6. Urcit klic k, k=y^a mod m
    k = divmod(pow(int(y), a),m)[1]
    print("\nKlic je: " + str(k))

    return 0

if __name__ == "__main__":
    main()
