# -*- coding: utf-8 -*-

"""
KT 5

Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

"""
lst = []
nimi = input("Anna nimesi: ")

if(len(nimi) > 18):
    print("Virhe!")

else:
    for i in nimi:
        lst.append(i)

    lst.reverse()
    space = "  " * (len(nimi) - 1)
    pituus = len(nimi) - 2
    with open("nimi.txt", 'w') as fr:
        for i in range (0 , len(nimi)):
            print(space + lst[i])
            fr.write(space+lst[i] + '\n')
            space = "  "
            i += 1
            space *= pituus
            pituus -= 1


