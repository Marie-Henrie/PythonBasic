#Kysy haluaako käyttäjä lopettaa ohjelman suorittamisen
#ja mikäli käyttäjä antaa kirjaimen ’k’ tai ’K’
#niin lopeta ohjelman suoritus tulosteella
#”Kiitos ohjelman käytöstä.” 


vastaus = input("Haluatko lopettaa ohjelman suorittamisen (k/K): ")
if (vastaus == 'k') or (vastaus == 'K'):

    print("Kiitos ohjelman käytöstä.")

else:
    nimi = input("Anna nimi: ")
    salasana = input("Anna salasana: ")
    if(nimi=='Matti' and salasana =='salasana'):
        print("Käyttäjä tunnistettu.")
    else:
        print("Antamasi nimi oli", len(nimi), "merkkiä pitkä, mutta se tai salasana ei ollut oikein.") 


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


