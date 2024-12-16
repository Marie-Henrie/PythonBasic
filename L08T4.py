

import L08T4Kirjasto
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
                tiedot = L08T4Kirjasto.lueLuku(tiedostonNimi, tiedot)
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
            
            laskutoimitus = L08T4Kirjasto.summa(luku1, luku2)
            print("Tulos lisätty listaan.")
            tulos.append(laskutoimitus)
            

        elif (vastaus == 3):
            osamaaratalletus = L08T4Kirjasto.osamaara(luku1, luku2)
            print("Tulos lisätty listaan.")

            tulos.append(osamaaratalletus)

        elif (vastaus == 0):
            L08T4Kirjasto.tallenna(kirjoitusNimi, tulos)
            print("Tallennettu tiedosto","'"+kirjoitusNimi+"'.")
            print("Kiitos ohjelman käytöstä.")
            break

  
    tiedot.clear()
    tulos.clear()
    
    return None  

 
def valikko():

    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut") 
    print("2) Summa")      
    print("3) Osamäärä")
    print("0) Lopeta")

    vastaus = int(input("Valitse toiminto (0-3): "))

    return vastaus      


paaohjelma()

