

##L07T5: Valikkopohjainen ohjelma / laskin listoilla, jatkoa L06T5:lle

##Tämä tehtävä laajentaa aiemmin tehtyä laskinta, jossa valikkopohjaisen laskimen
##valintarakenne tehtiin tehtävässä L03T3, toistorakenne L04T5,
##aliohjelmarakenne L05T5 ja tiedostonkäsittely L06T5.

##Lisää L06T5 ohjelmaan kaksi listaa,
##joista yhteen luetaan kaikki tiedostosta olevat luvut ja
##toiseen listaan lisätään kaikki tulokset ohjelman aikana.
##Tämän tehtävän lähtökohtana kannattaa käyttää itse tekemääsi ohjelmaa L06T5.

##Tällä kertaa pitää muuttaa pääohjelmaa ja
##luvut tiedostosta lukevaa aliohjelmaa sekä
##lisätä tulokset tiedostoon tallentava uusi aliohjelma.

##Pääohjelmassa kysytään nyt luettavan ja
##kirjoittavan tiedoston nimet sekä
##määritellään kaksi listaa.

##Kun käyttäjä antaa ohjelmalle luvut laskentaa varten ensimmäistä kertaa,
##ohjelma lukee kaikki tiedostossa olevat luvut,
##laittaa ne listaan ja sijoittaa kahdella ensimmäisellä rivillä
##olleet luvut laskettaviksi luvuiksi.

##Jatkossa käyttäjän pyytäessä uusia lukuja tiedostoa ei enää lueta
##vaan seuraavat luvut ovat listan kaksi seuraavaa alkiota
##niin kauan kuin listassa on lukuja.
##Voimme olettaa, että tiedostossa on parillinen määrä lukuja,
##jolloin listasta saadaan luettua aina kaksi lukua.

##Ohjelman pitää tietää listalla olevien lukujen määrä sekä
##seuraavan luvun indeksi listalla,
##jotta ohjelma pystyy käymään läpi kaikki listan alkiot ja
##osaa lopettaa sopivalla hetkellä.

##Laskutoimituksen jälkeen tulos laitetaan tulos-listaan merkkijonona.
##Kun käyttäjä lopettaa ohjelman,
##talleta tämä lista omassa aliohjelmassa tiedostoon,
##jonka jälkeen molemmat listat
##voidaan tyhjentää ja ohjelma lopettaa normaalisti.
##Huomaa, että edellisen viikon tehtävästä poiketen
##voimme nyt listojen avulla toteuttaa kaikki tiedostoihin liittyvät toimenpiteet
##aina yhdessä luku- tai kirjoitusaliohjelmassa tiedostonimen ja listan avulla.
##Moodlessa on tiedostot L06T5D1.txt ja L06T5D2.txt,
##joissa on erilaiset syötteet ohjelmalle ja
##ohjelman esimerkkitallenne L06T5T1.txt.
##Molempien tiedostojen muoto on sama kuin L06.



##Ohjelman esimerkkiajo:
##Anna luettavan tiedoston nimi: L06T5D2.txt
##Anna kirjoitettavan tiedoston nimi: L06T5T1.txt
##Tämä laskin osaa seuraavat toiminnot:
##1) Anna luvut
##2) Summa
##3) Osamäärä
##0) Lopeta
##Valitse toiminto (0-3): 1
##Luettu tiedosto 'L06T5D2.txt'.
##Luettiin luvut 1 ja 2
##Tämä laskin osaa seuraavat toiminnot:
##1) Anna luvut
##2) Summa
##3) Osamäärä
##0) Lopeta
##Valitse toiminto (0-3): 2
##Tulos lisätty listaan.
##Tämä laskin osaa seuraavat toiminnot:
##1) Anna luvut
##2) Summa
##3) Osamäärä
##0) Lopeta
##Valitse toiminto (0-3): 1
##Luvut loppuivat, lopeta ohjelma.
##Tämä laskin osaa seuraavat toiminnot:
##1) Anna luvut
##2) Summa
##3) Osamäärä
##0) Lopeta
##Valitse toiminto (0-3): 0
##Tallennettu tiedosto 'L06T5T1.txt'.
##Kiitos ohjelman käytöstä.

################################################################################

def paaohjelma():
    tiedot = []
    tulos = []
    indexMax = -2
    indexRivi = 0
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitusNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    
    while (True):
        vastaus = valikko()
        if (vastaus == 1):

            if(indexMax == -2):
                tiedot = lueLuku(tiedostonNimi, tiedot)
                print("Luettu tiedosto", "'"+str(tiedostonNimi)+"'.")
                indexMax = len(tiedot)-1
            else:
                indexRivi+=1

            if(indexRivi > indexMax):
                print("Luvut loppuivat, lopeta ohjelma.")
            else:
                luku1 = tiedot[indexRivi]
                indexRivi+=1
                luku2 = tiedot[indexRivi]
                print("Luettiin luvut", luku1, "ja", luku2)

           

    
        elif (vastaus == 2):
            
            laskutoimitus = summa(luku1, luku2)
            print("Tulos lisätty listaan.")
            tulos.append(laskutoimitus)
            

        elif (vastaus == 3):
            osamaaratalletus = osamaara(luku1, luku2)
            print("Tulos lisätty listaan.")

            tulos.append(osamaaratalletus)

        elif (vastaus == 0):
            tallenna(kirjoitusNimi, tulos)
            print("Tallennettu tiedosto","'"+kirjoitusNimi+"'.")
            print("Kiitos ohjelman käytöstä.")
            break

  
    tiedot.clear()
    tulos.clear()
    
    return None  

def lueLuku(tiedostonNimi, lista):

    tiedosto = open(tiedostonNimi, 'r', encoding="utf-8")

    for rivi in tiedosto:
        rivi = rivi.strip()
        lista.append(rivi)
     
        
    tiedosto.close()
    return lista
        
  
def valikko():

    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut") 
    print("2) Summa")      
    print("3) Osamäärä")
    print("0) Lopeta")

    vastaus = int(input("Valitse toiminto (0-3): "))

    return vastaus      


def tallenna(kirjoitusNimi, lista):

    tiedosto_kirjoitus = open(kirjoitusNimi, "w", encoding="utf-8")
    for tieto in lista:
        tiedosto_kirjoitus.write(tieto)
    tiedosto_kirjoitus.close()
    return None

       
def summa(luku1, luku2):
    summa = int(luku1) + int(luku2)
    summatalletus = "Summa " + str(luku1) + " " +"+ "+ str(luku2) + " = " + str(summa)+"\n"

    return summatalletus

def osamaara(luku1, luku2):
    luku1 = int(luku1)
    luku2 = int(luku2)
    if(luku2 != 0):
        tulos=luku1/luku2
        osamaaratalletus = "Osamäärä " + str(luku1) + " " +"/ "+ str(luku2) + " = " + str(round((luku1/luku2),2))+"\n"


    else:
        print("Nollalla ei voi jakaa.")     
    return osamaaratalletus

paaohjelma()

