
# L12T1: Henkilötunnuksen oikeellisuuden tarkastaminen
# Henkilötunnus on esimerkki koodatusta tiedosta, kuten luentojen 2 ja 3 ohjelmointivideoilla
# oli puhetta. Tee ohjelma, joka testaa onko käyttäjän antama henkilötunnus muodostettu oikein.
# Wikipedian artikkeli http://fi.wikipedia.org/wiki/Henkilötunnus kertoo, kuinka henkilötunnus
# muodostetaan ja sinun tulee toteuttaa tunnuksen tarkastus automaattisesti tietokoneohjelman
# avulla. Ohjelman tulee hyväksyä sekä isot että pienet kirjaimet syötteessä.
#
#  Ohjelman esimerkkiajo 1:
# Anna henkilötunnus: 120345-678M
# Henkilötunnus hyväksytty.
# Kiitos ohjelman käytöstä.

# Ohjelman esimerkkiajo 2:
# Anna henkilötunnus: 123456-4444
# Henkilötunnusta ei hyväksytä.
# Kiitos ohjelman käytöstä.

# hetu = "120345-678M"
hetu = input("Anna henkilötunnus: ")

# kirjaimet = kirjaimet.replace(" ", "")
# print(kirjaimet)
while True:

    if (hetu[6]== "-") or (hetu[6]== "+") or (hetu[6]== "A"):
        # print(hetu)
        # print(hetu[2]+hetu[3])
        # jako = hetu.split()
    

        pvm = int(hetu[0]+hetu[1])
        if (pvm < 32):
            # print("Henkilötunnus hyväksytty. pvm")
            
            kk = int(hetu[2]+hetu[3])
            
            if (kk < 13):
                # print("Henkilötunnus hyväksytty. kk")
                etuosa = hetu[:6]
                loppuosa = hetu[7:10]
                jakojaannos = int(etuosa+loppuosa)
                # print(etuosa, "etuosa")
                # print(loppuosa, "loppuosa")
                # print(jakojaannos)

                
                if (jakojaannos % 31 < 30):
                    kirjaimet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                    x = hetu[10]
                    # print(x)
                    if x in kirjaimet:
                        # print(x, kirjaimet)
                        print("Henkilötunnus hyväksytty.")
                        break
                    else:
                        print("Henkilötunnusta ei hyväksytä.")
                        break
                    
                    
                else:
                    print("Henkilötunnusta ei hyväksytä.")
                    break
            else:
                print("Henkilötunnusta ei hyväksytä.")
                break   
    
        else:
            print("Henkilötunnusta ei hyväksytä.")
            break
    else:
        print("Henkilötunnusta ei hyväksytä.")
        break
    
print("Kiitos ohjelman käytöstä.")

