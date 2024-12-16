
##L08T1: Python-kirjastojen käyttö, math ja random
##
##Tee ohjelma, joka hyödyntää Pythonin eri kirjastoja eri aliohjelmissa:
##
##1. Ympyrän pinta-alan laskenta math-kirjastolla.
##Ohjelma kysyy käyttäjältä ympyrän säteen ja
##laskee sen jälkeen ympyrän pinta-alan käyttäen math-kirjastosta
##löytyvää piin arvoa (pi) sekä potenssilasku-funktiota pow.
##Tulosta lopuksi pinta-ala pyöristettynä 2 desimaalin tarkkuudella.
##
##2. Arvotun luvun arvaaminen ja random-kirjasto.
##Ohjelma arpoo luvun väliltä 0-1000 random-kirjaston
##randint-funktiolla ko. arvot mukaan lukien.
##Sen jälkeen ohjelma kysyy käyttäjältä arvausta ja kertoo,
##onko haettu luku suurempi vai pienempi niin kauan kunnes
##käyttäjä arvaa luvun oikein.
##Onnistumisesta tiedottamisen lisäksi ohjelma kertoo,
##montako arvausta käyttäjä tarvitsi oikean luvun löytämiseen.
##Muista, että nyt käytetään pseudosatunnaislukuja
##eli ne lasketaan lähtien liikkeelle siemenarvosta.
##Jotta ohjelman testaaminen olisi mahdollista,
##aseta ohjelmassasi tämä siemenluku pääohjelmassa random.seed(1) –käskyllä.
##Katso alla olevasta esimerkkiajosta ohjelman tarkempi toiminta.
##
##Toteuta molemmat toiminnot omina aliohjelminaan,
##noin 5-15 riviä per aliohjelma.
##
##Ohjelman esimerkkiajo:
##Mitä haluat tehdä:
##1) Laskea ympyrän pinta-alan
##2) Arvata luvun
##0) Lopeta Valintasi: 1
##Anna ympyrän säde kokonaislukuna: 7
##Säteellä 7 ympyrän pinta-ala on 153.94.
##
##Mitä haluat tehdä:
##1) Laskea ympyrän pinta-alan
##2) Arvata luvun
##0) Lopeta
##Valintasi: 2
##Arvaa ohjelman arpoma kokonaisluku.
##Anna kokonaisluku välillä 0-1000: 500
##Haettu luku on pienempi.
##Anna kokonaisluku välillä 0-1000: 250
##Haettu luku on pienempi.
##Anna kokonaisluku välillä 0-1000: 125
##Haettu luku on suurempi.
##Anna kokonaisluku välillä 0-1000: 150
##Haettu luku on pienempi.
##Anna kokonaisluku välillä 0-1000: 137
##Oikein! Käytit arvaamiseen 5 kierrosta.
##
##Mitä haluat tehdä:
##1) Laskea ympyrän pinta-alan
##2) Arvata luvun
##0) Lopeta Valintasi: 0
##Kiitos ohjelman käytöstä.


import math
import random
random.seed(1)
#########################################################################
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def sade():
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    ala = math.pi * math.pow(sade, 2)
    print("Säteellä", sade, "ympyrän pinta-ala on", "%.2f" % ala+".")
    return ala

def luku():
    
    luku = random.randint(0, 1000)
    arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))
    kierros = 0

    while True:
        
        if (luku > arvaus):
            print("Haettu luku on suurempi.")
            arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))
            kierros+=1
        elif (luku < arvaus):
            print("Haettu luku on pienempi.")
            arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))
            kierros+=1

        elif (luku == arvaus):
            kierros+=1

            print("Oikein! Käytit arvaamiseen", kierros, "kierrosta.")
            break


        

def paaohjelma():
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    while (True):
        toiminta = valikko()
        if (toiminta == 1):
            sade()

        elif (toiminta == 2):
            print("Arvaa ohjelman arpoma kokonaisluku.")
            luku()
      
        elif (toiminta == 0):
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    return None
paaohjelma()
#########################################################################
# eof
