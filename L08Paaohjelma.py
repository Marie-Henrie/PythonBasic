#########################################################################
# (c) LUT 2020 L08Paaohjelma.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin
# opiskeluun. Muu käyttö kielletty.
#########################################################################
import datetime
import L08Kirjasto
def paaohjelma():
    lista = [] # Alustuksia ja alkutoimenpiteitä
    tulokset = None
##    nimi = input("Anna luettavan datatiedoston nimi: ")
    nimi = "askelia.txt"
    alku = input("Anna ensimmäinen huomioitava päivä: ")
    loppu = input("Anna viimeinen huomioitava päivä: ")
    pvAlku = datetime.datetime.strptime(alku, "%d.%m.%Y")
    pvLoppu = datetime.datetime.strptime(loppu, "%d.%m.%Y")
    lista = L08Kirjasto.lue(lista, nimi, pvAlku, pvLoppu)
    tulokset = L08Kirjasto.analysoi(lista, tulokset)
    L08Kirjasto.tulosta(tulokset)
    return None
paaohjelma()
#########################################################################
# eof
