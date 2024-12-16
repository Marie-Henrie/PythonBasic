##Anna pituus (cm): 170
##Anna paino (kg): 70
##Painoindeksi on 24.2(Normaali paino)
##Anna tavoiteindeksi: 22.5

##Tavoiteindeksi vastaa 5.0 kg alhaisempaa painoa.
##
##Painoindeksi x Kuvaus
##x <= 17 Vaarallinen aliravitsemus
##17 < x < 18,5 Liiallinen laihuus
##18,5 <= x < 25 Normaali paino
##25 <= x < 30 Ylipaino eli lievä lihavuus
##30 <= x < 35 Merkittävä lihavuus
##35 <= x < 40 Vaikea lihavuus
##40 <= x Sairaalloinen lihavuus 
##
##
##Kiitos ohjelman käytöstä. 



pituus = int(input("Anna pituus (cm): "))
paino = int(input("Anna paino (kg): "))

pituus1 = pituus/100

indeksi = round(paino/(pituus1*pituus1), 1)

if (indeksi <= 17):
    print("Painoindeksi on", indeksi, "(Vaarallinen aliravitsemus)")

if (17 < indeksi < 18.5):
    print("Painoindeksi on", indeksi, "(Liiallinen laihuus)")

if ( 18.5 < indeksi < 25):
    print("Painoindeksi on", indeksi, "(Normaali paino)")

if ( 25 <= indeksi < 30):
    print("Painoindeksi on", indeksi, "(Ylipaino eli lievä lihavuus)")

if (30 <= indeksi < 35):
    print("Painoindeksi on", indeksi, "(Merkittävä lihavuus)")

if (35 <= indeksi < 40):
    print("Painoindeksi on", indeksi, "(Vaikea lihavuus)")

if (indeksi >= 40):
    print("Painoindeksi on", indeksi, "(Sairaalloinen lihavuus)")
    
##print()
##print("Painoindeksi x      Kuvaus")
##print("_____________________________________________________")
##print("x <= 17             Vaarallinen aliravitsemus")
##print("17 < x < 18,5       Liiallinen laihuus")
##print("18,5 <= x < 25      Normaali paino")
##print("25 <= x < 30        Ylipaino eli lievä lihavuus")
##print("30 <= x < 35        Merkittävä lihavuus")
##print("35 <= x < 40        Vaikea lihavuus")
##print("40 <= x             Sairaalloinen lihavuus")

tavoite = float(input("Anna tavoiteindeksi: "))

tavoiteindeksi = tavoite*(pituus1*pituus1)
tulos = float(paino-tavoiteindeksi)

if(tulos>0):
    print("Tavoiteindeksi vastaa", round(tulos,1),"kg alhaisempaa painoa.")

if(tulos<0):
    print("Tavoiteindeksi vastaa", abs(round(tulos,1)),"kg suurempaa painoa.")

print("Kiitos ohjelman käytöstä.")


