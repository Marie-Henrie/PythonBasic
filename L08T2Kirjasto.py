
versionumero = 1.0     
  
def valikko():

    print("Minkä lämpötilamuunnoksen haluat tehdä?")
    print("1) Celsius->Fahrenheit")
    print("2) Celsius->Kelvin")
    print("3) Fahrenheit->Kelvin")
    print("4) Fahrenheit->Celsius")
    print("5) Kelvin->Celsius")
    print("6) Kelvin->Fahrenheit")
    print("0) Lopeta")
    vastaus = int(input("Valintasi: "))

    return vastaus      


def CelsiusFahrenheit():
    aste= int(input("Anna lähtölämpötila: "))
    farenheit = aste * 1.8 +32
##    °F = (°C) · 1,8 + 32
    return farenheit

def CelsiusKelvin():
    aste= int(input("Anna lähtölämpötila: "))
    kelvin = aste + 273.15
##    K = °C + 273,15
    return kelvin

def FahrenheitKelvin():
    aste= int(input("Anna lähtölämpötila: "))
    kelvin = (aste + 459.67) / 1.8
##    K = (°F + 459,67) / 1,8
    return kelvin

def FahrenheitCelsius():
    aste= int(input("Anna lähtölämpötila: "))
    celsius = (aste - 32) / 1.8
##    °C = (°F − 32) / 1,8
    return celsius

def KelvinCelsius():
    aste= int(input("Anna lähtölämpötila: "))
    celsius = aste - 273.15
##    °C = K − 273,15
    return celsius

def KelvinFahrenheit():
    aste= int(input("Anna lähtölämpötila: "))
    farenheit = aste * 1.8 - 459.67
##    °F = K · 1,8 − 459,67
    return farenheit
