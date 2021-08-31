import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    
    if a==0 and b==0:
        print("No tiene solucion")
    elif a==0 and b!=0:
        x=(-c)/b
        print(x)
    elif a!=0 and b==0:
        if (c<0 and a>0) or (c>0 and a<0):
            x=math.sqrt((-c)/a)
            print(x)
        else: 
            print("Raices complejas")
    elif a!=0 and b!=0:
        if ((b**2)-(4*a*c))<0:
            print("Raices complejas")
        else:
            x = (-b+(math.sqrt((b**2)-(4*a*c)))) / (2*a)
            print("x = "+str(x))
            x = (-b-(math.sqrt((b**2)-(4*a*c)))) / (2*a)
            print("x = "+str(x))
    else:
        ""


if __name__ == '__main__':
    main()
