# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""
import random

f = open("arvot.txt", 'w')
x = 0
lst = []
lst2 = []
määrä = int(input("Montako lukua arvotaan? "))
with open ("tulokset.txt", 'w') as fr:
    fr.write(str("Lkm: "+ str(määrä)) + '\n')
    if (määrä < 1 or määrä > 100):
        print("Virhe!")
    else:
        print("Arvottiing seuraavat luvut ja talletetaan tiedostoon arvot.txt")
        for x in range (0,määrä):
            random_decimal = random.randint(100, 10000) / 100
            lst.append(random_decimal)
            lst2.append(random_decimal)
            f.write(str(str(random_decimal))+ '\n')
            x+=1
            if(x == määrä):
                lst.sort()
                print(*lst2, sep=" ")
                print("Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:")
                print(*lst, sep=" ")
                maxLuku = max(lst)
                minLuku = min(lst)
                kokLuku = sum(lst)
                keskiArvo = sum(lst) / 3
                kA = "{:.2f}".format(keskiArvo)
                kLuku = "{:.2f}".format(kokLuku)
                fr.write(str("Sum: " + str(kLuku)) + '\n')
                fr.write(str("Ka: " + str(kA)) + '\n')
                fr.write(str("Min: "+ str(minLuku)) + '\n')
                fr.write(str("Max: " + str(maxLuku)) + '\n')

                print("Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:")
                fr.close()
                with open ("tulokset.txt", 'r') as fin:
                    print(fin.read())


