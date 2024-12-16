#########################################################################
# (c) LUT 2020 L08Kirjasto.py un Kirjasto, kiintoarvot, datetime
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin
# opiskeluun. Muu käyttö kielletty.
#########################################################################
# Datatiedoston rivi: ”21-01-2017;3001;14624;10,81;16;507;346;70;26;1826”

import datetime # Kirjastojen import tiedoston alussa


PAIVIA = 7 # Kiintoarvot

PAIVAT = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
EROTIN = ';'

class DATA: # Luokat
    aika = None
    askelia = 0

class TULOKSET:
    maxAika = None
    maxAskelia = 0
    keskiarvo = 0
    viikko = []

def lue(lista, nimi, alku, loppu):
    tiedosto = open(nimi, 'r')
    while (True): # Tiedoston lukeminen ja tallennus olioina listaan
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        sarakkeet = rivi[:-1].split(EROTIN)
        aika = datetime.datetime.strptime(sarakkeet[0], "%d-%m-%Y")
        if ((aika >= alku) and (aika <= loppu)): # Haluttu aikaväli
            data = DATA()
            data.aika = aika
            data.askelia = int(sarakkeet[2]) # askeltiedot 2. sarake
            lista.append(data)
    tiedosto.close()
    return lista

def analysoi(lista, tulokset):
    viikko = []
    summa = 0
    maxAika = lista[0].aika
    maxAskelia = lista[0].askelia
    paivia = (lista[-1].aika - lista[0].aika).days

    for i in range(PAIVIA):
        viikko.append(0)
        
    for alkio in lista: # Analyysi
        summa += alkio.askelia # Keskiarvoon tarvitaan summa
        viikko[alkio.aika.weekday()] += alkio.askelia # Jakauma päiville
        if (maxAskelia < alkio.askelia): # Suurin askelmäärä ja päivä
            maxAika = alkio.aika
            maxAskelia = alkio.askelia
            
    tulokset = TULOKSET()
    tulokset.maxAika = maxAika
    tulokset.maxAskelia = maxAskelia
    tulokset.keskiarvo = int(summa / paivia)
    tulokset.viikko = viikko
    
    return tulokset

def tulosta(tulokset):
    print("Suurin askelmäärä {0:d} tuli {1:%d.%m.%Y}.".format(
    tulokset.maxAskelia, tulokset.maxAika))
    print("Keskimäärin askelia kertyi {0:d} päivässä.".format(
    tulokset.keskiarvo))
    print("Viikonpäivittäin askelet jakautuivat seuraavasti:")
    for pv in range(PAIVIA):
        print("{0:s};{1:d}".format(PAIVAT[pv], tulokset.viikko[pv]))
    print("Ohjelman suoritus päättyi {0:%d.%m.%Y} kello {0:%H:%M}.".
    format(datetime.datetime.now()))

    return None
#########################################################################
# eof
