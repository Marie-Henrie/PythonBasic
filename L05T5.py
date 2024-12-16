def paaohjelma():
    
    while (True):
        vastaus = valikko()
        if (vastaus == 1):
            
            luku1, luku2 = annaLuku()
    
        elif (vastaus == 2):
            summa(luku1, luku2)

        elif (vastaus == 3):
            osamaara(luku1, luku2)

        elif (vastaus == 0):
            print("Lopetetaan")
            print("Kiitos ohjelman käytöstä.")
            break
    return None  

def valikko():

    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut") 
    print("2) Summa")      
    print("3) Osamäärä")
    print("0) Lopeta")

    vastaus = int(input("Valitse toiminto (0-3): "))

    return vastaus      

def annaLuku():
    
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))
    print("Annoit luvut", int(luku1), "ja", int(luku2))
    
    return luku1, luku2   
       
def summa(luku1, luku2):
    print("Summa", int(luku1), "+", int(luku2), "=",int(luku1+luku2))
    return None

def osamaara(luku1, luku2):
    if(luku2 != 0):
        tulos=luku1/luku2
        print("Osamäärä", int(luku1), "/", int(luku2), "=",float(round(tulos,2)))

    else:
        print("Nollalla ei voi jakaa.")     
        print("Summa", int(luku1), "+", int(luku2), "=",int(luku1+luku2))
    return None

paaohjelma()

