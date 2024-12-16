# Tee ohjelma, joka lukee tiedoston, hylkää epäkelvot rivit ja moukkaa hyväksyttävissä olevat
# rivit oikeaan muotoon sekä kirjoittaa ne uuteen tiedostoon.

# Tiedostot L12T3D1.txt ja L12T3D2.txt sisältävät dataa, joiden riveillä on puolipisteillä
# erotettuna kolme tietoalkiota eli 
# kommentoijan ID, kommentti ja mainepisteet. 
# Ohjelma tarkistaa ensin, että rivillä on oikea määrä tietoalkiota 
# ja että ID on hyväksyttävä. 
# Mikäli näin ei ole, rivi hylätään ja tulostetaan hylkäyksestä kertova virheilmoitus 
# ko. rivin kanssa (ks.# esimerkkiajo). 
# Kaikki hyväksyttävät rivit kirjoitetaan uuteen tiedostoon mahdollisten
# muokkausten jälkeen, tiedoston nimi kysytään käyttäjältä.
# Tietoalkioihin liittyvät vaatimukset ovat seuraavat. 
# 
# ID on nelinumeroinen luku, esimerkiksi 0023, ja luvussa voi olla etunollia  
# Kommentti-kentässä on kommentteja,
# jotka ovat satunnaisia alfanumeerisia merkkejä eli kirjaimia ja numeroita sisältäen
# mahdollisesti myös muita eli virheellisiä merkkejä. 
# Poista kommentti-kentästä kaikki muut paitsi alfanumeeriset merkit, 
# jolloin esimerkiksi kommentista "par!si-ttu 55" tulee "parsittu55".

# Mainepisteen tulee olla kokonaisluku ja mikäli se puuttuu tai on jotain muuta, 
# korvataan se arvolla 0. Tässä tehtävässä voidaan olettaa, 
# ettei kommenteissa ole puolipisteitä eli kenttien
# erotinmerkkejä eikä rivinvaihtomerkkejä eikä keskellä tiedostoa ole tyhjiä rivejä.

# Toteuta ohjelma kolmena aliohjelmana, joista 
# ensimmäinen lukee tiedoston, 
# toinen analysoi tiedot ja 
# kolmas kirjoittaa tiedoston. 
# Näin saat ohjelmalle selkeän rakenteen ja tiedostonkäsittelyihin normaalit virheenkäsittelyt.
# Analyysiosiossa kannattaa miettiä, miten tietoalkiot on helpointa tarkistaa ja 
# korjata tarpeen mukaan. 
# Esim. kommentin virheelliset merkit voi hoitaa kopioimalla hyväksyttävät merkit 
# toiseen merkkijonoon ja jättämällä eihyväksyttävät merkit kopioimatta sinne. 
# Mainepisteiden tarkistus onnistuu esim.
# poikkeustenkäsittelyllä muutettaessa merkkijono kokonaisluvuksi.
# Kerro käyttäjälle ohjelman etenemisestä eli tulosta pääohjelmassa tilannetietona aina
# suoritettu aliohjelma ja siihen liittyvä lukumäärätieto.


# Esimerkki luettavan tiedoston alusta: 
# ID;Kommentti;Mainepisteet
# 0001;mvseibmosm5;100
# 0002;s5semh5ehse5;-42
# 0003;spmss4easm4445;

# lue ohjelma palauttaa rivit
# analysointi:
# if lauseilla 2 eri listaan , toiseen kaikki, ja toiseen hyväksytyt
# for lauseella 
    # eka tarkistus onko sarakkeita 3
    # ennen split käsittely rivinumeroiden laskuri
#     continue
#         eka if lause virheellinen
# otsikkorivi eka
# ja sitten for rivi kerranllaan

# Ohjelman esimerkkiajo 1:
# Anna luettavan tiedoston nimi: L12T3D1.txt
# Anna kirjoitettavan tiedoston nimi: L12T3T1.txt
# Tiedosto 'L12T3D1.txt' luettu, 17 riviä.
# Virheellinen ID, rivi 12: ';!fmbp-df;b'
# Virheellinen ID, rivi 13: ';;'
# Väärä määrä arvoja, rivi 14: ';'
# Väärä määrä arvoja, rivi 15: ';;;'
# Virheellinen ID, rivi 16: '99999;flipflop!!;123'
# Tiedot analysoitu, 11 hyväksyttävää tietoalkiota.
# Tiedosto 'L12T3T1.txt' kirjoitettu, 12 riviä.
# Kiitos ohjelman käytöstä.

