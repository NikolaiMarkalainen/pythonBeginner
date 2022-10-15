# -*- coding: utf-8 -*-

#
# KT2
#
# Kysy käyttäjältä, montako lukua arvotaan.Jos käyttäjä syöttää arvon < 1, tulostuu "Virhe!"
# Tee lista ja arvo siihen em määrä lukuja  väliltä 0-20.
# Vain parilliset luvut sallitaan.
# Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
# Tulosta luvuista suurin ja pienein samalle riville
# Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna
# Huomaa, että viimeisen luvun jälkeen ei tule pilkkua
#
# Esimerkkiajo ohessa
#
# Montako lukua arvotaan: 3
# Suurin: 6 ja pienin: 0
# 4,0,6
#

import random

luku = int(input("Montako lukua arvotaan: "))
if(luku < 1 ):
    print("Virhe!")
arpaLuvut = []
x = 0
for x in range(0, luku):
    arvot = random.randrange(0, 20, 2)
    arpaLuvut.append(arvot)
    x+=1
    if(x == luku):
        print("Suurin:", max(arpaLuvut), "ja pienin:", min(arpaLuvut))
        print(*arpaLuvut, sep=",")