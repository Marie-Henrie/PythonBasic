


################################################################################

def paaohjelma():
    tiedot = []

    
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    
##    tiedostonNimi = "L09/L06T5D1.txt"
##    kirjoitusNimi = "L09T1T1.txt"
    luku(tiedostonNimi, tiedot)
    kirjoitusNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoittaminen(kirjoitusNimi, tiedot)
    print("Kiitos ohjelman käytöstä.")
      
    return None

def luku(tiedostonNimi, lista):
    import sys
    indexRivi = 0
    jatka = True
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")


        for rivi in tiedosto:
                
 
            indexRivi+=1
            lista.append(rivi[:2])
        tiedosto.close()
        print("Tiedoston", "'"+tiedostonNimi+"'", "lukeminen onnistui,",indexRivi, "riviä.")


    except OSError:
        print("Tiedoston","'"+tiedostonNimi+"'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return lista


def kirjoittaminen(kirjoitusNimi, lista):

    import sys

    try:
         
        tiedosto= open(kirjoitusNimi, "w", encoding="utf-8")

        try:
            for tieto in lista:
                tiedosto.write(tieto + "\n")

        except OSError:

            print("Tiedostoon kirjoittaminen ei onnistunut.")
            
            tiedosto.close()
            
            sys.exit(0)

    except OSError:

        print("Tiedoston","'"+kirjoitusNimi+"'", "käsittelyssä virhe, lopetetaan.")
        
        sys.exit(0)
    tiedosto.close()

    print("Tiedoston", "'"+kirjoitusNimi+"'","kirjoittaminen onnistui.")

    return None


paaohjelma()

