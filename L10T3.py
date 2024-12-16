 
#  L10T3: Tietorakenteet ja numpy-matriisin käyttö 
# Luo 4x4-kokonaislukumatriisi ja 
# alusta se nolliksi numpyn zeros-jäsenfunktiolla. 
# Sen jälkeen käy läpi matriisin kaikki alkiot kahdella silmukalla, 
# ensin rivit ja sitten sarakkeet, 
# ja sijoita matriisin jokaisen alkion arvoksi 
# aina sen sarake- ja rivi-indeksin tulo siten, 
# että sekä sarake- että rivi-indeksiin lisätään yksi 
# ettei taulukko jää suurelta osin nollille 
# (ts. (rivi-indeksi+1) * (sarakeindeksi+1), 
# ks. esimerkkituloste alla). 
# Tulosta matriisi tämän jälkeen print-käskyllä, 
# jolloin se noudattaa numpyn tarjoamaa muotoilua. 
# Tulosta sitten matriisi uudestaan riveittäin 
# sarakkeet puolipisteillä eroteltuina 
# alla olevan esimerkkiajon mukaisesti, 
# sillä tämä muoto on helppo siirtää 
# taulukkolaskentaohjelmaan visualisointia varten.  

# Ohjelman esimerkkiajo 1: 

# Tämä ohjelma esittelee numpy-matriisin käyttöä.
# Matriisi tulostettuna numpy-muotoilulla: 
# [[ 1  2  3  4]  
#  [ 2  4  6  8]  
#  [ 3  6  9 12] 
#  [ 4  8 12 16]] 
 
# Matriisi tulostettuna alkiot puolipisteillä eroteltuna: 
# 1;2;3;4; 
# 2;4;6;8; 
# 3;6;9;12; 
# 4;8;12;16;  

# Kiitos ohjelman käytöstä. 

####################################################################################################

import numpy
RIVEJA = 4
SARAKKEITA = 4

# # Matriisin luominen, 2 tapaa luoda ja alustaa, molemmissa kokonaislukuja
# matriisiA = numpy.array( # alustus halutuilla arvoilla
#    [[1,2,4],
#    [5,6,7],
#    [8,9,10]])
# #
matriisiB = numpy.zeros((RIVEJA, SARAKKEITA), int) # alustus nolliksi

# print(matriisiB)

# Matriisin alkioiden käsittely indekseillä alustamisen jälkeen
for rivi in range(RIVEJA):
   for sarake in range(SARAKKEITA):
       matriisiB[rivi][sarake] = (rivi+1) * (sarake+1)
       # (ts. (rivi-indeksi+1) * (sarakeindeksi+1)

# # Laskentaa matriiseilla numpyn avulla
# matriisiC = matriisiA + matriisiB

print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
print("Matriisi tulostettuna numpy-muotoilulla:")

# Matriisin tulostaminen numpyn avulla
print(matriisiB)
print()

# Matriisin tulostaminen indekseillä, puolipiste Excel-siirtoa varten
print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
for rivi in range(RIVEJA):
   for sarake in range(SARAKKEITA):
       print(matriisiB[rivi][sarake], end=';')
   print()


# # Matriisin tuhoaminen, rivin/sarakkeen/alkion poistaminen mahdollista
# matriisiA = numpy.delete(matriisiA, numpy.s_[:], None)

print()
print("Kiitos ohjelman käytöstä.")