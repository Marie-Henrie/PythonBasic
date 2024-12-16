##L05T4: Aliohjelmarakenne, globaalit ja lokaalit tunnukset 

minimi = 5
maximi = 15

def valikko():
    teksti = input("Anna merkkijono, 5-15 merkkiä: ")
    str = teksti
    findLen(str)
    return teksti


# Python code to demonstrate string length
# using for loop

# Returns length of string
def findLen(str):
    counter = 0
   
    for i in str:
        counter += 1
    if(counter < minimi):
        print("Liian lyhyt,", counter, "merkkiä, anna uusi.")
        valikko()
    if(counter > maximi):
        print("Liian pitkä,", counter, "merkkiä, anna uusi.")
        valikko()
    if(counter >= minimi) and (counter <= maximi):
        print("Annoit sopivan merkkijonon,", counter, "merkkiä.")
        print("Kiitos ohjelman käytöstä.")
        jatka = False
    return counter

def paaohjelma():
    jatka=False
    
    while True:
        toiminta = valikko()
        if (jatka == False):
            break
 
    return None

paaohjelma()

