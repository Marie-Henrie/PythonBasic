sana = input("Anna pitkä Sana: ")


print("Antamasi sanan viisi ensimmäistä kirjainta ovat", sana[0:5])
print("Viisi viimeistä kirjainta ovat", sana[-5:])
print("Kirjaimet 2,3,4 ja 5 ovat", sana[1:5])
print()
print("Sanan joka toinen kirjain alkaen toisesta kirjaimesta:", sana[1::2])
print()

print("Annoit sanan", "'"+sana[::]+"', joka on takaperin", "'"+sana[::-1]+"'.")
print()
x = input("Anna aloituspaikka: ")
aloitus = int(x)
y = input("Anna lopetuspaikka: ")
lopetus = int(y)
z = input("Anna siirtymä: ")
siirtyma = int(z)

print("Antamillasi asetuksilla sana", sana, "tulostuu näin:", sana[aloitus:lopetus:siirtyma])
print()
print("Sana oli",len(sana), "merkkiä pitkä.")

print("Kiitos ohjelman käytöstä.")
