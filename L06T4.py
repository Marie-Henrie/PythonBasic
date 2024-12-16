# L06T4: Tekstitiedoston tietojen tilastollinen analysointi   

def haeArvo(talletus, min_num, max_num, total):
    tiedosto_kirjoitus = open(talletus, "w", encoding="utf-8")
##    print(talletus)
##    print(total, max_num, min_num)
    print("Pienin askelmäärä oli", min_num, "askelta.")
    print("Suurin askelmäärä oli", max_num, "askelta.")
    print("Yhteensä askelia oli", total, "askelta.")
    print("Kiitos ohjelman käytöstä.")
    
    minimi = "Pienin askelmäärä oli "+ str(min_num)+ " askelta.\n"
    maximi = "Suurin askelmäärä oli "+ str(max_num)+ " askelta.\n"
    total = "Yhteensä askelia oli "+ str(total)+ " askelta."
    tiedosto_kirjoitus.write(minimi)
    tiedosto_kirjoitus.write(maximi)
    tiedosto_kirjoitus.write(total)
    tiedosto_kirjoitus.close()
    return None



def find_max(nimi):
    global max_num
    max_num = 0
    tiedosto = open(nimi, 'r', encoding="utf-8")
    for line in tiedosto:
        number = int(line.split(',')[0])
        if number > max_num:
             max_num = number
             
##    print("Suurin askelmäärä oli", max_num, "askelta.")
    tiedosto.close()
    return max_num


def find_min(nimi):
    global min_num
    min_num = 10000
    tiedosto = open(nimi, 'r', encoding="utf-8")
 
    for line in tiedosto:
        number = int(line.split(',')[0])
        if number < min_num:
             min_num = number

##    print("Pienin askelmäärä oli", min_num, "askelta.")
    tiedosto.close()
    return min_num


def summa(nimi):
    global total
    total = 0
    
    tiedosto = open(nimi, 'r', encoding="utf-8")
    tiedosto_kirjoitus = open("L06T4T1.txt", "w", encoding="utf-8")


    for line in tiedosto:
        num = int(line)
        total += num

##    print("Yhteensä askelia oli", total, "askelta.")
                    
    tiedosto.close()
    tiedosto_kirjoitus.close()
    return total



def paaohjelma():
    tiedostonNimi = input("Anna tiedot sisältävän tiedoston nimi: ")
    tiedosto = tiedostonNimi
    tallennaTiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedosto_kirjoitus = tallennaTiedostonNimi
    find_min(tiedosto)
    find_max(tiedosto)
    summa(tiedosto)
    haeArvo(tiedosto_kirjoitus, min_num, max_num, total)
        
    return None

paaohjelma()

