"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

 
"""
#Write functions and define global variables here!
KR_PISTE = 90

def KysyHypynPituus():
    pituus = float(input("Mikä oli hypyn pituus:"))
    return pituus

def KysyTuomareidenPisteet():
    pisteet = list()
    while(len(pisteet) < 5):
        lst = float(input("Mitkä oli tuomareiden pisteet: "))
        if(lst > 20 or lst < 0):
            print("Väärin!")
        else:
            pisteet.append(lst)
    return pisteet

def LaskeHypynPisteet(hyppy, tuomariPisteet):
    tuomariPisteet.sort()
    uudetPisteet = (hyppy - KR_PISTE) * 1.8 + (tuomariPisteet[1]+tuomariPisteet[2]+tuomariPisteet[3]) + 60
    return uudetPisteet

if __name__ == "__main__":
    #Write main program below this line
    length = KysyHypynPituus()
    tuomariPisteet = KysyTuomareidenPisteet()
    lopputulos = LaskeHypynPisteet(length, tuomariPisteet)
    print("Hypyn pituus ", "%.1f" % length)
    print("Hypyn pisteet ", "%.1f" % lopputulos)
