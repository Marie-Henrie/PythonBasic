
EROTIN = ";"
class TUOTE:
    tunniste = ""
    tuoteLkm = 0
    hinta = 0


################################################################################

def lueLuku(tiedostonNimi, lista):

    tiedosto = open(tiedostonNimi, 'r', encoding="utf-8")

   
    x = len(tiedosto.readlines())

   
    return x

def lue(nimi, kirjoitusNimi, lista):
    tiedosto = open(nimi, 'r', encoding="utf-8")
    tiedosto_kirjoitus = open(kirjoitusNimi, "w", encoding="utf-8")

    summa = 0
    
    while (True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        rivi = rivi[:-1]
        sarake = rivi.split(EROTIN)
        tuote = TUOTE()
        tuote.tunniste = sarake[0]
        tuote.tuoteLkm = int(sarake[1])
        tuote.hinta = float(sarake[2])
        lista.append(tuote)

        for asia in lista:
           laskelma = tuote.tuoteLkm * tuote.hinta
        tiedosto_kirjoitus.write("{:.2f}\n".format(laskelma))

        summa+=laskelma
        
        
    tiedosto.close()
    tiedosto_kirjoitus.close()

    return summa      
  

def tallenna(kirjoitusNimi, lista):

    tiedosto_kirjoitus = open(kirjoitusNimi, "w", encoding="utf-8")
    for tieto in lista:
        tiedosto_kirjoitus.write(tieto)
    tiedosto_kirjoitus.close()
    return None

       

