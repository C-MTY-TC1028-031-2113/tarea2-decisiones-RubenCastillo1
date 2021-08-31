
def main():
    a=int(input("Ingresa tu edad: "))
    if a<0:
        while a<0:
            print("respuesta incorrecta")
            a=int(input("Ingresa tu edad: "))
    else:
        print("")
    
    b = input("¿Tienes identificación oficial? (s/n)? ")
    if b != "n" and b != "s":
        while b != "n" or b != "s":
            print("Respuesta incorrecta")
            b = input("¿Tienes identificación oficial? (s/n)? ")
    else:
        print("")
            
            
    if a >= 18 and b == "s":
        print("Trámite de licencia concedido")
    else:
        print("No cumples requisitos")



if __name__ == '__main__':
    main()
