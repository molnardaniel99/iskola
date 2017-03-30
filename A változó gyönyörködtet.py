###F0002a
""" Az egér nevet nem fogja kiírni, mivel a kutya nevű változót nem hívtuk meg"""
cica = 'kutya'
kutya = 'egér'
egér = 'cica'
print(cica)
print('kutya')
print(egér)
print('cica')

###F0002b
"""Tyúk lesz kiírva, mivel a kutya felveszi a cica nevű változó értékét"""
cica = 'kutya'
print(cica)
kutya = 'egér'
egér = 'cica'
print('kutya')
cica = 'tyúk'
print(egér)
kutya = cica
print('kutya')
print(kutya)

###F0002c
"""Összesen 11 sort és ebben 5 sor szöveg"""
print('Első sor\n')
print('\nNos?')
print('Azaz?\n')
print('\nAkkor most mennyi?\n\n')
print('Utolsó sor')

###F0002d
print("    /\n   /\n  /\n /\n/\n")

###F0002e
print("\\\n \\\n  \\\n   \\\n    \\\n")

###F0002f
print("\\    /\n \\  /\n  \\/\n")
