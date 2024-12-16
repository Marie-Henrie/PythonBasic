print("Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.")

x = input("Anna luku 0 ja 10 väliltä: ")
luku1 = int(x)

z = input("Anna toinen luku 0 ja 10 väliltä: ")
luku2 = int(z)

w = input("Anna kolmas luku 0 ja 10 väliltä: ")
luku3 = int(w)
keskiarvo = (luku1+luku2+luku3)/3

print()

print("Antamiesi lukujen summa on", str(luku1+luku2+luku3)+".")
print("Antamiesi lukujen keskiarvo on", str((luku1+luku2+luku3)/3)+".")
print("Keskiarvo on kokonaislukuna", str(int((luku1+luku2+luku3)/3))+".")
print("Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on", str(round(keskiarvo,3))+".")
#print("Ympyrän säde on", str(sade)+",", "kehä on", 2*pii*sade, "ja pinta-ala on", str(pintaAla)+".")




print("Kiitos ohjelman käytöstä.")


#Anna luku 0 ja 10 väliltä: 7
#Anna toinen luku 0 ja 10 väliltä: 6
#Anna kolmas luku 0 ja 10 väliltä: 7

#Antamiesi lukujen summa on 20.
#Antamiesi lukujen keskiarvo on 6.666666666666667.
#Keskiarvo on kokonaislukuna 6.
#Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on 6.667.
#Kiitos ohjelman käytöstä. 