# Ohjelman esimerkkiajo 2:
# Anna luettavan tiedoston nimi: eiole.txt
# Tiedoston 'eiole.txt' käsittelyssä virhe, lopetetaan.

import sys


################################################################################

def paaohjelma():
    tiedot = []
    tarkistus = []

    
##    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
##    kirjoitusNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    # tiedostonNimi = "eiole.txt"

    tiedostonNimi = "L12/L12T3D1.txt"
    kirjoitusNimi = "L12T3T1.txt"

    tiedot = luku(tiedostonNimi, tiedot)
    if len(tiedot) == 0:
        print("Tiedosto oli tyhjä, yhtään riviä ei tunnistettu.")
    else:
        
        print("Tiedosto", "'"+tiedostonNimi+"'", "luettu,", len(tiedot), "riviä.")
        tiedot = analysointi(tiedostonNimi, tarkistus)
       
        tarkistus = kirjoittaminen(tiedostonNimi, kirjoitusNimi, tarkistus)
        print("Tiedot analysoitu,", len(kirjoitusNimi), "hyväksyttävää tietoalkiota.") 
        print("Tiedosto",  "'"+kirjoitusNimi+"'", "kirjoitettu,", len(kirjoitusNimi)+1, "riviä.")
    
    print("Kiitos ohjelman käytöstä.")
        
    
    return None

def luku(tiedostonNimi, lista):
    import sys
    # jatka = True
    
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")
              
        for rivi in tiedosto:

            lista.append(rivi.strip())
           
        tiedosto.close()
       
    except OSError:
        print("Tiedoston","'"+tiedostonNimi+"'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return lista

def analysointi(tiedostonNimi, tarkistus):
    
    try:
        riviNro = 1
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")
        
        rivi = tiedosto.readline()
        
        for rivi in tiedosto:
            
            sarakkeet = rivi.split(";")
            riviNro += 1
            
            index_count = rivi.count(";")
            if(index_count != 2):
                print("Väärä määrä arvoja, rivi", str(riviNro)+":", "'"+str(rivi)+"'"[:-1], end="")
            else:
               
                if (len(sarakkeet[0]) != 4):
                    print("Virheellinen ID rivi", str(riviNro)+":", "'"+str(rivi)+"'"[:-1], end="")
                else:
                    sarake1 = (sarakkeet[0] + ",")
                    tarkistus.append(sarake1)

                  # A string with special characters
                    special_string = sarakkeet[1]
                    # Declaring a list
                    sample_list=[]
                    # Iterate over the string using a for loop
                    for i in special_string:
                    # Check if the character in the list is not special
                        if i.isalnum():
                    # If the character is not special, add it to list
                            sample_list.append(i)
                    # Join the elements in the list to create a string
                    normal_string="".join(sample_list)
                    sarake2 = normal_string + ","
                    tarkistus.append(sarake2)
                                                   
                    try:
                        sarake2 = int(sarakkeet[2])
                        tarkistus.append(sarake2)
                    except ValueError:
                        sarakkeet[2] = 0
                        tarkistus.append(sarakkeet[2])
                                     
        tiedosto.close()

    except OSError:
        print("Tiedoston","'"+tiedostonNimi+"'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
   
    return tarkistus


def kirjoittaminen(tiedostonNimi, kirjoitusNimi, tarkistus):
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")
        tiedostoKirjoitus = open(kirjoitusNimi, "w", encoding="utf-8")

        rivi = tiedosto.readline()
        tiedostoKirjoitus.write(rivi)

        N = 3
        M = 0

        try:
            while True:
                res = tarkistus[M:N]
                tiedostoKirjoitus.write(' '.join(map(str, res)) + "\n")
                
                if N >= len(tarkistus):
                    break
                
                M += 3
                N += 3
        finally:
            tiedosto.close()
            tiedostoKirjoitus.close()
    
   
    except OSError:

        print("Tiedoston","'"+kirjoitusNimi+"'", "käsittelyssä virhe, lopetetaan.")
        
        
        tiedosto.close()
        sys.exit(0)

    return tarkistus


paaohjelma()

