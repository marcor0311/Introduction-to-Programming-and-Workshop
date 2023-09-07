##########################proyecto
import sys
sys.setrecursionlimit(2000000000)
import math
'''Explicacion: Va buscando factores 1 a 1 hasta la mitad de n
Dominio: Numeros naturales
Rango: Numeros primos'''
"De forma recursiva"
def Modo1(n,fac=2):#fac tiene que ser igual a 2
    if n==1:
        print()
        return
    if fac>n//2:
        print(n)
        return
    if n%fac==0:
        print(fac, end=" ")
        return Modo1(n//fac,fac)
    return Modo1(n,fac+1)
'''Explicacion: Va buscando factores 1 a 1 hasta la mitad de n
Dominio: Numeros naturales
Rango: Numeros primos'''
def Modo2(n):
    fac=2 #fac tiene que ser igual a 2
    while n!=1: #se utiliza iteracion, en este caso while
        if fac>n//2:
            print(n)
            return
        if n%fac==0:
            print(fac, end=" ")
            n//=fac
        else:
            fac+=1
    print()
'''Explicacion: Divide en por 2 tantas veces como sea posible sino se prueba con
los impares hasta la raiz cuadrada de n
Dominio: Numeros naturales
Rango: Numeros primos'''
"De forma recursiva"
def Modo3(n,fac=3):#fac tiene que ser 3
    if n == 1:
        print()
        return
    if n % 2 == 0:
        print(2, end=" ")
        return Modo3(n // 2, 3)
    if fac*fac > n:
        print(n)
        return(n)
    if n%fac==0:
        print(fac, end=" ")
        return Modo3(n//fac,fac)
    return Modo3(n,fac+2)
'''Explicacion: Divide en por 2 tantas veces como sea posible sino se prueba con
los impares hasta la raiz cuadrada de n
Dominio: Numeros naturales
Rango: Numeros primos'''
def Modo4(n):
    fac=3#fac tiene que ser 3
    while n!=1: #se utiliza iteracion, en este caso while
        if n%2==0:
            print(2, end=" ")
            n//=2
        elif fac*fac>n:
            print(n)
            return
        elif n%fac==0:
            print(fac, end=" ")
            n//=fac
        else:
            fac+=2
    print()
#La Criba necesita un limite para generarse
#Ademas es una funcion externa porque solo se tiene que calcular una vez
def Criba(limite):
    limite = int(math.sqrt(limite)) #se define el limite
    marcados = [] #numeros no primos
    primos = [] #numeros primos
    for i in range(2,limite+1): #esta iteracion ayuda a filtrar las listas
        if i not in marcados:
            primos.append(i)
            for j in range(i, limite//i+1):
                if j*i not in marcados:
                    marcados.append(j*i)
    return primos
'''Explicacion: Se utiliza la criba para factorizar los numeros
Dominio: Numeros naturales
Rango: Numeros primos generados en la criba'''
def Modo5(n, primos):
    contador = 0
    while contador < len(primos) and n!= 1:
        if primos[contador]*primos[contador] > n:
            print(n)
            return
        if n % primos[contador]==0:
            print(primos[contador], end=" ")
            n //= primos [contador]
        else:
            contador += 1
    print()
"Esto para la entrada por consola"
entradaPrincipal = [int(i) for i in input().split(" ")]
"Esto es para generar la criba una vez con el limite que se haya entregado"
lista_de_numerosPrimos = None
if entradaPrincipal[1] == 5:
    lista_de_numerosPrimos = Criba(entradaPrincipal[2])
"Esto es para saber cual modo se usara"
for i in range(entradaPrincipal[0]):
    if entradaPrincipal[1] == 1:
        Modo1(int(input()))
    if entradaPrincipal[1] == 2:
        Modo2(int(input()))
    if entradaPrincipal[1] == 3:
        Modo3(int(input()))
    if entradaPrincipal[1] == 4:
        Modo4(int(input()))
    if entradaPrincipal[1] == 5:
        Modo5(int(input()), lista_de_numerosPrimos)