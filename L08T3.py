
import datetime
from datetime import timedelta
  
def valikko():

    print("Mitä haluat tehdä:")
    print("1) Tunnistaa aika-olion komponentit")
    print("2) Laskea iän päivinä")
    print("3) Tulostaa viikonpäivät")
    print("4) Tulostaa kuukaudet")
    print("0) Lopeta")
    vastaus = int(input("Valintasi: "))

    return vastaus      

def aikaOlio():
    aika = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    aika1 = datetime.datetime.strptime(aika, "%d.%m.%Y %H:%M")
##    print(aika1.strftime("%m"))
    syote = datetime.datetime.strptime(aika,"%d.%m.%Y %H:%M")
    print("Annoit vuoden",syote .year)
    print("Annoit kuukauden",syote .month)
    print("Annoit päivän",syote .day)
    print("Annoit tunnin",syote .hour)
    print("Annoit minuutin",syote .minute)


##    print("Annoit vuoden", aika1.strftime("%Y"))
##    print("Annoit kuukauden", aika1.strftime("%#m"))
##    print("Annoit päivän", aika1.strftime("%#d"))
##    print("Annoit tunnin", aika1.strftime("%#H"))
##    print("Annoit minuutin", aika1.strftime("%#M")) 

    return aika1

def ika():
    ika = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
    ika1 = datetime.datetime.strptime(ika, "%d.%m.%Y")

    laskenta = "01.01.2000"
    aikaToka = datetime.datetime.strptime(laskenta, "%d.%m.%Y")
    
    erotus = aikaToka - ika1
    print("1.1.2000 sinä olit", erotus.days, "päivää vanha.")
  
    return

def viikonpaivat():
    viikko = "3.4.2023"
    vkoPvm = datetime.datetime.strptime(viikko, "%d.%m.%Y")
    vkoPvm2 = vkoPvm.strftime("%d.%m.%Y")
##    print("Annoit päivän", vkoPvm.strftime("%d"))
##    print(vkoPvm.weekday())
    viikonpaiva = vkoPvm + timedelta(days=1)
##    nextPvm = str(vkoPvm2) + datetime.timedelta(days=1)
##    print(viikonpaiva)


    oneday = datetime.timedelta(days = 1)
##    print(vkoPvm.weekday())
    if (vkoPvm.weekday() == 0):
          print("Monday")
    date_counter = 0
    for days in range(1, 7):
         date_counter += 1
         vkoPvm+= oneday
         if (vkoPvm.weekday() == 1):
             print("Tuesday")
         if (vkoPvm.weekday() == 2):
             print("Wednesday")
         if (vkoPvm.weekday() == 3):
             print("Thursday")
         if (vkoPvm.weekday() == 4):
             print("Friday")
         if (vkoPvm.weekday() == 5):
             print("Saturday")
         if (vkoPvm.weekday() == 6):
             print("Sunday")
    return

def kuukaudet():
    viikko = "10.1.2023"
    vkoPvm = datetime.datetime.strptime(viikko, "%d.%m.%Y")
    vkoPvm2 = vkoPvm.strftime("%d.%m.%Y")
##    print("Annoit päivän", vkoPvm.strftime("%d"))
##    print(vkoPvm.weekday())
##    viikonpaiva = vkoPvm + timedelta(days=30)
##    kk = vkoPvm.month
##    print(kk)
##    kuukausi = vkoPvm + timedelta(days=30)
##    print(kuukausi)
##    nextPvm = str(vkoPvm2) + datetime.timedelta(days=1)
##    print(viikonpaiva)


##    oneday = datetime.timedelta(days = 1)
##    print(vkoPvm.weekday())
##    if (vkoPvm.weekday() == 0):
##          print("Monday")
    kk = datetime.timedelta(days = 30)
    kk_counter = 0
    if (vkoPvm.month == 1):
             print("Jan")
    for days in range(0, 11):
         kk_counter += 1
         vkoPvm+= kk
         
         if (vkoPvm.month == 2):
             print("Feb")
         if (vkoPvm.month == 3):
             print("Mar")
         if (vkoPvm.month == 4):
             print("Apr")
         if (vkoPvm.month == 5):
             print("May")
         if (vkoPvm.month == 6):
             print("Jun")
         if (vkoPvm.month == 7):
             print("Jul")
         if (vkoPvm.month == 8):
             print("Aug")
         if (vkoPvm.month == 9):
             print("Sep")
         if (vkoPvm.month == 10):
             print("Oct")
         if (vkoPvm.month == 11):
             print("Nov")
         if (vkoPvm.month == 12):
             print("Dec")
   
    return

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    
    while (True):
        vastaus = valikko()
        if (vastaus == 1):
            aikaOlio()
##            aika = aikaOlio()
##            print(aika)
        elif (vastaus == 2):
            ika()
          
        elif (vastaus == 3):
            viikonpaivat()

        elif (vastaus == 4):
            kuukaudet()

        elif (vastaus == 0):
           
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
        print()
    return None  

paaohjelma()




