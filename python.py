def principal():
    print("Peso piedras de Lucia: ")
    LuciaP1 = float(input("Ingrese peso piedra 1: "))
    LuciaP2 = float(input("Ingrese peso piedra 2: "))
    print("Peso piedras de Juana: ")
    JuanaP1 = float(input("Ingrese peso piedra 1: "))
    JuanaP2 = float(input("Ingrese peso piedra 2: "))
    print("Peso piedras de Javier: ")
    JavierP1 = float(input("Ingrese peso piedra 1: "))
    JavierP2 = float(input("Ingrese peso piedra 2: "))
    print("Peso piedras de Andres: ")
    AndresP1 = float(input("Ingrese peso piedra 1: "))
    AndresP2 = float(input("Ingrese peso piedra 2: "))

    LuciaPT = LuciaP1 + LuciaP2
    JuanaPT = JuanaP1 + JuanaP2
    JavierPT = JavierP1 + JavierP2
    AndresPT = AndresP1 + AndresP2

    if LuciaPT>JuanaPT and LuciaPT>JavierPT and LuciaPT>AndresPT:
        print("Lucia tiene las piedras de mayor peso: ", LuciaPT)
    elif JuanaPT>LuciaPT and JuanaPT>JavierPT and JuanaPT>AndresPT:
        print("Lucia tiene las piedras de mayor peso: ", JuanaPT)
    elif JavierPT>JuanaPT and JavierPT>LuciaPT and JavierPT>AndresPT:
        print("Lucia tiene las piedras de mayor peso: ", JavierPT)
    elif AndresPT>JuanaPT and AndresPT>JavierPT and AndresPT>LuciaPT:
        print("Lucia tiene las piedras de mayor peso: ", AndresPT)
    else:
        print("sos re pavo")
    promedioPT = (LuciaPT + AndresPT + JavierPT + JuanaPT)/4
    print("El peso promedio de los petes igual a: ", promedioPT)
#principal()










    
    