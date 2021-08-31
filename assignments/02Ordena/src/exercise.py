
def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    if x<y and x<z:
        a=x
        print(x)
    elif y<x and y<z:
        a=y
        print(y)
    else:
        a=z
        print(z)

    if a==x:
        if z<y:
            print(z)
            print(y)
        else:
            print(y)
            print(z)
    elif a==y:
        if x<z:
            print(x)
            print(z)
        else:
            print(z)
            print(x)
    elif y<x:
        print(y)
        print(x)
    else:
        print(z)
        print(y)


if __name__=='__main__':
    main()
