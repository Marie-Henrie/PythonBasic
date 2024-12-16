
################################################################################



def lueLuku(tiedostonNimi, lista):

    tiedosto = open(tiedostonNimi, 'r', encoding="utf-8")

    for rivi in tiedosto:
        rivi = rivi.strip()
        lista.append(rivi)
     
        
    tiedosto.close()
    return lista
        
  

def tallenna(kirjoitusNimi, lista):

    tiedosto_kirjoitus = open(kirjoitusNimi, "w", encoding="utf-8")
    for tieto in lista:
        tiedosto_kirjoitus.write(tieto)
    tiedosto_kirjoitus.close()
    return None

       
def summa(luku1, luku2):
    summa = int(luku1) + int(luku2)
    summatalletus = "Summa " + str(luku1) + " " +"+ "+ str(luku2) + " = " + str(summa)+"\n"

    return summatalletus

def osamaara(luku1, luku2):
    luku1 = int(luku1)
    luku2 = int(luku2)
    if(luku2 != 0):
        tulos=luku1/luku2
        osamaaratalletus = "Osamäärä " + str(luku1) + " " +"/ "+ str(luku2) + " = " + str(round((luku1/luku2),2))+"\n"


    else:
        print("Nollalla ei voi jakaa.")     
    return osamaaratalletus


