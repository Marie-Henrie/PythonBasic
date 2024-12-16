
# sanakirja:
# eri automerkit ja niiden esiintymät
#
# pääohjelma:
# kysy luettava tiedosto
# kysy kirjoitettava tiedosto
#
# selvitä luettavassa tiedostossa olevien eri automerkkien määrät,
# kun yhdellä rivillä on aina yhden auton merkki.
# Tulostiedostoon kirjoitetaan kukin automerkki
# yhden kerran aakkosjärjestyksessä ja
# automerkin perään tule sen esiintymiskertojen lukumäärä.
# Tässä tehtävässä kannattaa käyttää sanakirjaa eli
# dictionary –tietorakennetta ja sorted-funktiota.
# voisiko sorted-funktio toimia sanakirjan kanssa vastaavalla tavalla
# kuin tuple:n kanssa.
# Voit testata ohjelmaa edellisen viikon tiedostoilla L09T3D1.txt,
# L09T3D2.txt ja L09T3D3.txt.

# Käytä toteutuksessasi kolmea aliohjelmaa eli
# pääohjelma
#   Kysy tiedostonimet pääohjelmassa
#   ja välitä ne tiedosto-aliohjelmiin parametreina.
#   tulosten lajittelun voi tehdä tulostamisen yhteydessä.
# tiedoston luku
# analyysi
#   Varsinainen analyysi tulee tehdä analyysi-aliohjelmassa
# tiedoston kirjoitus
#   tiedostoon kirjoitetaan datasta selvitettävät asiat
#   eli automerkkien ja
#   autojen lukumäärät sekä
#   merkkikohtaiset tiedot.
#   tulosteessa auto-sanan muoto riippuu niiden lukumäärästä.
#   
# Mikäli luettava tiedosto on tyhjä,
# älä turhaan kutsu analyysi- ja kirjoitus-aliohjelmia
# vaan tulosta ilmoitus
# "Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.". 
#
##Anna luettavan tiedoston nimi: L09T3D1.txt
##Anna kirjoitettavan tiedoston nimi: L10T1T1.txt
##Tunnistettiin 8 automerkkiä ja 15 autoa:
##Kia: 2 autoa
##Mazda: 3 autoa
##Mercedes-Benz: 1 auto
##Opel: 1 auto
##Renault: 2 autoa
##Seat: 1 auto
##Toyota: 1 auto
##Volkswagen: 4 autoa
##Kiitos ohjelman käytöstä. 
#
################################################################################
import sys
def paaohjelma():
    tiedot = []
    # autot = []
    autoSanakirja = {}

    
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitusNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    # tiedostonNimi = "L09/L09T3D1.txt"
    # kirjoitusNimi = "L10T1D1.txt"

    tiedot = luku(tiedostonNimi, tiedot)
     
    if len(tiedot) == 0:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        
        autoSanakirja = analysointi(tiedot, autoSanakirja)
      
        print("Tunnistettiin", len(autoSanakirja), "automerkkiä ja",  sum(autoSanakirja.values()), "autoa:")
        
        for malli, lkm in autoSanakirja.items():
            if lkm <2:
                print(f"{malli}: {lkm} auto")
            else:
                print(f"{malli}: {lkm} autoa")

        kirjoittaminen(kirjoitusNimi, autoSanakirja)

    print("Kiitos ohjelman käytöstä.")
        
    
    return None


def luku(tiedostonNimi, lista):
    import sys
    
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")

    
        for rivi in tiedosto:

            lista.append(rivi.strip())
            # lista.append(rivi)
                      
        tiedosto.close()

                             
    except OSError:
        print("Tiedoston","'"+tiedostonNimi+"'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return lista

def analysointi(lista, autoSanakirja):
  
  
    for auto in lista:
        if auto in autoSanakirja:
           autoSanakirja[auto] += 1
        elif auto not in autoSanakirja:
            autoSanakirja[auto] = 1
        
    return autoSanakirja

def kirjoittaminen(kirjoitusNimi, autoSanakirja):

    import sys

    try:
         
        tiedosto= open(kirjoitusNimi, "w", encoding="utf-8")

        try:

            rivivaihto = "\n"

            tiedosto.write(f"Tunnistettiin {len(autoSanakirja)} automerkkiä ja {sum(autoSanakirja.values())} autoa:{rivivaihto}")
            
            for malli, lkm in autoSanakirja.items():
                if lkm <2:
                    tiedosto.write(f"{malli}: {lkm} auto{rivivaihto}")
                else:
                    tiedosto.write(f"{malli}: {lkm} autoa{rivivaihto}")

                            
        except OSError:

            print("Tiedostoon kirjoittaminen ei onnistunut.")
            
            tiedosto.close()
            
            sys.exit(0)

    except OSError:

        print("Tiedoston","'"+kirjoitusNimi+"'", "käsittelyssä virhe, lopetetaan.")
        
        sys.exit(0)
    tiedosto.close()


    return None


paaohjelma()

