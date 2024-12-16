x = input("Anna positiivinen kokonaisluku: ")
luku = int(x)


print("Luku", luku, "kerrottuna itsellään on", luku*luku)


y = input("Anna ympyrän säteen pituus kokonaislukuna: ")
sade = int(y)
pii = float(3.14)
pintaAla = pii*sade*sade

print("Ympyrän säde on", str(sade)+",", "kehä on", 2*pii*sade, "ja pinta-ala on", str(pintaAla)+".")

z = input("Anna suorakulmion yhden sivun pituus kokonaislukuna: ")
pituus1 = int(z)

w = input("Anna suorakulmion toisen sivun pituus kokonaislukuna: ")
pituus2 = int(w)

print("Suorakulmion sivut ovat", pituus1,"ja",str(pituus2)+";", end="")
print(" kehä on", str((pituus1+pituus1+pituus2+pituus2))+';', end="")
print(" ja pinta-ala on",  str(pituus1*pituus2)+".")






print("Kiitos ohjelman käytöstä.")
