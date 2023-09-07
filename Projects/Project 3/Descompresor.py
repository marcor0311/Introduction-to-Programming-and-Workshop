from time import time


def encontrar_nombre(string_nombre):
    #recorre los caracteres de atras para adelante para obtener el nombre sin extension
    for caracter in range(len(string_nombre)-1,-1,-1):
        if string_nombre[caracter]==".":
            return string_nombre[:caracter]
    return string_nombre[:1]#Se supone que nunca deberia de pasar

def recorrido_arbol_optimizado(archivo_descomprimido,lista_de_bytes,arbol_en_funcion,ultimo_byte):

    def recorrido_arbol_aux(codigo,arbol_actual,arbol_original):

        if arbol_actual[0]!=" ":
            archivo_descomprimido.write(bytes([arbol_actual[0]]))

            return codigo,arbol_original
        if codigo:
            #Ambas condiciones van recortando el arbol y el codigo
            if codigo[0]=="1":
                return recorrido_arbol_aux(codigo[1:],arbol_actual[2],arbol_original)
            elif codigo[0]=="0":
                return recorrido_arbol_aux(codigo[1:],arbol_actual[1],arbol_original)
        else:
            #Si se acaba el codigo, devuelve un "", el cual se interpreta como False en el while
            #y el arbol original, para continuar el recorrido con el siguiente byte
            return "",arbol_actual




    byte_a_escribir=""
    #Deep copy al arbol, necesitamos 2 arboles, el original para mandarlo cuando el auxiliar se acabe
    arbol_actual=[i for i in arbol_en_funcion]
    for elemento in lista_de_bytes:
        byte_a_escribir+=elemento
        #Busca a terminar cada byte individual antes de proseguir
        while byte_a_escribir:
            byte_a_escribir,arbol_actual=recorrido_arbol_aux(byte_a_escribir,arbol_actual,arbol_en_funcion)
    if ultimo_byte!="No":
        #Si es no, los bits eran divisores de 8
        #y no hay problema con el byte final
        byte_a_escribir+=ultimo_byte
        while byte_a_escribir:

            byte_a_escribir,arbol_actual=recorrido_arbol_aux(byte_a_escribir,arbol_actual,arbol_en_funcion)
    archivo_descomprimido.close()

    pass






def rearmar_arbol(codigos, arbol_nuevo=[]):
    def rearmar_arbol_aux(arbol, codigo, byte_a_poner):
        #recibe codigos y crea el arbol con ellos

        if not codigo:
            arbol.append(byte_a_poner)
            #Si el codigo actual no existe, añade el byte como nodo


            return
        if arbol == []:
            arbol.append(" ")
            arbol.append([])
            arbol.append([])
            #Si el camino no existe, lo crea
        if int(codigo[0]):
            rearmar_arbol_aux(arbol[2], codigo[1:], byte_a_poner)
            #Recorre el camino derecho
        else:
            #recorre el camino izquierdo
            rearmar_arbol_aux(arbol[1], codigo[1:], byte_a_poner)

        return arbol

    for codigo in codigos:
        arbol_nuevo = rearmar_arbol_aux(arbol_nuevo, codigo[0], codigo[1])

    return arbol_nuevo






def decompresor(archivo):
    print('Descomprimiendo')

    nombre_archivos=encontrar_nombre(archivo)
    #Meramente estetico, para elimina el .huff de la variable archivo
    codigos = []
    #Lee los codigos que se utilizaran
    with open(nombre_archivos+".table", 'r') as tabla_codigos:
        codigos=tabla_codigos.readlines()
        tabla_codigos.close()
    #El ultimo elemento de esa lista es un byte
    #el ultimo byte, al cual le faltaron 00s para ser escrito
    #Puede ser un "No", si no existia algun byte incompleto

    #el ultimo byte y la extension estan al final de la lista
    indice_ultimo_byte=codigos.pop()
    extension=codigos.pop()
    extension=extension[:-1]
    #elimina el salto de linea de la extension


    for codigo in range(len(codigos)):

        nuevo_codigo=codigos[codigo].split(",")
        nuevo_codigo[1] = nuevo_codigo[1][:-1]
        nuevo_codigo[1] = int(nuevo_codigo[1])
        codigos[codigo]=nuevo_codigo








    arbol_rearmado = rearmar_arbol(codigos)

    bytes_huff = open(nombre_archivos+'.huff', "rb").read()
    #vamos a probar con el bytesote
    #luego falta modificar el byte actual












    lista_bytes = ["0"*(8 - len(bin(i)[2:]))+bin(i)[2:] for i in bytes_huff]

    decompressed=open(nombre_archivos+"decompressed"+extension,"wb")
    recorrido_arbol_optimizado(decompressed,lista_bytes,arbol_rearmado,indice_ultimo_byte)






    print("Decompresion Exitosa")

    return




x=time()
archivo="zack.huff"

#Se asume que
#El huff y el table estan la misma carpeta que el .py
decompresor(archivo)
print(f"Tiempo de descompresion {time()-x}")
input()






