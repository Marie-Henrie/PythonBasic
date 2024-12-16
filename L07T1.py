

#########################################################################
def valikko():
    print("Voit valita alla olevista toiminnoista:")
    print("1) Lisää")
    print("2) Poista")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def lisaa(lista):
    lisaaTuote = input("Anna lisättävä tuote: ")
    lista.append(lisaaTuote)
    return lista

def poista(lista):
    print("Ostoslistassasi on", len(lista), "tuotetta.")
    poistaTuote = int(input("Anna poistettavan tuotteen järjestysnumero: "))
    del lista[poistaTuote-1]
    return lista

def paaohjelma():
    ostoslista = []
    tiedosto = "L07Demo.txt"
    while (True):
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        print(ostoslista)
        toiminta = valikko()
        if (toiminta == 1):
            ostoslista = lisaa(ostoslista)
        elif (toiminta == 2):
            poista(ostoslista)
        elif (toiminta == 0):
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            print(ostoslista)
            print("Kiitos ohjelman käytöstä.")
            ostoslista.clear()
            break
        else:
            print("Tunnistamaton valinta.")
        print()
    return None
paaohjelma()
#########################################################################
# eof
