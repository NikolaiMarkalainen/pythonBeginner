# -*- coding: utf-8 -*-

"""
KT2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:

 Hyvä (jos arvosana oli 9 tai 10)

 Kelpo (jos 7 - 8)

 Tyydyttävä (jos 5 - 6)

 Heikko (jos 4)

 Toteuta ohjelma if-elif-else -rakenteella.

 Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

 
"""
arvosana = int(input("Syota arvosana: "))
if(arvosana >= 9 and arvosana <= 10):
    print("Hyvä")

elif(arvosana >= 7 and arvosana <= 8):
    print("Kelpo")

elif(arvosana >= 5 and arvosana <= 6):
    print("Tyydyttävä")

elif(arvosana == 4):
    print("Heikko")

else:
    print("Et antanut arvosanaa annetulta väliltä")
