# L04-T4: Toistorakenteiden laajennokset

alaraja = int(input('Anna alueen alaraja: '))
ylaraja = int(input('Anna alueen yläraja: '))
ylaraja = ylaraja + 1


for i in range (alaraja, ylaraja,1):
##    print(i)
##    print("yläraja",ylaraja-1)
##   
    if (i % 5 == 0) and (i % 7 == 0):
        print('Luku', i, 'on jaollinen 5:llä ja 7:llä.')
        print('Lopetetaan etsintä.')
        print("Kiitos ohjelman käytöstä.")
        break
    if (i == (ylaraja-1)):
        print(i, 'ei ole jaollinen seitsemällä, hylätään.')
        print('Alueelta ei löytynyt sopivaa arvoa.')
        print('Kiitos ohjelman käytöstä.')
        continue
   
    if (i % 5 == 0)and (i % 7 != 0):
        print(i, 'ei ole jaollinen seitsemällä, hylätään.')   
        continue
    if (i % 5 != 0):
        print(i, 'ei ole jaollinen viidellä, hylätään.') 
        continue
  
##       
##    if (i % 5 != 0) and (i % 7 != 0):
##        print('Alueelta ei löytynyt sopivaa arvoa.')
##        print('Kiitos ohjelman käytöstä.')
 
            
##
###############################################################################





################################################################################
##a_arvo=0 #kokooja
##b_arvo=0
##jatko=True
##lkm=0
##
##a=int(input("Anna a:n arvo:  "))
##b=int(input("Anna b:n arvo:  "))
##print("a: ",a,"b: ",b)
##while True:
##    #a_arvo=a*2
##    print(a)
##    a *= a
##    b +=b
##    #b_arvo=b+100+b_arvo
##    #lkm = lkm + 1
##
##     
##    if(a>b):
##        print("Kiitos ohjelman käytöstä.")
##        break
##    if(a>10000)or (b>10000):
##        print("Kiitos ohjelman käytöstä.")
##        break
##    print("a: ",a,"b: ",b)

##    if(arvosana == -1):
##        keskiarvo=summa/lkm
##        print("Arvosanojen keskiarvo on", str(round(keskiarvo,2))+".")
##        print("Kiitos ohjelman käytöstä.")
##        break
##    if (arvosana<1) or (arvosana>5):
##        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
##        arvosana=int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): " ))
##        continue

#print("Kiitos ohjelman käytöstä.")


####################################################################################################


##aloitusarvo = int(input("Anna aloitusarvo: "))
##lopetusarvo = int(input("Anna lopetusarvo: "))
##print("Toteutus for-lauseella:")
##arvo1=lopetusarvo+1
##for i in range(aloitusarvo,arvo1):
####    if((i%10)==0):
####        continue
##    print(i, end=" ")
##    
##print()
##print()
##print("Toteutus while-lauseella:")
##
##i=aloitusarvo
##arvo=lopetusarvo+1
##while(i<arvo):
##    print(i, end=" ")
##    i= i+1
##
##print()
##print()
##print("Kiitos ohjelman käytöstä.")

##summa = 0
##for i in [0,1,2,3]:
##    luku=int(input("Anna luku: "))
##    summa=summa+luku
##print("Antamiesi lukujen summa on", summa)
##
##print("Kiitos ohjelman käytöstä.")

###tulostetaan parilliset arvot vain
##alku=int(input("Anna ensimmäinen luku: "))
##loppu=int(input("Anna loppuluku: "))
##for i in range(alku,loppu+1):
##    if((i%2)==0):
##        print(i)


### While salaman etäisyys-ohjelma
##salaman_nopeus=340
##aika=int(input("Anna kulunut aika (s): "))
##while(aika>0):
##    etaisyys=aika*salaman_nopeus/1000
##    print("Salama löi", etaisyys, "km:n päässä.")
##    aika=int(input("Anna kulunut aika (s): "))
##print("Kiitos ohjelman käytöstä.")


# Keskiarvon laskeminen

# 1. tapa
##summa=0 #kokooja
##for kurssi in [1,2,3,4,5,6,7,8]:
##    kehote="Anna "+ str(kurssi) +". arvosana: "
##    arvosana=int(input(kehote))
##    summa=summa+arvosana
##keskiarvo=summa/8
##print("Keskiarvo on", keskiarvo)


