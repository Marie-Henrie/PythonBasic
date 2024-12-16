import random

puolet = ("kruuna", "klaava")

def pyydä_arvaus():
    """Pyydetään pelaajaa 1 arvaamaan."""
    pyyntö = "Pelaaja 1, valitse joko kruuna tai klaava: "
    arvaus = input(pyyntö)
    while arvaus not in puolet:
        print("Arvauksesi ei ole sallittu!")
        arvaus = input(pyyntö)
    return arvaus

def päättele_jäänyt(arvaus):
    """Päätellään pelaajalle 2 jäänyt vaihtoehto."""
    päätelty = 0 if puolet.index(arvaus) == 1 else 1
    puoli = puolet[päätelty]
    return puoli

def arvo_tulos(arvaus):
    """Arvotaan lopputulos ja ilmoitetaan voittaja."""
    tulos = random.choice(puolet)
    print("Arvottiin {tulos}".format(tulos=tulos))
    if tulos == arvaus:
        print("Pelaaja 1 voittaa!")
    else:
        print("Pelaaja 2 voittaa!")

arvaus = pyydä_arvaus()
puoli = päättele_jäänyt(arvaus)
print("Pelaaja 2:lle jää {puoli}".format(puoli=puoli))
arvo_tulos(arvaus)
