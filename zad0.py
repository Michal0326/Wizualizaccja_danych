import random
import math

a=[1-x for x in range(1,11)]
print(a)

b=[4**i for i in range(0,8)]
print(b)

c=[x for x in b if x%2==0]
print(c)

lista=[random.randint(1, 100) for r in range(1,11)]
print(lista)

listap=[r for r in lista if r%2==0]
print(listap)

s1 = {"jajko":"10szt", "ziemnaiki":"20kg", "marchewka":"5kg", "buraki":"50kg","pomidor":"20szt"}
s2 = {v: k for v,k in s1.items() if "szt" in k}
print(s2)

def czy_prostokatny(a,b,c):
    boki = sorted([a,b,c])
    if boki[0]**2 + boki[1]**2==boki[2]**2:
        return True
    else:
        return False
print(czy_prostokatny(4,6,2))

def pole_trapezu(a,b,h):
    pole = 0.5*(a+b)*h
    return pole
print(pole_trapezu(5,2,1))

def ciag(a1, r, n):
    iloczyn = 1
    for i in range(n):
        iloczyn *= a1 + i * r
    return iloczyn
print(ciag(1,4,10))


lp = int(input("Podaj liczbe: "))
if lp < 0:
    raise ValueError("Nie da się pierwiastkowac ujemnej liczby")
print("Oto pierwiastek z tej liczby: ", math.sqrt(lp))


#z lekcji


#s1 = {1:2, 2:3, 3:4}
#s2 = {v: k for k, v in s1.items()}
#print(s2)

#def rownanie_kwadratowe(a,b,c):
#    delta = b**2-4*a*c
#    if delta<0:
#        print("Brak rozwiazan")
#        return 0
#    elif delta==0:
#        x = -b/(2*a)
#        print("Jeden pierwiastek")
#        return x
#    elif delta>0:
#        x1 = (-b - math.sqrt(delta)) / (2*a)
#        x2 = (-b + math.sqrt(delta)) / (2 * a)
#        print("Dwa pierwiastki")
#        return x1, x2
#
#print(rownanie_kwadratowe(6, 1, 3))
#print(rownanie_kwadratowe(1, 2, 1))
#print(rownanie_kwadratowe(1, 4, 1))
#
#def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#print(dlugosc_odcinka())
#print(dlugosc_odcinka(2, 4, 5, 7))
#print(dlugosc_odcinka(x2 = 1, y2 = 5 , x1 = 5, y1 = 7))

#plik = open('tekst.txt', 'r', encoding='utf-8')
#znaki = plik.read(10)
#linia = plik.readline()
#linie = plik.readlines()
#plik.close()

#print(znaki)
#print(linia)
#print(linie)

#plik1 = open('tekst.txt', 'a+', encoding = 'utf-8')
#plik1.seek(0)
#znaki1 = plik1.read(10)
#plik1.close()
#print(znaki1)

#plik2 = open('tekst.txt', 'w', encoding = 'utf-8')
#plik2.write('aaaadq')
#plik2.close()

#with open('tekst.txt','r') as plik:
#    znaki2 = plik.readlines()

#print(znaki2)
