# -*- coding: utf-8 -*-

"""

KT5

Esittele muuttuja pii, jolle annat alkuarvoksi piin likiarvon 6 desimaalin tarkkuudella.
Lue käyttäjältä ympyrän halkaisija ja tulosta ympyrän piiri ja pinta-ala kahden desimaalin tarkkuudella

Malli ohessa:

Anna ympyrän halkaisija: 12
Piiri on 37.70
Pinta-ala on 113.10

"""

pii = 3.141593
halkaisija = int(input("Anna ympyrän halkaisija: "))
piiri = 2* pii * 6
print("Piiri on {:0.2f}"  .format(piiri))
pintaAla= pii*((halkaisija/2)**2)
print("Pinta-ala on {:0.2f}".format(pintaAla))
