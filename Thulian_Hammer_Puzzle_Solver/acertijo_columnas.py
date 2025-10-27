import random

def main():
    # Las posiciones de los bloques son:
    #   - DELANTE: 1
    #   - DERECHA: 2
    #   - ATRÁS: 3
    #   - IZQUIERDA: 4

    blockA = random.randint(0,3)
    blockB = random.randint(0,3)
    blockC = random.randint(0,3)
    blockD = random.randint(1,3)

    while not (blockA == blockB == blockC == blockD == 0):

        print(f"Bloque A: {blockA+1}\nBloque B: {blockB+1}\nBloque C: {blockC+1}\nBloque D: {blockD+1}")

        n = input(
            "\n¿Qué quiere hacer?"
            "\nAñadir A"
            "\nAñadir B"
            "\nAñadir C"
            "\nAñadir D"
            "\nSalir (s)"
            "\n --> "
        )
        
        if(n == "a"):
            blockA, blockB = añadirA(blockA, blockB)
        
        elif(n == "b"):
            blockA, blockB, blockC = añadirB(blockA, blockB, blockC)
        
        elif(n == "c"):
            blockB, blockC, blockD = añadirC(blockB, blockC, blockD)

        elif(n == "d"):
            blockC, blockD = añadirD(blockC, blockD)
        
        elif(n == "s"):
            print("Saliendo...")
            break
        
        else:
            print("No se ha elegido una opción mostrada.")
    
    print(f"\nBloque A: {blockA+1}\nBloque B: {blockB+1}\nBloque C: {blockC+1}\nBloque D: {blockD+1}")

def añadirA(blockA, blockB):
    blockA = (blockA+2)%4
    blockB = (blockB+1)%4
    return blockA, blockB

def añadirB(blockA, blockB, blockC):
    blockA = (blockA+1)%4
    blockB = (blockB+2)%4
    blockC = (blockC+1)%4
    return blockA, blockB, blockC

def añadirC(blockB, blockC, blockD):
    blockB = (blockB+1)%4
    blockC = (blockC+2)%4
    blockD = (blockD+1)%4
    return blockB, blockC, blockD

def añadirD(blockC, blockD):
    blockC = (blockC+1)%4
    blockD = (blockD+2)%4
    return blockC, blockD

if __name__ == "__main__":
    main()