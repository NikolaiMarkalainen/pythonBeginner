"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5,
niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei
luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi
annetaan LOPPU.

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana).
Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn s
aaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

"""

#Write functions here!
def LuoNimetJaArvosanat():
    nimi = ""
    arvo = 0
    data = {}
    while True:
        nimi = input("Syotä nimesi: ")
        if(nimi == 'LOPPU'):
             return nimi
             break
        elif nimi in data:
           print(nimi, " nimi on jo listalla")
           continue
        try:
            henkilo arvo = int(input("Syotä arvosana: "))
        except:
            print("Anna luku")
        if(arvo == 0):
             return nimi
        if(arvo > 5):
             arvo = 5
        if(arvo < 0):
            arvo = 0
        data[nimi] = arvo
def TulostaHylatyt(tulos):
    for nimi in tulos:
        print(*nimi, sep=", ")

def PalautaHylattyjenMaara(hylatyt):
        i = 0
        for nimi in hylatyt:
            if tulos[nimi] < 1:
                print(nimi, tulokset[nimi])
        print("Hylättyjen määrä oli: " + str(len(hylatyt)))

def TulostaKaikki(nimi, ika):
    i = 0
    while i < len(nimi):
        print(nimi[i], sep = ", ",*str(ika[i]))
        i+= 1

if __name__ == "__main__":
    #Write main program below this line
    tulos = LuoNimetJaArvosanat()
    TulostaHylatyt(tulos)
    PalautaHylattyjenMaara(tulos)