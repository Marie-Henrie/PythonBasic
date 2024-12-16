
##L07T2: Luokan määrittely ja olion käyttö
##Tee ohjelma, jossa on luokka ja
##demonstroi luokan käyttöä kysymällä tietoja
##sekä tulostamalla ne käyttäen hyväksi aliohjelmia.

##1. Määrittele luokka, jossa on auton merkki
##sekä autojen lukumäärä –jäsenmuuttujat.

##2. Luo paaohjelma():ssa luokasta olio,
##kutsu tiedot kysyvää aliohjelmaa ja
##välitä sille parametrina em. olio.
##Palauta olio paluuarvona paaohjelma():aan.

##3. Välitä olio tulostus-aliohjelmaan,
##joka tulostaa sen sisältämien jäsenmuuttujien arvot.
##Noudata tulosteissa esimerkkiajon muotoa.
##Ohjelman esimerkkiajo:
##    Anna automerkki: Fiat
##    Anna automerkin lukumäärä varastossa: 3
##    Varastossa on nyt Fiat-merkkisiä autoja 3 kpl.
##    Kiitos ohjelman käytöstä. 
#########################################################################


#kenttaerottimena
EROTIN = ";"

class AUTO:
    automerkki = ""
    lkm = 0
    
#########################################################################
def kysy(lista):
##    auto = AUTO()
    lista.automerkki = input("Anna automerkki: ")
    lista.lkm = int(input("Anna automerkin lukumäärä varastossa: "))
##    lista.append(lista)
    return lista

def paaohjelma():
    uusi = AUTO()
    autot = uusi
    kysy(autot)
    print("Varastossa on nyt",uusi.automerkki+"-merkkisiä autoja", uusi.lkm,"kpl.")
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()
#########################################################################
# eof
