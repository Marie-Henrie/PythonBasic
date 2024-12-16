

##L07T3: Tiedoston rivillä olevien tietojen käsittely
##Data-tiedostoissa on useita tietoalkioita samalla rivillä
##erotettuna erotin-merkillä.
##
##Tee ohjelma, joka
##1. Lukee tiedoston rivi kerrallaan,
##tiedoston formaatti näkyy alla.
##2. Jakaa rivin erotinmerkeillä (;)
##tietoalkioihin ohjelmointioppaan luvun 6 mukaisesti split-käskyllä.
##3. Tulostaa käyttäjälle kellonajan ja
##punnitun marjan nimen alla olevan esimerkkiajon mukaisesti.
##Huomaa, että tiedostossa on otsikkorivi,
##se kannattaa lukea ensin pois ja
##käydä sen jälkeen kaikki data-rivit läpi samalla tavalla.
##Testaa ohjelmasi tiedostoilla L07T3D1.txt ja L07T3D2.txt.
##Toteuta ohjelma paaohjelma():na ja kaikki tulosteet voivat olla merkkijonoja.
##Ohjelman lukeman tiedoston muutama ensimmäistä riviä:
##
##Marja;Paino(g);Kellonaika
##vadelma;234.0;00:00
##sudenmarja;40.5;08:05
##
##Ohjelman esimerkkiajo:
##Anna tiedoston nimi: L07T3D2.txt
##Kello oli 00:00, kun punnittiin marjoja vadelma.
##Kello oli 08:05, kun punnittiin marjoja sudenmarja.
##Kello oli 11:43, kun punnittiin marjoja lakka.
##Kello oli 13:15, kun punnittiin marjoja pensasmustikka.
##Kello oli 23:59, kun punnittiin marjoja karpalo.
##Kello oli 15:03, kun punnittiin marjoja karviainen.
##Kello oli 11:11, kun punnittiin marjoja viherherukka.
##Kello oli 12:19, kun punnittiin marjoja banaani.
##Kello oli 5:15, kun punnittiin marjoja papaija.
##Kello oli 20:12, kun punnittiin marjoja tomaatti.
##Kiitos ohjelman käytöstä.
#########################################################################


#kenttaerottimena
EROTIN = ";"

#########################################################################
def paaohjelma():
    nimi = input("Anna tiedoston nimi: ")
    tiedosto = open(nimi, "r", encoding="utf-8")
##    with open(nimi) as tiedosto:
    rivi = tiedosto.readline()
##    print(rivi)
    while True:
##        for line in tiedosto:
##            next(tiedosto)
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
##            rivi = rivi[1:]
        rivi = rivi[:-1]
        sarake = rivi.split(EROTIN)
        print("Kello oli", sarake[2]+",", "kun punnittiin marjoja", sarake[0]+".")
        


    tiedosto.close()
    print("Kiitos ohjelman käytöstä.")
    return None

##def paaohjelma():
##    nimi = input("Anna tiedoston nimi: ")
##    with open(nimi) as f:
##        while True:
####            next(f)
##            for line in f:
##               
##                rivi = f.readline()
####                if (len(rivi) == 0):
####                   break
##                rivi = rivi[:-1]
##                sarake = rivi.split(EROTIN)
##                print("Kello oli", sarake[2]+",", "kun punnittiin marjoja", sarake[0]+".")             
##
##
##    f.close()
##    return None
        
paaohjelma()
#########################################################################
# eof
