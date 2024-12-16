
# L11T1: Algoritmikehitys: 
# Algoritmi neliöjuuren laskentaan 
# Ensimmäisessä tehtävä on kehittää algoritmi ja 
# ohjelma luvun neliöjuuren laskentaan. 
# Kysy ensin käyttäjältä luku. 
# Tämän jälkeen tee silmukka, jonka avulla etsit kokonaisluvun, 
# joka toiseen korotettuna on lähimpänä käyttäjän antamaa lukua. 
# Koska vastaus annetaan kokonaislukuna, 
# voi tulostuksessa olla pientä heittoa oikeaan arvoon nähden.  
# Ohjelman esimerkkiajo 1: 
# 
# Anna luku: 144 
# Neliöjuuri on 12 
# Kiitos ohjelman käytöstä. 
# Ohjelman esimerkkiajo 2: 
# 
# Anna luku: 115 
# Neliöjuuri on 11 
# Kiitos ohjelman käytöstä. 




y = -1
# tulos = 0
luku = int(input("Anna luku: "))

while True: 
    y += 1
    tulos = y ** 2
    if (tulos >= luku):
        break
    # if ((tulos == luku)):
    #     break

print("Neliöjuuri on", y)
print("Kiitos ohjelman käytöstä.")
    
   