### 2. tapa
# range-funktio
##summa=0 #kokooja
##lkm=int(input("Montako arvosanaa lasketaan? " ))
##
##for kurssi in range(1, lkm+1):
##    kehote="Anna "+ str(kurssi) +". arvosana: "
##    arvosana=int(input(kehote))
##    summa=summa+arvosana
##keskiarvo=summa/lkm
##print("Keskiarvo on", keskiarvo)

### 3. tapa
### while
##summa=0 #kokooja
##kurssi=1
##lkm=int(input("Montako arvosanaa lasketaan? " ))
##while (kurssi < lkm+1):
##    kehote="Anna "+ str(kurssi) +". arvosana: "
##    arvosana=int(input(kehote))
##    summa=summa+arvosana
##    kurssi=kurssi+1
##keskiarvo=summa/lkm
##print("Keskiarvo on", keskiarvo)
##
### 4. tapa
### while
##summa=0 #kokooja
##kurssi=1
##lkm=0
##arvosana=int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa):" ))
##while (arvosana > -1):
##    summa=summa+arvosana
##    lkm = lkm + 1
##    arvosana=int(input("Anna arvosana, (-1 lopettaa): " ))
##if(lkm>0):
##    keskiarvo=summa/lkm
##    print("Keskiarvo on", round(keskiarvo,2))
##else:
##    print("Et antanut yhtään arvosanaa, 0 jako ei onnistu.")
##
##if(arvosana>=1 or arvosana<=5)
##print("Kiitos ohjelman käytöstä.")

################################################################################





##print("Laskin osaa seuraavat toiminnot:")
##jatka=True
##while jatka:
##    print("1) Summa")      
##    print("2) Erotus")
##    print("3) Tulo")
##    print("4) Osamäärä")
##    print("5) Potenssi")
##    print("6) Lopeta")
##
##    luku1 = float(input("Anna ensimmäinen luku: "))
##    luku2 = float(input("Anna toinen luku: "))
##        
##    print("Antamasi luvut ovat", int(luku1), "ja", int(luku2))
##    vastaus = int(input("Valitse toiminto (1-5): "))
##
##
##    if(vastaus == 6):
##       jatka=False
##
##      
##    elif (vastaus == 1):
##
##        summa = luku1 + luku2
##        print("Summa", int(luku1), "+", int(luku2), "=",int(summa))
##
##
##    elif (vastaus == 2):
##
##        erotus = luku1 - luku2
##        print("Erotus", int(luku1), "-", int(luku2), "=",int(erotus))
##
##
##    elif (vastaus == 3):
##
##        tulo = luku1 * luku2
##        print("Tulo", int(luku1), "*", int(luku2), "=",tulo)
##
##
##
##    elif (vastaus == 4):
##        if(luku2 != 0):
##            tulos=luku1/luku2
##            print("Osamäärä", int(luku1), "/", int(luku2), "=",float(round(tulos,2)))
##
##        else:
##             print("Nollalla ei voi jakaa.")          
##
##    elif(vastaus == 5):
##        potenssi = luku1 ** luku2
##        print("Potenssi", int(luku1), "**", int(luku2), "=",int(potenssi))
##
##   
##
##
##    else:
##        print("Toimintoa ei tunnistettu.")
##
##print("Kiitos ohjelman käytöstä.")



################################################################################


##lkm=1
##jatka=True
##while(lkm<10) and (jatka==True):
##    print("Luku on", lkm)
##    syote=input("Haluatko jatkaa k/e?: ")
##    if((syote=='e')or(syote=='E')):
##        jatka=False
##    lkm=lkm+1

##alku=1
##loppu=10
##askel=1
##
##for i in range(alku,loppu,1):
##    print(i)
##    

##for i in range(1,101):
##    if((i%10)==0):
##        continue
##    print(i)
##
##for i in range(1,101):
##    if((i%10)==0):
##        break
##    print(i)




### Tiedosto: silmukointia.py
##while (True):
##    kerroin=int(input("Anna toistojen lukumäärä (0=lopetus): "))
##    if(kerroin==0):
##        break
##    sana = input("Anna toistettava sana: ")
##    for i in range(0, kerroin):
##        print(sana)
##
##print("Ohjelman suoritus lopetettu.")


