def busqueda_secuencial(arreglo,valor_buscar,cantidad_elementos):
    i=0
    respuesta=1
    while(i<cantidad_elementos) and (arreglo[i] != valor_buscar):
        i+= 1
    if (i < cantidad_elementos):
        #devolver posicion
        respuesta+= i
    return respuesta
arreg=[1,2,3,4,5,6,7,8,9,10]
print(busqueda_secuencial(arreg, 5, 9))