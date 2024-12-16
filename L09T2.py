

def indeksiError():
    lista = [11, 22, 33, 44, 55]
    try:
        indeksi = int(input("Anna indeksi 0-4: "))
        if (indeksi<5 or indeksi>-1):
            print("Listan arvo on", lista[indeksi], "indeksillä", str(indeksi)+".")
    except IndexError:
        print("Tuli IndexError, indeksi", str(indeksi)+".")
    return None

def nollaJakoError():
    jaettava = 4
    try:
        jakaja = int(input("Anna jakaja: "))
        jako = jaettava / jakaja
        print(str(jaettava)+"/"+str(jakaja), "on {:.2f}".format(jako)+".")
    except ZeroDivisionError as e:
        print("Tuli ZeroDivisionError, jakaja", str(jakaja)+".")
    return None

def kirjausError():
    
    try:
        luku = input("Anna numero: ")
        if (luku > 0 or luku < 1000):
            kerto = luku * luku
            print(kerto)
    except TypeError:
        print("Tuli TypeError,", luku+"*"+luku, "merkkijonoilla ei onnistunut.")
    return None

def valikko(): # Aliohjelmat määritellään ennen pääohjelmaa.
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")
    while True:
        try:
           
            valinta = int(input("Valintasi: "))
            break
        except ValueError:
            print("Anna valinta kokonaislukuna.")
    return valinta

def paaohjelma(): # Pääohjelma pidetään yksinkertaisena.
    while (True):
            valinta = valikko()
            if (valinta == 1):
                print("Valikko-ohjelma testaa ValueError'n.")
            elif (valinta == 2):
                indeksiError()
            elif (valinta == 3):
                nollaJakoError()
            elif (valinta == 4):
                kirjausError()
            elif (valinta == 0):
                break
            else:
                print("Valintaa ei tunnistettu, yritä uudestaan.")
        
##        else:
##           valinta = valikko() 
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma() # Päätasolla on vain pääohjelmakutsu.
# eof
