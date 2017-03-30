import random
gondolt_szám=random.randrange(1,11)
kitalálta = False
elhasznált_lehetőségek = 0
 
while not kitalálta and elhasznált_lehetőségek < 3:
    tipp = int(input('Melyik számra gondoltam 1 és 10 között? '))
    elhasznált_lehetőségek += 1
    if tipp == gondolt_szám:
        kitalálta = True
    elif tipp > gondolt_szám:
        print("Tippelj nagyobbat")
    elif tipp < gondolt_szám:
        print("Tippelj kisebbet")
    else:
        print("Sajnálom, legközelebb jobban sikerül :)")
        print("Pápá")

#F0008d:
hús=False
marha=False
sonka=False
pulykahús=False
sajt=False

valasz = input("Van-e benne hús? i/n")
if valasz=="i":
    hús=True

valasz = input("Van-e benne marha? i/n")
if valasz=="i":
    marha=True

valasz = input("Van-e benne sonka? i/n")
if valasz=="i":
    sonka=True

valasz = input("Van-e benne pulykahús? i/n")
if valasz=="i":
    pulykahús=True

valasz = input("Van-e benne sajt? i/n")
if valasz=="i":
    sajt=True

if (marha or sonka) and (pulyka and sajt) and hús:
    print("Nyamnyam")
else:
    print("Nem teljes a jó szendvisz :(")

#F0008e:
szegfűbors=False
szerecsendió=False
fahéj=False

valasz = input("Van-e benne szegfűbors? i/n")
if valasz=="i":
    szegfűbors=True

valasz = input("Van-e benne szerecsendió? i/n")
if valasz=="i":
    szerecsendió=True

valasz = input("Van-e benne fahéj? i/n")
if valasz=="i":
    fahéj=True

if (not(szegfűbors and szerecsendió)) and (fahéj and szerecsendió) or (not fahéj and not szerecsendió):
    print("Nyamnyam")
else:
    print("Valami nem stimmel!")

#F0008f:
olivabogyó=False
pepperoni=False
sonka=False

valasz= input("Van-e benne olivabogyó? i/n")
if valasz== "i":
    olivabogyó=True

valasz = input("Van-e benne pepperoni? i/n")
if valasz =="i":
    pepperoni=True

valasz = input("Van-e benne sonka? i/n")
if valasz =="i":
    sonka=True

if (olivabogyó and pepperoni) and (pepperoni and not sonka) and (pepperoni and olívabogyó):
    print("Mindenki eszik")
else:
    print("Valaki éhes marad")
