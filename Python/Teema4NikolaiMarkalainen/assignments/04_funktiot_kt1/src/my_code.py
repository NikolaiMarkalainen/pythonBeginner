"""
KT1


Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 

Funktio palauttaa kokonaislukuarvon seuraavasti:

 

1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.

-1, jos syötetty luku on negatiivinen. 

 

Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.


”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

"""

#Write KysyJaTestaaLuku function here!
def KysyJaTestaaLuku():
    luku = int(input("Syotä luku: "))
    if(luku >= 1):
        print("Luku oli positiivinen")
        return 1
    if(luku == 0):
        print("Luku oli nolla")
        return 0
    if (luku <= -1):
        print("Luku oli negatiivinen")
        return -1
if __name__ == "__main__":
    #Write main program below this line
    KysyJaTestaaLuku()

