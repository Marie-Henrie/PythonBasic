#L06T1: Tekstitiedoston kirjoittaminen ja lukeminen 

# L06T1: Tekstitiedoston kirjoittaminen ja lukeminen
# Harjoitellaan tiedoston kirjoittamista ja lukemista aliohjelmissa.
# 1. Tee kolmesta aliohjelmasta muodostuva ohjelma luentokalvojen valikkopohjaisen
# ohjelman tyyliin. Nyt tarvittavat ohjelmat ovat paaohjelma, TiedostoKirjoita ja
# TiedostoLue. Kysy pääohjelmassa tallennettavan tiedoston nimi ja välitä se parametrina
# molempiin aliohjelmiin.

# 2. Tiedon kirjoitus -aliohjelman tulee kysyä käyttäjältä nimi ja tallentaa sen
# tekstitiedostoon. Kysy nimi toistorakenteessa ja lopeta kysyminen, kun käyttäjä antaa
# syötteeksi 0:n (ts. numerosta nolla muodostuva merkkijono). Tiedosto tulee avata
# aliohjelman alussa ja mahdollinen aiempi tiedoston sisältö tulee tuhota avauksen
# yhteydessä. Aliohjelman lopuksi tiedosto tulee sulkea.

# 3. Tiedoston luku -aliohjelmalla varmistetaan, että tiedostossa on haluttu sisältö. Avaa
# tiedosto, lue sen sisältö ja tulosta näytölle yksi nimi riville sekä lopuksi sulje tiedosto.
# Huomaa, että tässä tehtävässä pitää toteuttaa oikein toistorakenne (L04), aliohjelmat (L05) ja
# tiedostonkäsittely (L06). Virhe missä tahansa näistä kohdista estää ohjelman oikean
# toiminnan, joten tarkista em. rakenteet aiemmilta viikoilta tarpeen mukaan.
# Ohjelman esimerkkiajo:

# Anna tallennettavan tiedoston nimi: L06T1T1.txt
# Anna tiedostoon tallennettava nimi (0 lopettaa): Ville
# Anna tiedostoon tallennettava nimi (0 lopettaa): Kalle
# Anna tiedostoon tallennettava nimi (0 lopettaa): Joonatan
# Anna tiedostoon tallennettava nimi (0 lopettaa): 0
# Tiedostoon 'L06T1T1.txt' on tallennettu seuraavat nimet:
# Ville
# Kalle
# Joonatan
# Kiitos ohjelman käytöstä.

#########################################################################

# def valikko():
#     print("Mitä haluat tehdä:")
#     print("1) Tallenna tiedosto")
#     print("2) Lue tiedosto")
#     print("0) Lopeta")
#     valinta = int(input("Valintasi: "))
#     return valinta

def tallenna(nimi):
    tiedosto = open(nimi, 'w', encoding="utf-8")
    while (True):
        talletus = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
        if(talletus == "0"):
            break
        tiedosto.write(talletus)
        tiedosto.write("\n")
    tiedosto.close()
    return None

def lue(nimi):
    tiedosto = open(nimi, 'r', encoding="utf-8")
    print("Tiedostoon ", "'"+nimi+"'", "on tallennettu seuraavat nimet:")
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        rivi = rivi[:-1] # rivinvaihtomerkki pois
        
        sarake = rivi.split(';')
   
        for tiedot in sarake:
            print(tiedot)

 ##     print("Tiedostoon ", nimi, "on tallennettu seuraavat nimet:  '"+sarake[0]+"' ja '"+sarake[1]+"'.")
    print("Kiitos ohjelman käytöstä.")
    tiedosto.close()
    return None


def paaohjelma():
    tiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedosto = tiedostonNimi
    tallenna(tiedosto)
    lue(tiedosto)
    # while (True):
    #     toiminto = valikko()
    #     if (toiminto == 1):
    #         tallenna(tiedosto)
    #     elif (toiminto == 2):
    #         lue(tiedosto)
    #     elif (toiminto == 0):
    #         print("Kiitos ohjelman käytöstä.")
    #         break
    #     else:
    #         print("Valintaa ei tunnistettu, yritä uudestaan.")
    #     print()
    return None

paaohjelma()
#########################################################################
# eof



##def valikko():
##    print("Mitä haluat tehdä:")
##    print("1) Tallenna tiedosto")
##    print("2) Lue tiedosto")
##    print("0) Lopeta")
##    valinta = int(input("Valintasi: "))
##    return valinta
##
##def tallenna(nimi):
##    tiedosto = open(nimi, 'w', encoding="utf-8")
##    while (True):
##        talletus = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
##        if(talletus == "0"):
##            break
##        tiedosto.write(talletus)
##        tiedosto.write("\n")
##    tiedosto.close()
##    return None
##
##def lue(nimi):
##    tiedosto = open(nimi, 'r', encoding="utf-8")
##    while (True):
##        rivi = tiedosto.readline()
##        if (len(rivi) == 0):
##            break
##        rivi = rivi[:-1] # rivinvaihtomerkki pois
##        sarake = rivi.split(';')
##        
##        for tiedot in sarake:
##            print(tiedot)
##
## ##     print("Tiedostoon ", nimi, "on tallennettu seuraavat nimet:  '"+sarake[0]+"' ja '"+sarake[1]+"'.")
##
##    tiedosto.close()
##    return None
##
##
####rivi = "Ville;Vallaton;0404567890"
####tiedot = rivi.split(';')
####print(tiedot)
####for alkio in tiedot:
####  print(alkio)
##
##def paaohjelma():
##    tiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
##    tiedosto = tiedostonNimi
##    while (True):
##        toiminto = valikko()
##        if (toiminto == 1):
##            tallenna(tiedosto)
##        elif (toiminto == 2):
##            lue(tiedosto)
##        elif (toiminto == 0):
##            print("Kiitos ohjelman käytöstä.")
##            break
##        else:
##            print("Valintaa ei tunnistettu, yritä uudestaan.")
##        print()
##    return None
##
##paaohjelma()
###########################################################################
### eof
##






###Esimerkki 6.2. Tiedoston avaaminen, kirjoittaminen ja lukeminen
### Tiedosto: tiedostot.py
##tiedosto_luku = open("data.txt", "r", encoding="utf-8")
##
##tiedosto_kirjoitus = open("lyhyet.txt", "w", encoding="utf-8")
##
##
##while (True):
##    rivi = tiedosto_luku.readline()
##
##    if (len(rivi) == 0):
##
##        break
##
##    if (len(rivi) < 10):
##        tiedosto_kirjoitus.write(rivi)
##
##tiedosto_luku.close()
##tiedosto_kirjoitus.close()

##
###Esimerkki 6.3. Merkkijonojen muokkailua
### Tiedosto: mjonot.py
##mjono1 = "Tässä on meille tekstiä. "
##mjono2 = input("Anna merkkijono: ")
##print(mjono1, mjono2)
##print(mjono1.strip(), mjono2)
##print(mjono1.upper(), mjono2.upper())
##if (mjono2.isalpha()):
##    print("mjono2 käsittää vain kirjaimia.")
##print("mjono1 jaettuna välilyöntien kohdalta listaksi:", mjono1.split())