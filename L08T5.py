
import L08T5Kirjasto
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
                tiedot = L08T5Kirjasto.lueLuku(tiedostonNimi, tiedot)
                
                print("Tiedosto", "'"+str(tiedostonNimi)+"' luettu,",tiedot, "riviä.")
                print()


      
        elif (vastaus == 2):
            tulokset = L08T5Kirjasto.lue(tiedostonNimi, kirjoitusNimi, tulos)
            
            print("Tiedot analysoitu, varaston arvo on", "{:.2f}".format(tulokset), "EUR." )
            print()

            

        elif (vastaus == 3):
             print("Tulokset tallennettu tiedostoon", "'"+str(kirjoitusNimi)+"'.")
             print()

        elif (vastaus == 0):

            print("Kiitos ohjelman käytöstä.")
            break


    
    return None  

 
def valikko():

    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto") 
    print("2) Analysoi tiedot")      
    print("3) Tallenna Tulokset")
    print("0) Lopeta")

    vastaus = int(input("Valintasi: "))
    
    return vastaus      


paaohjelma()

