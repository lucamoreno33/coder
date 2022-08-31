vector=["luca", "bruno","facu","joe","maxi","juan","gabriel"]
def buscar_alumno(vector, tamaño):
    p=1
    alumno=input("ingrese el nombre del alumno: ")
    esta = False
    for i in range(tamaño):
        if alumno==vector[i]:
            print("el alumno ",alumno," se encuentra en el vector")
            esta = True
    if esta==False:
        print("el alumno no esta en el vector")
print(vector)
buscar_alumno(vector,7)