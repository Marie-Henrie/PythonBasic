
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")





if (sana1 > sana2):

    print("'"+sana2+"'", "on aakkosissa aiemmin kuin", "'"+sana1+"'"+".")

    

if (sana1 < sana2):
    print("'"+sana1+"'", "on aakkosissa aiemmin kuin", "'"+sana2+"'"+".")
 
  
if (sana1 == sana2):
    print("Sanat ovat samoja.")


    
if "z" in sana1:

    print("Kirjain 'z' löytyy sanasta 1.")

if "z" in sana2:

    print("Kirjain 'z' löytyy sanasta 2.")
if "z" not in sana1 and "z" not in sana2:
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.") 

sana3 = input("Anna testattava sana: ")

sana4 = sana3[::-1]


if (sana3 == sana4):
    print("Antamasi sana", "'"+sana3+"'", "on palindromi.")

if (sana3 != sana4):
    print("Antamasi sana ei ole palindromi.")
    print("Se on väärinpäin", "'"+sana4+"'", "ja oikein päin", "'"+sana3+"'"+".")

print("Kiitos ohjelman käytöstä.")


##print("Laskin osaa seuraavat toiminnot:")
##print("1) Summa")      
##print("2) Erotus")
##print("3) Tulo")
##print("4) Osamäärä")
##print("5) Potenssi")
##
##print("Antamasi luvut ovat", int(luku1), "ja", int(luku2))
##vastaus = int(input("Valitse toiminto (1-5): "))
##
##if (vastaus == 1):

##    summa = luku1 + luku2
##    print("Summa", int(luku1), "+", int(luku2), "=",int(summa))

##
##elif (vastaus == 2):

##    erotus = luku1 - luku2
##    print("Erotus", int(luku1), "-", int(luku2), "=",int(erotus))

##
##elif (vastaus == 3):

##    tulo = luku1 * luku2
##    print("Tulo", int(luku1), "*", int(luku2), "=",tulo)

##
##
##elif (vastaus == 4):
##    if(luku2 != 0):
##        tulos=luku1/luku2
##        print("Osamäärä", int(luku1), "/", int(luku2), "=",float(round(tulos,2)))
##
##    else:
##         print("Nollalla ei voi jakaa.")          
##
##elif(vastaus == 5):
##    potenssi = luku1 ** luku2
##    print("Potenssi", int(luku1), "**", int(luku2), "=",int(potenssi))

##
##else:
##    print("Toimintoa ei tunnistettu.")
##    
##print("Kiitos ohjelman käytöstä.")
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


