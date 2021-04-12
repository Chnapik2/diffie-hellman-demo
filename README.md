# Demo algortimu Diffie-Hellman

Matěj Pokorný

Demonstrace fungování algoritmu pro  bezpečnou
výměnu klíčů přes nezabezpečený komunikační
kanál.

## Spuštění

> python machineA.py

> python machineB.py

Po spuštění obou programů následujte instrukce v terminálech.

## Příklad výmeny klíčů pomocí DH (s konkrétními hodnotami)
1. Uzly A a B se dohodnou na použitém modulu m=23 a základu z=5
2. Uzel A si zvolí tajné číslo a=6
3. Uzel A pošle uzlu B hodnotu x=z^a mod m, tj. x=5^6 mod 23=8
4. Uzel B si zvolí tajné číslo b=15
5. Uzel B pošle uzlu A hodnotu y=z^b mod m, tj 5^15 mod 23=19
6. Uzel A určí klíč k=y^a mod m, tj. k=19^6 mod 23=2
7. Uzel B spočítá klíč k=x^b mod m, tj. k=8^15 mod 23=2