
def bittiluku(bittijono1):
    # bittijono = input("Anna binaariluku: ")
    tulos = 0
    pituus = len(bittijono1)
    bittijono1 = bittijono1[::-1] # Bittijonoa luetaan lopusta alkuun päin
    # print("Bittijonosi on", pituus, "bittiä pitkä.")
    for i in range(0,pituus):
        if (bittijono1[i] == "1"): # Jos bitin arvo 1 eli otetaan mukaan
            tulos = tulos + 2**i # lisätään tulokseen 2^i
    # print("Bittijonosi on 10-kantaisena", tulos)
    return tulos

def erotus(luku1, luku2):
    erotus2 = luku1 - luku2
    
  
    return erotus2

def paaohjelma():

    bittijono1 = input("Anna ensimmäinen binaariluku: ")
    bittijono2 = input("Anna toinen binaariluku: ")
    tulos1 = bittiluku(bittijono1)
    tulos2 = bittiluku(bittijono2)
    print("Bittijonosi", bittijono1, "on kymmenkantaisena kokonaislukuna", tulos1) 
    print("Bittijonosi", bittijono2, "on kymmenkantaisena kokonaislukuna", tulos2) 

    lasku = erotus(tulos1, tulos2)
    print("Lukujen", tulos1, "ja", tulos2, "erotus on", lasku)
    print("Kiitos ohjelman käytöstä.")


paaohjelma()
