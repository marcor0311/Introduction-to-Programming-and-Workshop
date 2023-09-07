from time import time
def nodosNivel(arbol, n):
    #Funcion vista en clases
    #Modificada para adaptarse al tipo de arbol usado
    if len(arbol) != 2:
        if n != 0:
            return nodosNivel(arbol[1], n-1) + nodosNivel(arbol[2], n-1)
        return [arbol[0]]
    if n!=0:
        return []
    return [arbol[0]]

def encontrar_nombre(string_nombre):
    # recorre los caracteres de atras para adelante para obtener el nombre sin extension
    for caracter in range(len(string_nombre)-1,-1,-1):
        if string_nombre[caracter]==".":
            return string_nombre[:caracter]
    return string_nombre[:1]#Se supone que nunca deberia de pasar

def preorden(arb):
    #Funcion vista en clases, modificada para adaptarse al arbol usado
    #Obtenemos todos los nodos, y con el len obtenemos la cantidad de nodos
    if 2 == len(arb):return arb
    return [arb[0]]+preorden(arb[1])+preorden(arb[2])
def rutasHojas(arbol_binario):
    #Funcion que nos da todas las rutas a una hoja
    rutas = []
    cola = []
    cola.append([""]+[arbol_binario])

    while cola:

        ruta_actual = cola.pop(0)

        arbol_actual = ruta_actual.pop()

        #print(ruta_append)
        if len(arbol_actual)==2:
            #Len arbol==2 sustituye el arbol =[]
            #aqui se sabe cuando la ruta acabo

            rutas.append(ruta_actual + [arbol_actual[1]])
            continue
        #Anade 0s o 1s segun el camino que se tome
        if arbol_actual[1] != []:

            cola.append([ruta_actual[0]+"0"]  + [arbol_actual[1]])
        if arbol_actual[2] != []:
            #print(ruta_append)
            cola.append([ruta_actual[0]+"1"]   + [arbol_actual[2]])
        #if arbol_actual[1] == [] and arbol_actual[2] == []:

    return rutas
def insertar_ordenar(a, x, lo=0, hi=None):
    #Insertar a lista con busqueda binaria


    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2

        if x[0] < a[mid][0]:
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)




def nivel(k, arb):
    #Obtienes los nodos de cada nivel
    #Le saca len() para obtener nodos por nivel
    if len(arb) == 2: return []
    if k == 0: return [arb[0]]
    return nivel(k-1,arb[1])+nivel(k-1,arb[2])
def anchura(arb):
    #Funcion que obtiene la anchura del arbol
    anch = 0
    for niv in range(altura(arb)+1):
        anch = max(anch, len(nivel(niv, arb)))
    return anch
def altura(arb):
    #Funcion vista en clases, modificada
    #El -1 pasa a ser 0, porque no existe un salto extra
    #como si existiria en un arbol binario visto en clases
    if len(arb)==2:return 0
    return 1+max(altura(arb[1]),altura(arb[2]))


def contar_frecuencias(archivo,objeto_archivo):
    frecuencias = [0] * 256
    # Lista de frecuencias
    # 256 espacios para encontrarlos mas rapido

    #Cada vez que encuentra 1 byte le suma a la frecuencia asignada a su posicion
    for b in objeto_archivo:
        frecuencias[b] += 1
    return frecuencias
