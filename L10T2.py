
# Tee Python-ohjelma, joka laskee eri vuosina rekisteröityjen
# henkilöautojen lukumäärät annetusta tiedostosta L10T2D1.txt.
# Käytetyssä tiedostossa vuosiluku löytyy
# toisen kentän neljästä ensimmäisestä merkistä.
# Käytä laskennassa hyväksi sanakirjaa ja
# tulosta tiedot lajiteltuna vuosiluvun mukaan
# laskevaan järjestykseen esimerkkiajon mukaisesti.
# Huom. Luettavassa tiedostossa on nyt enemmän dataa,
# kuten alla olevasta tiedoston alusta näkyy.
# Jos avaat tiedoston editorilla, älä muokkaa äläkä ainakaan talleta sitä,
# sillä muutoin sen muoto saattaa muuttua ja ohjelma ei toimi.
# Mikäli ohjelmasi toimii oikein omalla koneellasi, mutta
# CodeGradessa tulee joku tiedostomuotoon liittyvä virhe,
# ota Moodlesta alkuperäisessä muodossa oleva tiedosto uudestaan
# ja varmistu, että ohjelmasi toimii oikein sen kanssa.
# Tiedostoa avatessasi käytä utf-8 –koodausta.

# Ohjelman esimerkkiajo:
# Anna luettavan tiedoston nimi: L10T2D1.txt
# Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.
# Vuosi: Autoja
# 2016: 66
# 2015: 64
# 2014: 56
# 2013: 57
# 2012: 68
# 2011: 65
# 2010: 63
# Yhteensä 439 autoa.
# Kiitos ohjelman käytöstä. 

###################################################################################
# verotiedot kirjastoon
from collections import Counter
import operator

def paaohjelma():
    lista = []
    autoSanakirja = {}

    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    # tiedostonNimi = "L10/L10T2D1.txt" # input("Anna luettavan tiedoston nimi: ")
    lista = luku(tiedostonNimi, lista)
    
   
    if len(lista) == 0:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        autoSanakirja = analysointi(lista, autoSanakirja)

        print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    
        lajiteltu = sorted(autoSanakirja.items(), key=lambda autoSanakirja:autoSanakirja[0], reverse=True)
        print("Vuosi: Autoja")
        for alkio in lajiteltu:
            print("{0:s}: {1:d}".format(alkio[0], alkio[1]))
        
        rivitYht= len(lista)
        print("Yhteensä", rivitYht, "autoa.")
        print("Kiitos ohjelman käytöstä.")



    return None

def luku(tiedostonNimi, lista):
    import sys
    
    jatka = True
    
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")  

        rivi = tiedosto.readline()

        for rivi in tiedosto:
            tietueet = rivi.split(";")
            vuosi = (tietueet[1])
            vuosiLuku = vuosi[:4]   
            lista.append(vuosiLuku)
            # print(lista)
                      
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

paaohjelma()


