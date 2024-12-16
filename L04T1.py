aloitusarvo = int(input("Anna aloitusarvo: "))
lopetusarvo = int(input("Anna lopetusarvo: "))
print("Toteutus for-lauseella:")
arvo1=lopetusarvo+1
for i in range(aloitusarvo,arvo1):
##    if((i%10)==0):
##        continue
    print(i, end=" ")
    
print()
print()
print("Toteutus while-lauseella:")

i=aloitusarvo
arvo=lopetusarvo+1
while(i<arvo):
    print(i, end=" ")
    i= i+1

print()
print()
print("Kiitos ohjelman käytöstä.")




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


