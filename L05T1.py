
### Tiedosto: funktio2.py
##def sano_terve(nimi, osasto, vuosikurssi):
##    print("Terve vaan " + nimi + "!")
##    print("Sanoit olevasi osastolla " + osasto + ".")
##    print("Ja että meneillään on " + vuosikurssi + ". vuosi.")
##    return None
##sano_terve("Brian", "Tite", "4" ) # Annetaan kutsussa parametreja
##
##a = "Late"
##b = "Kote"
##c = "2"
##sano_terve(a, b, c)
##
##
### Tiedosto: func_return.py
##def maksimi(x, y):
##    if (x > y):
##        isompi = x
##    else:
##        isompi = y
##    return isompi
##luku1 = 100
##luku2 = 50
##suurempi = maksimi(luku1, luku2)
##print("Suurempi arvo on", suurempi)
##
##
### Tiedosto: kyltti.py
##def tee_kyltti(teksti):
##    plakaatti = "*" * (len(teksti) + 4) + "\n"
##    plakaatti = plakaatti + "* " + teksti + " *\n"
##    plakaatti = plakaatti + "*" * (len(teksti) + 4) + "\n"
##    return plakaatti
##syote = input("Anna syöte: ")
##taulu = tee_kyltti(syote)
##print(taulu)
##
##
##print(tee_kyltti("Matti"))
##print(tee_kyltti("<3"))
##print(tee_kyltti("Mervi"))
##
##
### Tiedosto: funktio_lokaali.py
##def funktio():
##    x = 2
##    print("x funktion sisällä", x)
##    return None
##x = 50
##print("x on ennen funktiota", x)
##funktio()
##print("x on funktion kutsumisen jälkeen edelleen", x)
##print()

### Tiedosto: ohjelma_rakenne.py
##def tulosta(lkm): # Aliohjelma(t), ennen pääohjelmaa
##    print(lkm)
##    return None
##
##def paaohjelma():
##    luku = 1
##    tulosta(luku)
##    print("Kiitos ohjelman käytöstä.")
##    return None
##paaohjelma()
### eof



##print()
####def fib(maara):
####"""Tulostaa Fibonaccin lukusarjan maara ensimmäistä \n \
####jäsentä. Suositus maara < 400."""
####    uusin = 0
####    fib_luku1 = 0
####    fib_luku2 = 1
####    for i in range(0, maara):
####        uusin = fib_luku1 + fib_luku2
####        print(uusin, end = " ")
####        fib_luku2 = fib_luku1
####        fib_luku1 = uusin
####fib(11)
##
##
### Tiedosto: valikkopohjainen_ohjelma.py
##def valikko():
##    print("Käytettävissä olevat toiminnot:")
##    print("1) Tulosta 'Moi'")
##    print("2) Tulosta 'Hoi'")
##    print("0) Lopeta")
##    valinta = int(input("Valintasi: "))
##    return valinta
##
##def tulosta(sana):
##    print(sana)
##    return None
##
##def paaohjelma():
##    while (True):
##        toiminto = valikko()
##        if (toiminto == 1):
##            tulosta("Moi")
##        elif (toiminto == 2):
##            tulosta("Hoi")
##        elif (toiminto == 0):
##            print("Kiitos ohjelman käytöstä.")
##            break
##        else:
##            print("Valintaa ei tunnistettu, yritä uudestaan.")
##        print()
##    return None
##
##paaohjelma()
### eof

# L05T1: Aliohjelman 3 erilaista perusversiota 
def tulosta(): # Aliohjelma(t), ennen pääohjelmaa
    
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")
    return None

# 2. vaihe
##def kysyLuku():
##    luku = int(input("Anna luku: "))
##    print(luku)
##    return luku


def LuvunNelio():
    luku1 = luku
    print("Aliohjelmassa parametrin arvo on", luku1)
    luku2 = luku1*luku1
    print("Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen", luku2)
    return None

def kokoNimi():
    etu = etunimi
    suku = sukunimi
##    print(etu)
##    print(suku)
    print("Etunimi", "'"+ etu +"'", "ja sukunimi", "'"+ suku +"'", "muodostavat nimen", "'"+ etu + " " + suku +"'." )
##    print("Etunimi", "'"+ etu +"'")

    return None

print("Ensimmäinen vaihe:")
tulosta()
print()

print("Toinen vaihe:")

luku = int(input("Anna luku: ")) 
print("Päätasolla ennen aliohjelmaa luku on", luku)
LuvunNelio()
print("Päätasolla aliohjelman jälkeen luku on", luku)

print()
print("Kolmas vaihe:")

etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
kokoNimi()
print("Kiitos ohjelman käytöstä.")




