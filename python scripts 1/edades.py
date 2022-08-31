import random
vector=[0]*20
def carga_vector(arreglo, menor, mayor, tamaño):
    for i in range(tamaño):
        arreglo[i]=random.randint(menor, mayor)

def ordenarBurbuja(vector,elementos):
   pasos = 0
   se_hizo_intercambio = True
   while se_hizo_intercambio:
       se_hizo_intercambio = False
       i = 1
       pasos = pasos + 1
       while (i < elementos):
           if (vector[i - 1] > vector[i]):
               #realizamos el itercambio
               swap = vector[i - 1]
               vector[i - 1] = vector[i]
               vector[i] = swap
               se_hizo_intercambio = True
           i = i + 1
      
   return vector

def mas_repetido(arreglo, tamaño):
    for i in range()





carga_vector(vector,1,10,20)




