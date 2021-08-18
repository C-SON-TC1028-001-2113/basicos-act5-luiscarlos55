import math
def main():
    #escribe tu código abajo de esta línea
    b = int(input('Dame la base: '))
    h = int(input('Dame la altura: '))
    r = int(input('Dame el rendimiento por m2: '))
    area = b * h
    print("El area es: "+str(area))
    distancia = (area/r)
    print("Rendimiento por m2/l: "+str(distancia))

if __name__ == '__main__':
    main()
