

jatko=True

while True:
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut") 
    print("2) Summa")      
    print("3) Erotus")
    print("4) Tulo")
    print("5) Osamäärä")
    print("6) Potenssi")
    print("0) Lopeta")

    vastaus = int(input("Valitse toiminto (0-6): "))

    if (vastaus == 1):
        jatko=True
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))
        print("Annoit luvut", int(luku1), "ja", int(luku2))
        
    if (vastaus == 2):
        jatko=True
        summa = luku1 + luku2
        print("Summa", int(luku1), "+", int(luku2), "=",int(summa))


    elif (vastaus == 3):
        jatko=True
        erotus = luku1 - luku2
        print("Erotus", int(luku1), "-", int(luku2), "=",int(erotus))


    elif (vastaus == 4):
        jatko=True
        tulo = luku1 * luku2
        print("Tulo", int(luku1), "*", int(luku2), "=",int(tulo))



    elif (vastaus == 5):
        jatko=True
        if(luku2 != 0):
            tulos=luku1/luku2
            print("Osamäärä", int(luku1), "/", int(luku2), "=",float(round(tulos,2)))

        else:
             print("Nollalla ei voi jakaa.")          

    elif(vastaus == 6):
        jatko=True
        potenssi = luku1 ** luku2
##        muunnos=str(potenssi)
        print("Potenssi", int(luku1), "**", int(luku2), "=",int(potenssi))
##        print("Potenssi", int(luku1), "**", int(luku2), "=", muunnos[0:83])

##        sana[0:3]

    elif(vastaus<0) or (vastaus>6):
        jatko=True
        print(   "Tuntematon valinta, yritä uudestaan.")

    elif( vastaus == 0):
        
        print("Lopetetaan")
        print("Kiitos ohjelman käytöstä.")
        break

  
    

##elif (vastaus == 4):
##    if(luku2 == 0):
##        print("Nollalla ei voi jakaa.")
##    else:
##        osamaara = float(luku1) - float(luku2)
####        print("Osamäärä", luku1, "/", luku2, "=",round(osamaara, 3))
##        print("Osamäärä", luku1, "/", luku2, "=",float(round(osamaara,2)))
##
##
##else:
##    potenssi = luku1 ** luku2
##    print("Potenssi", luku1, "**", luku2, "=",potenssi)




#vastaus = input("Haluatko lopettaa ohjelman suorittamisen (k/K): ")
#if (vastaus == 'k') or (vastaus == 'K'):

#    print("Kiitos ohjelman käytöstä.")

#else:
#    nimi = input("Anna nimi: ")
#    salasana = input("Anna salasana: ")
#    if(nimi=='Matti' and salasana =='salasana'):
#        print("Käyttäjä tunnistettu.")
#    else:
#        print("Antamasi nimi oli", len(nimi), "merkkiä pitkä, mutta se tai salasana ei ollut oikein.") 


# Tiedosto: valikkorakenteista.py
# Kysytään käyttäjältä kolme syötettä ja muutetaan ne kokonaisluvuiksi

#luku = int(input("Anna kokonaisluku: "))


#if (luku < 0):

#    print("Luku on pienempi kuin 0.")


#elif (luku < 10):

#    print("Luku on pienempi kuin 10.")

#else:

#    print("Luku on suurempi tai yhtä suuri kuin 10.")
    

#if (luku% 2 == 0):

#    print("Antamasi luku on parillinen.")

#else:

#    print("Antamasi luku on pariton.")



#print("Kiitos ohjelman käytöstä.")


