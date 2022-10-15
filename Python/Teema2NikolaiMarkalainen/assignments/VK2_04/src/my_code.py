# -*- coding: utf-8 -*-
"""
KT4
Laita vakioon ARVATTAVA_LUKU jonka arvo on 124
Määritä vakio funktion avulla.

Tee ohjelma, joka pyytää arvaamaan lukua.
Jos käyttäjä syötti isomman luvun kuin muuttujassa, niin tulosta : ”Annoit liian suuren luvun”.
Jos taas käyttäjän syöttämä luku oli pienempi kuin vakion luku niin tulosta : ”Annoit liian pienen luvun”.



Kun käyttäjä arvaa luvun oikein niin tulosta : ”Oikein, arvasit luvun 27 kerralla!”.
Missä siis arvo 27 kertoo montako kierrosta meni ennen kuin käyttäjä arvasi oikein

"""

arvaukset = 0
veikkaus = False;
def ARVATTAVA_LUKU():
    return 124

while(veikkaus == False):
    arvaukset+=1
    luku = int(input("Arvaa luku: "))

    if luku < ARVATTAVA_LUKU():
        print("Annoit liian pienen luvun")
    elif luku > ARVATTAVA_LUKU():
        print("Annoit liian suuren luvun")

    elif luku == ARVATTAVA_LUKU():
        print("Oikein, arvasit luvun " + str(arvaukset) + " kerralla!")
        veikkaus = True

