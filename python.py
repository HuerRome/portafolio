
def menu():
    print("------------Menu de restaurante---------------")
    print("Si su compra supera los 600$ se hara un descuento del 10%")
    print("1- Pizza de muzarella------------ 550$")
    print("2- Pizza especial---------------- 750$")
    print("3- Milanesa napolitana------------ 850$")


    opcion = int(input("Por favor ingrese una opcion: "))
    if opcion < 1 or opcion > 3:
        print("Ingreso una opcion incorrecta. Intente de nuevo\n")
        menu()
    else:
        return opcion


def opciones():
    opcion = menu()
    if opcion == 1:
        total = 550
        print('Su pedido es menor a 600$, no se aplica descuento')
        print(f"Su total a pagar es {total}$")
        return total
    elif opcion == 2:
        descuento = (750/100) * 10
        resta = 750 - descuento
        print(f"Su compra supero los 600$ se aplica descuento. Total a pagar {resta}$")
        return resta
    else:
        descuento = (800/100) * 10
        resta = 800 - descuento
        print(f"Su compra supero los 600$ se aplica descuento. Total a pagar {resta}$")
        return resta
opciones()


def opciones_pago():
    print("Por favor ingrese una opcion de pago")
    print("a- Devito ")
    print("b- Efectivo")
    print("c-Transferencia")
    opcion = input("Ingres")






