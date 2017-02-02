#F0005b
jelszó = 'KafTrU'
tipp = input('Mi a jelszó? ')
if tipp == jelszó:
    print('Bemehet.')
else:
    print('Hozzáférés megtagadva.')

#F0005c
x = int(input("Egyik szám:"))
y = int(input("Másik szám:"))
sum = x + y
tipp = int(input("Adja meg a tippet az összegre:"))
if tipp == sum:
    print("Helyes! A válasz tényleg", str(sum), "volt!")
else:
    print("Figyelj jobban! A helyes válasz pedig:", str(sum))

#F0005d
szam = int(input("Add meg a számot:"))
if szam >= 0:
    print("Természetes szám")
else:
    print("Nem természetes szám")
