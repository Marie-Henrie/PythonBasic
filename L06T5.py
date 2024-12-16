def paaohjelma():
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(tiedostonNimi, 'r', encoding="utf-8")
    

    tiedosto_kirjoitus = open("L06T5T1.txt", "w", encoding="utf-8")
    
    while (True):
        vastaus = valikko()
        if (vastaus == 1):

            luku1 = lueLuku(tiedosto)
            luku2 = lueLuku(tiedosto)
            print("Luettiin luvut", luku1, "ja", luku2)
    
        elif (vastaus == 2):
            summa(luku1, luku2)
            print("Tulos tallennettu tiedostoon.")
            summatalletus = "Summa " + str(luku1) + " " +"+ "+ str(luku2) + " = " + str(luku1+luku2)+"\n"
            tiedosto_kirjoitus.write(summatalletus)

        elif (vastaus == 3):
            osamaara(luku1, luku2)
            print("Tulos tallennettu tiedostoon.")

            osamaaratalletus = "Osamäärä " + str(luku1) + " " +"/ "+ str(luku2) + " = " + str(round((luku1/luku2),2))+"\n"
            tiedosto_kirjoitus.write(osamaaratalletus)

        elif (vastaus == 0):
            print("Lopetetaan")
            print("Kiitos ohjelman käytöstä.")
            break

    tiedosto.close()
    tiedosto_kirjoitus.close()
    return None  

def lueLuku(tiedosto):

    line = tiedosto.readline()
    
    if (len(line) > 0):
       
        luku = int(line)

    else:
        print("Luvut loppuivat, lopeta ohjelma.")
        luku = 0

    return luku
        

   
def valikko():

    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut") 
    print("2) Summa")      
    print("3) Osamäärä")
    print("0) Lopeta")

    vastaus = int(input("Valitse toiminto (0-3): "))

    return vastaus      

       
def summa(luku1, luku2):
##    print("Summa", int(luku1), "+", int(luku2), "=",int(luku1+luku2))
    return None

def osamaara(luku1, luku2):
    if(luku2 != 0):
        tulos=luku1/luku2
##        print("Osamäärä", int(luku1), "/", int(luku2), "=",float(round(tulos,2)))

    else:
        print("Nollalla ei voi jakaa.")     
        print("Summa", int(luku1), "+", int(luku2), "=",int(luku1+luku2))
    return None

paaohjelma()

