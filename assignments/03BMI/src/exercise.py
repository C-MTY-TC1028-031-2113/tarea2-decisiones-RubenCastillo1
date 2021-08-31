def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    if peso !=0 and altura != 0:
        imc=peso/altura**2
    else:
        ""
        
    if peso !=0 and altura != 0:
        if imc<20:
            estado = "Peso bajo"
        elif imc>=20 and imc<25:
            estado = "Peso normal"
        elif imc>=25 and imc<30:
            estado = "Sobrepeso"
        elif imc>=30 and imc<40:
            estado = "Obesidad"
        else:
            estado = "Obesidad morbida"


    if peso !=0 and altura != 0:
        print(estado)
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")

if __name__=='__main__':
    main()