def czy_doskonala():
    suma = 0
    lista = []
    for i in range(1,1001):
        for x in range(1, i):
            if i%x==0:
                suma = suma + x
                if suma == i and x >= suma/2:
                    lista.append(i)
                    suma = 0
                elif (x==i-1 and suma !=i):
                    suma = 0
            elif (x==i-1 and suma !=i):
                suma = 0
    print(lista)




czy_doskonala()