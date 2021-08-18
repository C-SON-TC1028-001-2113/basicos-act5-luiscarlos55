import math
def main():
    #escribe tu código abajo de esta línea
    h = int(input("Dame la altura de la casa: "))
    a = int(input("Dame el angulo de inclinación: "))
    s = math.sin(a)
    l = h/s
    print("El largo de la escalera es: "+str(math.ceil(l)))    
    
if __name__ == '__main__':
    main()
