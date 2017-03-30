#F0007a
szam=int(input("Add meg a számot:"))
while szam<=100:
    print(szam**2)
    szam = szam+1

#F0007b
szam=int(input("Honnan kezdjem"))
while szam<=100:
    print(szam)
    szam+=2

#F0007c:
szam=100
while szam<=1000:
    if szam%2!=0:
        print(szam)
    szam+=1
        
#F0007d:
valasz=None

while valasz!="Szeretlek":
   valasz=input("De ugye szeretsz?")

#F0007e,f,g
mettől = input('Honnan kezdve írjam ki a számokat? ')
meddig = input('Meddig írjam ki a számokat? ')
hányasával = input('Hányasával írjam ki a számokat? ')
hatványkitevő = input('Hányadik hatványukat írjam a számok mellé? ')
 
mettől = int(mettől)
meddig = int(meddig)
hányasával = int(hányasával)
hatványkitevő = int(hatványkitevő)
 
szám = mettől
 
while szám <= meddig:
    print(szám, szám**hatványkitevő)
    szám = szám + hányasával

