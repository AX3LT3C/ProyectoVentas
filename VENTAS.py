name = str(input("Digite su nombre: "));
age = int(input("Digite su año de nacimiento: "));
total = 2022 - age;
print("SU EDAD ACTUAL ES: ", total);

if (total >= 18):
    print("********* PUEDE CONTINUAR DIGITANDOSE *********");
    ven1=int(input("Digite las ventas del primer semestre: "));
    ven2=int(input("Digite las ventas del segundo semestre: "));
    totalanual=ven1+ven2;
    print("VENDEDOR: ",name);
    print("VENTAS ANUALES: ",totalanual);

    if (ven1>ven2):
        mensaje="1ERO.";
        print("MEJOR SEMESTRE: ",mensaje);
    elif(ven2>ven1):
        mensaje="2DO."
        print("MEJOR SEMESTRE: ",mensaje);

    if (totalanual < 100000):
        print("MEDALLA ACREDITADA: Bronce");
        print("PREMIO: Un dia libre");
    elif(totalanual < 500000):
        print("MEDALLA ACREDITADA: Plata");
        print("PREMIO: Un dia libre y un bono de Q250");
    elif(totalanual < 1000000):
        print("MEDALLA ACREDITADA: Oro");
        print("PREMIO: Un dia libre y un bono de Q500");
    elif(totalanual > 100000):
        print("MEDALLA ACREDITADA: Diamante");
        print("PREMIO: Dos dias libres y un bono de Q1000");

else:
    print("SE ESTA FINALIZANDO EL SISTEMA");
    end