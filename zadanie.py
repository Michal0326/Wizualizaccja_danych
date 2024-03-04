import sys
def zad1():
    zdanie = input("Podaj zdanie: ")
    slowa = (zdanie.split())
    print(len(slowa))

#def zad2():
#    a = int(sys.stdin.readline())
#    b = int(sys.stdin.readline())
#    c = int(sys.stdin.readline())

#    dzialanie = (a**b)+c
#    print(dzialanie)


def zad3():
    napis = input("Podaj napis: ")
    odwrotny = napis[::-1]
    if napis == odwrotny:
        print("To palindrom")
    else:
        print("Nie palindrom")

def zad4():
    liczba = int(input("Podaj liczbę: "))
    if liczba%2==0 and liczba > 2:
        print("Liczba nie jest pierwsza")
    else:
        print("Liczba jest pierwsza")



def zad5(n):
    suma_dziel = sum([i for i in range(1,n) if n % i ==0])
    return suma_dziel == n

for n in range (1,1001):
    if zad5(n):
        print(n)

def zad6():
    lista=[]
    for i in range(1,5):
        f = float(input("Podaj liczbę typu float: "))
        p = int(input("Podaj liczbe typu int: "))
        lista.append(f)
        lista.append(p)
    for i in lista:
        lista[i] = lista[i]**2
    print(lista)



zad1()
#zad2()
zad3()
zad4()
zad5(n)
zad6()