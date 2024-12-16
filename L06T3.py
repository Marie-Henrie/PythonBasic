# L06T3: Tiedoston tietojen testaaminen, palindromit  

# Tiedosto: tiedostot.py
##
##tiedosto_luku = open("L06T3D2.txt", "r", encoding="utf-8")
##tiedosto_kirjoitus = open("L06T3T1.txt", "w", encoding="utf-8")
##
##while (True):
##    rivi = tiedosto_luku.readline()
##    if (len(rivi) == 0):
##        break
##    if (len(rivi) < 10):
##        tiedosto_kirjoitus.write(rivi)
##
##tiedosto_luku.close()
##tiedosto_kirjoitus.close()



###############################################################################



##def tallenna(nimi):
##    tiedosto = open(nimi, 'w', encoding="utf-8")
##    while (True):
##        talletus = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
##        if(talletus == "0"):
##            break
##        tiedosto.write(talletus)
##        tiedosto.write("\n")
##    tiedosto.close()
##    return None

##def lue(nimi):
##    tiedosto = open(nimi, 'r', encoding="utf-8")
##    while (True):
##        rivi = tiedosto.readline()
##        if (len(rivi) == 0):
##            break
##        rivi = rivi[:-1] # rivinvaihtomerkki pois
##        
##        sarake = rivi.split(';')
##   
##        for tiedot in sarake:
##            print(tiedot)
##
##    print("Kiitos ohjelman käytöstä.")
##    tiedosto.close()
##    return None

def palindromiJaNumero(nimi):
    tiedosto = open(nimi, 'r', encoding="utf-8")
    tiedosto_kirjoitus = open("L06T3T1.txt", "w", encoding="utf-8")
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break 
      
        
        rivi = rivi[:-1] # rivinvaihtomerkki pois

        sana = rivi[::-1] # palindromi tarkistus

        
        
        if (rivi == sana) and (rivi.isalpha()):
##            teksti = "Rivi "+"'"+str(rivi)+"'"+"on palindromi."+"\n"
            

            print("Rivi", "'"+rivi+"'", "on palindromi.")
            teksti = str(rivi)+"\n"
            tiedosto_kirjoitus.write(teksti)

        if (rivi != sana) and (rivi.isalpha()):
            print("Rivi", "'"+rivi+"'", "ei ole palindromi.")
##            teksti = "Rivi "+"'"+str(rivi)+"'"+"ei ole palindromi."+"\n"



        if (rivi.isdigit()) and (rivi.isalpha()==False):
            print("Rivi", "'"+rivi+"'", "on numerorivi.")
##            teksti = "Rivi "+"'"+str(rivi)+"'"+"on numerorivi."+"\n"


        
##        sarake = rivi.split(';')
##   
##        for tiedot in sarake:
##            print(tiedot)

    print("Kiitos ohjelman käytöstä.")
    tiedosto.close()
    tiedosto_kirjoitus.close()
    return None
    

def paaohjelma():
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = tiedostonNimi
##    lue(tiedosto)
    palindromiJaNumero(tiedosto)
##    tallenna(tiedosto)
    
    
    return None

paaohjelma()

##def kirjoita(nimi):
##    nimi = "L06T3T1.txt"
##    # kirjoita 10 numeroa tiedostoon allekkain
##    kirjoitaTiedosto = open(nimi, "w")
##    for i in range(riveja+1):
##        kirjoitaTiedosto.write(str(i) + '\n')
##    kirjoitaTiedosto.close()
##    return None
##
##def lue2(nimi):
##    tiedosto = open(nimi, "r", encoding="utf-8") #open file in read mode
## 
##    number_of_words = 0
##    number_of_lines = 0
##    number_of_characters = 0
##
##    with tiedosto as file:
##        for l in file:
##          number_of_words += len(l.split())
##          number_of_lines += 1
##          number_of_characters += len(l)
##
##    
##    tiedosto.close()
##    
##    print("Tiedostossa oli", number_of_lines, "nimeä ja", number_of_characters,"merkkiä.")
##      
##    return None
##
##def keskiarvo(nimi):
##    tiedosto = open(nimi, "r", encoding="utf-8") #open file in read mode
####     def averageLineLength(fn):
####    fn = open("Ex_file.txt", "r")
##    lines = tiedosto.readlines()
##    tiedosto.close()
##    
##
####    print(sum([len(line.strip('\n')) for line in lines]) / len(lines))
##    luku = sum([len(line.strip('\n')) for line in lines]) / len(lines)
##    print("Keskimääräinen nimen pituus oli {0:.0f}".format(luku), "merkkiä.")
##    print("Kiitos ohjelman käytöstä.")
##    return None
##
##    
##def paaohjelma():
##    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")
##    tiedosto = tiedostonNimi
##  
##    lue2(tiedosto)
##    keskiarvo(tiedosto)
##    return None
##
##
##
##paaohjelma()

#############################################################################

##sana1 = input("Anna sana 1: ")
##sana2 = input("Anna sana 2: ")
##
##
##
##
##
##if (sana1 > sana2):
##
##    print("'"+sana2+"'", "on aakkosissa aiemmin kuin", "'"+sana1+"'"+".")
##
##    
##
##if (sana1 < sana2):
##    print("'"+sana1+"'", "on aakkosissa aiemmin kuin", "'"+sana2+"'"+".")
## 
##  
##if (sana1 == sana2):
##    print("Sanat ovat samoja.")
##
##
##    
##if "z" in sana1:
##
##    print("Kirjain 'z' löytyy sanasta 1.")
##
##if "z" in sana2:
##
##    print("Kirjain 'z' löytyy sanasta 2.")
##if "z" not in sana1 and "z" not in sana2:
##    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.") 
##
##sana3 = input("Anna testattava sana: ")
##
##sana4 = sana3[::-1]
##
##
##if (sana3 == sana4):
##    print("Antamasi sana", "'"+sana3+"'", "on palindromi.")
##
##if (sana3 != sana4):
##    print("Antamasi sana ei ole palindromi.")
##    print("Se on väärinpäin", "'"+sana4+"'", "ja oikein päin", "'"+sana3+"'"+".")
##
##print("Kiitos ohjelman käytöstä.")
##
##

###############################################################################

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

