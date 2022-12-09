def cruzarRio():
    izquierda = [1,1,1,1]
    derecha = [0,0,0,0]
    posicion_izq = True
    pasos = []
    print(izquierda, "\t", derecha)

    while(True):
        if(derecha==[1,1,1,1]):
            break;
        if(posicion_izq):
            print("Izquierda")
            if(izquierda[0] == izquierda[1] and izquierda[1] == izquierda[2] and izquierda[2] == izquierda[3]):
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                pasos.append("GC")
                print("R1")
            elif(izquierda[1] != izquierda[2] and izquierda[1] != izquierda[3] and pasos[len(pasos)-1][0] != "C"):
                izquierda[0] = 0
                derecha[0] = 1
                pasos.append("C")
                print("R2")
            elif(izquierda[0] == 1 and izquierda[3] == izquierda[0] and izquierda[1] != izquierda[2] and pasos[len(pasos)-1][0] != "M"):
                izquierda[0], izquierda[3] = 0, 0
                derecha[0], derecha[3] = 1, 1
                pasos.append("MC")
                print("R3")
            elif(izquierda[0] == 1 and izquierda[2] == izquierda[0] and izquierda[1] != izquierda[3] and pasos[len(pasos)-1][0] != "L"):
                izquierda[0], izquierda[2] = 0, 0
                derecha[0], derecha[2] = 1, 1
                pasos.append("LC")
                print("R4")
            elif(izquierda[0] == 1 and izquierda[0] == izquierda[1] and pasos[len(pasos)-1][0] != "G"):
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                pasos.append("GC")
                print("R5")
        else:
            print("Derecha")
            if(derecha[0] == derecha[1] and derecha[1] == derecha[2] and derecha[2] == derecha[3]):
                izquierda[0], izquierda[1] = 1, 1
                derecha[0], derecha[1] = 0, 0
                pasos.append("GC")
                print("R1")
            elif(derecha[1] != derecha[2] and derecha[1] != derecha[3] and pasos[len(pasos)-1][0] != "C"):
                izquierda[0] = 1
                derecha[0] = 0
                pasos.append("C")
                print("R2")
            elif(derecha[0] == 1 and derecha[3] == derecha[0] and derecha[1] != derecha[2] and pasos[len(pasos)-1][0] != "M"):
                izquierda[0], izquierda[3] = 1, 1
                derecha[0], derecha[3] = 0, 0
                pasos.append("MC")
                print("R3")
            elif(derecha[0] == 1 and derecha[2] == derecha[0] and derecha[1] != derecha[3] and pasos[len(pasos)-1][0] != "L"):
                izquierda[0], izquierda[2] = 1, 1
                derecha[0], derecha[2] = 0, 0
                pasos.append("LC")
                print("R4")
            elif(derecha[0] == 1 and derecha[1] == derecha[0] and pasos[len(pasos)-1][0] != "G"):
                izquierda[0], izquierda[1] = 1, 1
                derecha[0], derecha[1] = 0, 0
                pasos.append("GC")
                print("R5")
            
        posicion_izq = not posicion_izq
        print(pasos[len(pasos)-1])
        print(izquierda, "\t", derecha)
    return pasos

pasosReales = cruzarRio()

print("-----------------------------------------------")
print(pasosReales)