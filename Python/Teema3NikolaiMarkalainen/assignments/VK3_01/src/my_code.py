# -*- coding: utf-8 -*-

#
# KT1
#
# Luo aluksi tyhjä lista (muuttujanimi: luvut) ja lue siihen käyttäjältä 5 kokonaislukuarvoa.
# Tulosta lopuksi syötettyjen lukujen summa (kokonaislukuna) ja keskiarvo kolmella desimaalilla
#
# Esimerkkiajo ohessa
#
# Anna luku: 1
# Anna luku: 2
# Anna luku: 3
# Anna luku: 4
# Anna luku: 5
# Summa on: 15
# Keskiarvo on: 3.000
#
luvut = []
for x in range(0,5):
    luvut.append(int(input("Anna luku: ")))

luku  = sum(luvut)
keskiArvo = "{: .3f}".format(luku / len(luvut))

print("Summa on: ", luku)
print("Keskiarvo on: ", keskiArvo)

