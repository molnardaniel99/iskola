"""
#F0004a
név = input('Hogy híjják kendet? ')
kor = int(input('És hány éves kend? ')) # itt még stringet kapunk
korm = int(input("Milyen évet írunk?")) # átalakítjuk egész számmá, azaz int-té
születési_év = korm - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

#F0004b
név = input('Hogy híjják kendet? ')
kor = int(input('És hány éves kend? ')) # itt még stringet kapunk
korm = int(input("Milyen évet írunk?")) # átalakítjuk egész számmá, azaz int-té
születési_év = korm - kor
erettsegi = születési_év + 18
print(név, ', kend ', születési_év, '-ban született.',erettsegi, "- ban érettségizik/érettségizett")

#F0004c
x = int(input("Egyik szám:"))
y = int(input("Másik szám:"))
szorzat = x*y
print(szorzat)
"""
#F0004d
magyar_merfold = int(input("Hány magyar mérföldre van a sárkány barlangja?"))
km = magyar_merfold * 8.3536
tengeri_merfold = km / 1.852
print("Ez a táv", km, "kilómétert és", tengeri_merfold, "tengeri mérföldet jelent.") 
