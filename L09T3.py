import sys

################################################################################

def paaohjelma():
    tiedot = []
    autot = []

    

    tiedostonNimi = "L09/L09T3D1.txt"
    kirjoitusNimi = "L09T3D3.txt"
    tiedot = luku(tiedostonNimi, tiedot)
    if len(tiedot) == 0:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        autot = analysointi(tiedot, autot)
        print("Tiedostossa oli", len(autot), "eri automerkkiä.")
        kirjoittaminen(kirjoitusNimi, autot)
    
    print("Kiitos ohjelman käytöstä.")
        
    
    return None

def luku(tiedostonNimi, lista):
    import sys
    jatka = True
    
    try:
        tiedosto = open(tiedostonNimi, "r", encoding="utf-8")

        
        for rivi in tiedosto:

            lista.append(rivi.strip())
                  
            
        tiedosto.close()
       

        
    except OSError:
        print("Tiedoston","'"+tiedostonNimi+"'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return lista

def analysointi(lista, autot):
    vertailtava = lista[0]
    autot.clear()
    autot.append(vertailtava)

    for tieto in lista:
        if (vertailtava != tieto):
            autot.append(tieto)
            vertailtava = tieto
        
    return autot

def kirjoittaminen(kirjoitusNimi, autot):

    import sys

    try:
         
        tiedosto= open(kirjoitusNimi, "w", encoding="utf-8")

        try:
            for tieto in autot:
                tiedosto.write(tieto+ "\n")
                print(tieto)

            

        except OSError:

            print("Tiedostoon kirjoittaminen ei onnistunut.")
            
            tiedosto.close()
            
            sys.exit(0)

    except OSError:

        print("Tiedoston","'"+kirjoitusNimi+"'", "käsittelyssä virhe, lopetetaan.")
        
        sys.exit(0)
    tiedosto.close()


    return None


paaohjelma()

