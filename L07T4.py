

##L07Tehtavat
##L07T4: Valikkopohjainen ohjelma, aliohjelmat, luokka, olio ja lista
##Tee valikkopohjainen ohjelma, joka pystyy

##kysymään käyttäjältä automerkkejä ja niiden myyntihintoja,
##tulostamaan kaikki annetut tiedot näytölle
##sekä lopettamaan ohjelman suorittamisen.

##Määrittele ohjelmaan luokka, jossa on kaksi jäsenmuuttujaa
##yhden auton merkkiä (merkkijono) ja
##hintaa (kokonaisluku) varten.
##Käyttäjän antaessa auton tietoja,
##välitä lista parametrinä aliohjelmaan,
##luo uusi olio ja laita käyttäjän antamat tiedot siihen
##ja lisää olio listaan sekä
##palauta lista paluuarvona kutsuvaan ohjelmaan.

##Käyttäjän valitessa tietojen tulostuksen,
##välitä lista aliohjelmaan ja tulosta tiedot siellä.
##Kun käyttäjä valitsee lopetatoiminnon,
##ohjelma tyhjentää listan ennen suorituksen päättymistä.
##Mikäli ohjelma ei tunnista käyttäjän antamaa valintaa,
##ilmoittaa se käyttäjälle tästä ilmoituksella
##"Tuntematon valinta, yritä uudestaan."

##Tietojen tulostuksessa kannattaa harjoitella format-funktion käyttöä, sillä se tarjoaa hyviä
##työkaluja tulosteiden muotoiluun niin kuin luennoilla oli puhetta. Tämän tehtävän tulosteet
##pystyy kuitenkin tekemään ihan hyvin aiemmin läpikäydyillä tulostustavoilla.
##

##Ohjelman esimerkkiajo:
##Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.
##Käytettävissä olevat toiminnot:
##
##1) Anna auton tiedot
##2) Tulosta autojen tiedot
##0) Lopeta
##Valintasi: 1
##Anna auton merkki: Audi
##Anna auton hinta: 12345
##Käytettävissä olevat toiminnot:
##1) Anna auton tiedot
##2) Tulosta autojen tiedot
##0) Lopeta
##Valintasi: 2
##Listalta löytyy seuraavat automerkit ja hinnat:
##Audi 12345
##Käytettävissä olevat toiminnot:
##1) Anna auton tiedot
##2) Tulosta autojen tiedot
##0) Lopeta
##Valintasi: 0
##Kiitos ohjelman käytöstä.



# Globaalit tunnukset. käytetään useissa aliohjelmissa, eivät muutu
#kenttaerottimena
EROTIN = ";"

class AUTO:
    merkki = ""
    hinta = 0
    


##########################################################################

# Aliohjelmat

def valikko():
##    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    print("Käytettävissä olevat toiminnot:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta


def kysy(lista):
    car = AUTO()
    car.merkki = input("Anna auton merkki: ")
    car.hinta = int(input("Anna auton hinta: "))
    lista.append(car)
    return lista

def tulosta(lista):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for car in lista:
        print("{0:s} {1:d}".format(car.merkki, car.hinta))
    return None

##def tallenna(nimi, lista):
##    tiedosto = open(nimi, "w", encoding="utf-8")
##    for hlo in lista:
##        tiedosto.write("{0:s}{1:s}{2:d}\n".format(hlo.nimi, EROTIN, hlo.pituus))
##    tiedosto.close()
##    return None
##
##def lue(nimi, lista):
##    tiedosto = open(nimi, "r", encoding="utf-8")
##    while True:
##        rivi = tiedosto.readline()
##        if (len(rivi) == 0):
##           break
##        rivi = rivi[:-1]
##        sarake = rivi.split(EROTIN)
##        hlo = HENKILO()
##        hlo.nimi = sarake[0]
##        hlo.pituus = int(sarake[1])
##        lista.append(hlo)
##    tiedosto.close()
##    return lista

def paaohjelma():
    tiedot = []
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    while True:
        toiminta = valikko()
        if (toiminta == 1):
            tiedot = kysy(tiedot)
        elif (toiminta == 2):
            tulosta(tiedot)
        elif (toiminta == 0):
            print("Kiitos ohjelman käytöstä.")
            tiedot.clear()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    return None


############################################################################
# Päätasolla oleva koodi
paaohjelma()


# eof



