# -*- coding: utf-8 -*-
"""

KT4

Lue nimi, pituus ja paino em nimisiin muuttujiin. Käytä juuri noita muuttujanimiä.
Esittele lisäksi bmi muuttuja ja alusta se nollaksi. Kysy käyttäjältä nimi, pituus metreinä ja paino kiloina.
Laske painoindeksi bmi muuttujaan seuraavasti:


bmi = paino / pituus ^ 2



Tulosta lopuksi:


Jussi Juonio pituutesi on 1.81 m ja painosi 104.0 kg
Painoindeksisi on siten 31.75

Huomaa, että bmi tulee kahdella desimaalilla

"""
bmi = 0
nimi = "Jussi Juonio"
pituus = 1.81
paino = 104.0

print(nimi + " pituutesi on " + str(pituus) + " m ja painosi on " + str(paino) + " kg")
bmi = paino/pituus**2.0
bmi = round(bmi,2)
print("Painoindeksisi on siten " + str(bmi))

