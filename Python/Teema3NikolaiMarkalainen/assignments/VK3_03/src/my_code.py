# -*- coding: utf-8 -*-

"""
KT3

Kysy käyttäjältä ensin kieli (Suomi = 0/ Englanti =1). Oletuskieli on suomi, eli muu kuin 0/1 tarkoittaa suomenkielistä tulostusta.
Määrittele koodissa viikonpäivien(ma, ti ke..) tekstit yhteen listaan, jossa on alkio/päivä eli siis molempien kielien viikonpäivänimet (esim Maanatai/Monday].
Kyse on siis rakenteesta lista listassa.

Ota käyttöön muuttuja (dictonary-tyyppinen), johon voit tallentaa maanantain ja perjantain välisenä aikana neljä mittaustulosta
jokaiselta päivältä (mittaustulos on sademäärä milleinä). Lue käyttäjältä nämä mittaustulokset ja
laske vasta lopuksi ja tulosta jokaisen päivän mittaustulosten keskiarvo yhdellä desimaalilla seuraavan esimerkin mukaisesti :

Maanantai:      12.0 mm
Tiistai:        0.0 mm
Keskiviikko:    1.9 mm
Torstai:        22.8 mm
Perjantai:      0.9 mm

Esimerkkiajo ohessa:
Millä kielellä /Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Säästetty tilaa...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm

Syötteiden järkevyydestä ei tarvitse välittää!

Ole taas huolellinen tulostusten kanssa!

"""
viikonPäivät = ['Maanantai ', 'Tiistai ', 'Keskiviikko ','Torstai ','Perjantai ',
                'Monday ', 'Tuesday ', 'Wednesday ', 'Thursday ', 'Friday ']
laskelmat = ['1. : ','2. : ','3. : ','4. : ']
sade = dict()
limit = 5
index = 0
ma=[]
ti=[]
ke=[]
to=[]
pe=[]
sade["päivät"] = viikonPäivät[0:5]
#print(sade["päivät"])
sade["days"] = viikonPäivät[5:10]
#print(sade["days"])
#print(sade["days"][0])
sade["counter"] = laskelmat[0:4]
#print(sade["counter"])
INPUT = int(input("Millä kielellä /Please choose language (0 = suomi, 1 = english): "))
if(INPUT != 1):
   while index < 5:
    for x in range(0,4):
        luku = int(input(sade["päivät"][index]+sade["counter"][x]))
        if (index == 0):
            ma.append(luku)
            sade["ma"]= ma
        if (index == 1):
            ti.append(luku)
            sade["ti"] = ti
        if (index == 2):
            ke.append(luku)
            sade["ke"] = ti
        if (index == 3):
            to.append(luku)
            sade["to"] = ti
        if (index == 4):
            pe.append(luku)
            sade["pe"] = ti
    index += 1
    if (index == 5):
        print(sade["päivät"][0],"{:.1f}".format(sum(sade["ma"]) / 4) + " mm")
        print(sade["päivät"][1], "{:.1f}".format(sum(sade["ti"]) / 4) + " mm")
        print(sade["päivät"][2], "{:.1f}".format(sum(sade["ke"])/ 4) + " mm")
        print(sade["päivät"][3], "{:.1f}".format(sum(sade["to"])/ 4) + " mm")
        print(sade["päivät"][4], "{:.1f}".format(sum(sade["pe"])/ 4) + " mm")
else:
    while index < 5:
        for x in range(0, 4):
            luku = int(input(sade["days"][index] + sade["counter"][x]))
            if (index == 0):
                ma.append(luku)
                sade["ma"] = ma
            if (index == 1):
                ti.append(luku)
                sade["ti"] = ti
            if (index == 2):
                ke.append(luku)
                sade["ke"] = ti
            if (index == 3):
                to.append(luku)
                sade["to"] = ti
            if (index == 4):
                pe.append(luku)
                sade["pe"] = ti
        index += 1
        if (index == 5):
            print(sade["days"][0], "{:.1f}".format(sum(sade["ma"]) / 4) + " mm")
            print(sade["days"][1], "{:.1f}".format(sum(sade["ti"])/ 4) + " mm")
            print(sade["days"][2], "{:.1f}".format(sum(sade["ke"])/ 4) + " mm")
            print(sade["days"][3], "{:.1f}".format(sum(sade["to"])/ 4) + " mm")
            print(sade["days"][4], "{:.1f}".format(sum(sade["pe"]) / 4) + " mm")


#for index, viikonPäivä in (zip(range(limit), viikonPäivät)):
 #   sade["päivät"] = viikonPäivä
  #  sade["päivät"] = viikonPäivä
#for viikonPäivä in viikonPäivät[5:10]:
 #   sade["days"] = viikonPäivä
  #  print(sade["days"])

    #if (index == 0):
     #   for luku in range (0,4):
      #      arvot = set()
       # while len(arvot) < 3:
        #    nro = int(input(viikonPäivä))
         #   arvot.add(nro)
          #  sade[luku] = arvot
       # print(sum(sade[luku]))
