"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:
LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän
ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU.
Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on
opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022.
Rekisteröintipäivämäärä
pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina e dellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt.
Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja
rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot.
Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
from datetime import datetime
import re
#Write functions, define global variables, and import modules here!
"""Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:
LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän 
ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU."""
def LueAutot():
    Autot = {}
    while True:
        rekisteriNumero = input("Syota auton rekisterinumero: ")
        if(rekisteriNumero == 'LOPPU'):
            break
        date_entry = str(input("Syota rekisterointipaiva  DD.MM.YYYY"))
        date_time_obj = datetime.strptime(date_entry, '%d.%m.%Y').date()
        rekisteriPäivä = date_time_obj.strftime("%d.%m.%Y")
        print(rekisteriPäivä)
        Autot[rekisteriNumero] = rekisteriPäivä
    return Autot
"""Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on 
opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022. 
Rekisteröintipäivämäärä 
pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.
"""
def TalletaTiedostoon(autot):
    with open('autot.txt', 'w') as f:
        for i in autot:
            f.write(str(i))
            f.write('\t')
            f.write(str(autot[i]))
            f.write('\n')

    """TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt.
Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja
rekisteröintipäivämäärän '\t'-merkillä erotettuna
"""
def LueTiedostosta():
    autot2 = {}
    with open('autot.txt')as f:
        a = {str(x): y for line in f for (x,y) in [line.strip().split(None,1)]}
        autot2 = a
    return autot2
    """LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen."""


def TulostaTiedot(data):
    for i in data:
        print(i,data[i])

    """TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot.
Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät."""
if __name__ == "__main__":
    auto = dict()
    auto["data"] = LueAutot()
    TalletaTiedostoon(auto["data"])
    autot2 = LueTiedostosta()
    TulostaTiedot(auto["data"])
    #Write main program below this line

    