def compresor(archivo):
    print("Comprimiendo")
    byytes = open(archivo, "rb").read()

    frecuencias=contar_frecuencias(archivo,byytes)
    #obtiene las frecuencias




    lista_de_arboles = []
    for i in range(256):
        if frecuencias[i]:
            # lista_de_arboles.append([[frecuencias[i],i],[],[]])

            lista_de_arboles.append([frecuencias[i], i])
            #Añade al arbol los bytes que si aparecen

    lista_de_arboles.sort()
    #ordena los arboles


    while (len(lista_de_arboles) > 1):
        izquierdo = lista_de_arboles.pop(0)
        derecho = lista_de_arboles.pop(0)
        arbol_a_meter = [izquierdo[0] + derecho[0], izquierdo, derecho]

        insertar_ordenar(lista_de_arboles, arbol_a_meter)

        # hoja es de largo 2
        # largo 3 es nodo interno o raiz aka arbol
        # Crea el arbol, donde las hojas son el byte y su frecuencia,el resto de nodos son sumas de frecuencias

    lista_de_arboles = lista_de_arboles[0]
    #realmente no es una lista de arboles llegado a este punto.
    #Quitarle los [] externos


    ruta_codigos = rutasHojas(lista_de_arboles)  # Obtener lista de codigos donde
    #Utiliza los caminos hacia los nodos, y crea un codigo para cada hoja.
    # El ultimo elemento es el byte y el resto son las rutas



    name_archivos_nuevos = encontrar_nombre(archivo)

    extension=encontrar_nombre(archivo[-1::-1])
    #encuentra el nombre archivo con el string alreves, para obtener la extensio
    extension="."+extension[-1::-1]
    #le añade el punto, y le da vuelta al string obtenido




    codigos = [0] * 256  # Se hace para hacer mas sencillo la busqueda del codigo
    for codigo in ruta_codigos:
        index = int(codigo[1])
        codigos[index] = codigo[0]  #Le envia el codigo a la posicion del byte.
        #Se hace para optimizar la busqueda en la siguiente parte
    indice_ultimo_byte=0


    with open(name_archivos_nuevos + ".huff", "wb") as escribir_huff:
        byte_a_escribir = ""



        for b in byytes:

            byte_a_escribir += codigos[b]



            #Anade el string el codigo del byte


            while len(byte_a_escribir) >= 8:
                #Cuanto el byte a escribir sea mayor o igual a 8
                #lo escribe y lo recorta
                escribir_huff.write(bytes([int(byte_a_escribir[:8], 2)]))

                byte_a_escribir = byte_a_escribir[8:]



        if len(byte_a_escribir)!=0:
         last_byte=byte_a_escribir
         #Se utiliza para almacenar el ultimo byte en caso
         #de que haya un byte incompleto al final
        else:last_byte="No"

        escribir_huff.close()

    indice_ultimo_byte=8-indice_ultimo_byte

    with open(name_archivos_nuevos + ".table", "w") as table_file:
        #Escribe el table de manera que podamos utilizarlo en la descompresion
        for codigo in ruta_codigos:
            table_file.write(f"{codigo[0]},{codigo[1]}\n")
            #crea el archivo table.
            #potencialmente aqui puedo poner el ultimo byte
        #table_file.write(str(indice_ultimo_byte))
        #Escribe la extension para escribirla en la descompresion
        table_file.write(extension+"\n")
        table_file.write(last_byte)
        #Escribe el ultimo byte, para escribirlo en la descompresion
        table_file.close()

    with open(name_archivos_nuevos + ".stats.txt", "w") as stats_file:
            altura_arbolito=altura(lista_de_arboles)
            stats_file.write(f"La altura del arbol es {altura_arbolito} \n")
            stats_file.write(f"La anchura del arbol es {anchura(lista_de_arboles)} \n")
            stats_file.write(f"La cantidad de nodos del arbol es {len(preorden(lista_de_arboles))} \n")
            for i in range(altura_arbolito+1):
                stats_file.write(f"Nodos en el nivel {i} : {len(nodosNivel(lista_de_arboles,i))} \n")




            stats_file.write(f"Frecuencias \n")
            for i in range(len(frecuencias)):
                if frecuencias[i] !=0:
                    stats_file.write(f" Byte {i}: {frecuencias[i]} \n")





            stats_file.close()
    print("Compresion Finalizada")

    return  # Eliminar el return o cambiarlo



#Se asume que el archivo estará en la misma direccion del .py
archivo="zack.svg"

x=time()
compresor(archivo)
print(f"Compresion realizada en {time()-x}")
