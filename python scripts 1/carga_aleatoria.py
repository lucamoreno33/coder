import random
def carga_aleatoria_int(arreglo,cantidad_elementos,minimo,maximo):
    for i in range(cantidad_elementos):
        arreglo[i]=random.randint(minimo,maximo)