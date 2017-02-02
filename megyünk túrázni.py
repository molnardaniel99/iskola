#F0006ab
x=int(input("Egyik szám"))
y=int(input("Másik szám"))
print(min(x,y)

#F0006c
helyezes=int(input("Hanyadik helyen végeztél?"))
if helyezes == 1 or helyezes == 2 or helyezes == 3:
    print("Gratulálok! :)")
else:
    print("Ne bánkódj, fel a fejjel ;)")

#F0006d
helyezes=int(input("Hanyadik helyen végeztél?"))
if helyezes == 1:
    print("arany érem")
elif helyezes == 2:
    print("ezüst érem")
elif helyezes == 3:
    print("bronz érem")
else:
    print("legközelebb jobban sikerül!")

#F0006e
a=int(input("a értéke:"))
b=int(input("b értéke:"))
c=int(input("c értéke:"))
if a+c > b and a+b > c and b+c > a:
    print("szerkeszthető")
else:
    print("nem szerkeszthető")

#F0006g
név = input('Mi a kedves vezetékneved? ')
nem = input('Lány vagy, avagy fiú vagy-é? (l/f) ')
if nem == 'l':
    előtag = 'Ms.'
elif nem == 'f':
    előtag = 'Mr.'
else:
    print('Íly nemet sajna nem ismerek. Nem fogok rendesen köszönni.')
    előtag = 'M?.'
napszak = input('Milyen napaszak van? (r/du/e/é) ')
# r = reggel, du = délután, e = este, é = éjjel
if napszak == 'r':
    angol_napszak = 'morning'
elif napszak == 'du':
    angol_napszak = 'afternoon'
elif napszak == 'e':
    angol_napszak = 'evening'
elif napszak == 'e':
    angol_napszak = 'evening'
elif napszak == 'é':
    angol_napszak = 'nignt'
else:
    print('E napszakot sajnos nincs szerencsém ismerni. Aú! Revoár!')
    angol_napszak = 'i-don\'t-know'
print('Good ', angol_napszak, ', ', előtag, ' ', név, '!',)

#F0006h
gondolt_szám = 4
tipp = int(input('Szerinted melyik számra gondolok 1 és 5 között? '))
if gondolt_szám == tipp:
    print('Eltaláltad!')
elif tipp == gondolt_szám+1 or tipp == gondolt_szám-1:
    print('Közel voltál, de nem!')
else:
    print('Majd legközelebb!')
print('Pápá!')

#F0006i
kor=int(input("Add meg a korod:"))
if kor<6:
    print("Nézd a Piroska és a farkast!")
elif kor>6 and kor<=16:
    print("Nézd a Zootropoliszt!")
else:
    print("Bármit megnézhetsz!")
