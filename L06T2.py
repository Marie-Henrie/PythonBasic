# L06T2: Tiedoston rivimäärän ja merkkien laskeminen 

def lue2(nimi):
    tiedosto = open(nimi, "r", encoding="utf-8") #open file in read mode
 
    number_of_words = 0
    number_of_lines = 0
    number_of_characters = 0

    with tiedosto as file:
        for l in file:
          number_of_words += len(l.split())
          number_of_lines += 1
          number_of_characters += len(l)

    
    tiedosto.close()
    
    print("Tiedostossa oli", number_of_lines, "nimeä ja", number_of_characters,"merkkiä.")
      
    return None

def keskiarvo(nimi):
    tiedosto = open(nimi, "r", encoding="utf-8") #open file in read mode
##     def averageLineLength(fn):
##    fn = open("Ex_file.txt", "r")
    lines = tiedosto.readlines()
    tiedosto.close()
    

##    print(sum([len(line.strip('\n')) for line in lines]) / len(lines))
    luku = sum([len(line.strip('\n')) for line in lines]) / len(lines)
    print("Keskimääräinen nimen pituus oli {0:.0f}".format(luku), "merkkiä.")
    print("Kiitos ohjelman käytöstä.")
    return None

    
def paaohjelma():
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = tiedostonNimi
  
    lue2(tiedosto)
    keskiarvo(tiedosto)
    return None



paaohjelma()




### L06T2: Tiedoston rivimäärän ja merkkien laskeminen 
##
##riveja = 20
##
##def valikko():
##    print("1) Kirjoita tiedosto")
##    print("2) Lue tiedosto")
##    print("0) Lopeta")
##    valinta = int(input("Anna valintasi: "))
##    return valinta
##
####def kirjoita(nimi):
####    # kirjoita 10 numeroa tiedostoon allekkain
####    tiedosto = open(nimi, "w")
####    for i in range(riveja+1):
####        tiedosto.write(str(i) + '\n')
####    tiedosto.close()
####    return None
##
### def lue(nimi):
###     tiedosto = open(nimi, "r")
###     for i in range(riveja+1):
###         rivi = tiedosto.readline() [:-1]
###         print(rivi) # end=""
###     tiedosto.close()
###     return None
##
##def lue2(nimi):
##    tiedosto = open(nimi, "r", encoding="utf-8") #open file in read mode
##    lkm = 0
##    data = tiedosto.read() #read the content of file
##    merkit = len(data) #get the length of the data
##
##    while True:
##        rivi = tiedosto.readline() [:-1]
##        if (rivi == ""):
##            break
##        print(rivi) # end=""
##        lkm = lkm + 1
##    
##    
##    tiedosto.close()
##    
##    print("Tiedostossa oli", lkm, "nimeä ja", merkit,"merkkiä.")
##    print("Keskimääräinen nimen pituus oli 7 merkkiä.")
##    print("Kiitos ohjelman käytöstä.")
##    return None
##
##def paaohjelma():
##    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
##    tiedosto = tiedostonNimi
##   
##    lue2(tiedosto)
##    return None
##
####    print("Tämä on valikkopohjainen sovellus")
####    tiedostoNimi = "testi.txt"
####    while (True):
####        valinta = valikko()
####        if (valinta == 1):
####            kirjoita(tiedostoNimi)
####        elif (valinta == 2):
####            # lue(tiedostoNimi)
####            lue2(tiedostoNimi)
####
####        elif (valinta == 0):
####            print("Kiitos ohjelman käytöstä.")
####            break
####        else:
####            print("Tuntematon valinta, valitse uudestaan.")
##
##paaohjelma()
