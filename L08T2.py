
##Ohjelman esimerkkiajo:
##Käytetään lämpötilamuunnoskirjaston versiota 1.0
##Minkä lämpötilamuunnoksen haluat tehdä?
##1) Celsius->Fahrenheit
##2) Celsius->Kelvin
##3) Fahrenheit->Kelvin
##4) Fahrenheit->Celsius
##5) Kelvin->Celsius
##6) Kelvin->Fahrenheit
##0) Lopeta
##Valintasi: 1
##Anna lähtölämpötila: 0
##Lämpötila Fahrenheit asteina: 32.0
##
##Minkä lämpötilamuunnoksen haluat tehdä?
##1) Celsius->Fahrenheit
##2) Celsius->Kelvin
##3) Fahrenheit->Kelvin
##4) Fahrenheit->Celsius
##5) Kelvin->Celsius
##6) Kelvin->Fahrenheit
##0) Lopeta Valintasi: 4
##Anna lähtölämpötila: 80
##Celsius asteina: 26.67
##
##Minkä lämpötilamuunnoksen haluat tehdä?
##1) Celsius->Fahrenheit
##2) Celsius->Kelvin
##3) Fahrenheit->Kelvin
##4) Fahrenheit->Celsius
##5) Kelvin->Celsius
##6) Kelvin->Fahrenheit
##0) Lopeta Valintasi: 6
##Anna lähtölämpötila: 293
##Lämpötila Fahrenheit asteina: 67.73
##
##Minkä lämpötilamuunnoksen haluat tehdä?
##1) Celsius->Fahrenheit
##2) Celsius->Kelvin
##3) Fahrenheit->Kelvin
##4) Fahrenheit->Celsius
##5) Kelvin->Celsius
##6) Kelvin->Fahrenheit
##0) Lopeta
##Valintasi: 0
##Kiitos ohjelman käytöstä. 

import L08T2Kirjasto

def paaohjelma():
    print("Käytetään lämpötilamuunnoskirjaston versiota", L08T2Kirjasto.versionumero)

    
    while (True):
        vastaus = L08T2Kirjasto.valikko()
        if (vastaus == 1):
            farenheit = L08T2Kirjasto.CelsiusFahrenheit()
            print("Lämpötila Fahrenheit asteina:", "%.1f" % farenheit)
            
        elif (vastaus == 2):
            kelvin = L08T2Kirjasto.CelsiusKelvin()
            print("Lämpötila Kelvin asteina:", "%.2f" % kelvin)
          
        elif (vastaus == 3):
            kelvin = L08T2Kirjasto.FahrenheitKelvin()
            print("Lämpötila Kelvin asteina:", "%.2f" % kelvin)

        elif (vastaus == 4):
            celsius = L08T2Kirjasto.FahrenheitCelsius()
            print("Lämpötila Celsius asteina:", "%.2f" % celsius)

        elif (vastaus == 5):
            celsius = L08T2Kirjasto.KelvinCelsius()
            print("Lämpötila Celsius asteina:", "%.2f" % celsius)

        elif (vastaus == 6):
            farenheit = L08T2Kirjasto.KelvinFahrenheit()
            print("Lämpötila Fahrenheit asteina:", "%.2f" % farenheit)

        elif (vastaus == 0):
           
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
        print()
    return None  

paaohjelma()


