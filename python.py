''' PROBLEMA 7
Elabore un algoritmo que permita validar una fecha dada. La fecha está 
integrada por 3 vbles: año, mes y día. Para que una fecha sea correcta es 
necesario que:
1. El día mayor o igual a 1 y menor o igual a 31 
2. El año debe ser mayor a 1000 y menor a 10000.
3. El mes debe estar entre 1 y 12.
4. Dependiendo del mes que sea, el día debe estar dentro del rango válido. 
Si existe algún error, imprimir por pantalla la ctte “ERROR EN FECHA” 
seguidos la variable con el error, si la fecha es correcta, imprimir “FECHA CORRECTA”
Deberá contemplar si dicho año ingresado es bisiesto o no. Para el análisis correcto, si es 
bisiesto debe indicarlo también. Puede ver el siguiente video https://www.youtube.com/watch?v=QShH3ctjhUY (desde el 
comienzo hasta minuto 3:41) Utilizar 2 métodos, uno para saber si es bisiesto el año (Recibe en 
parámetros y retorna valor), y otro para determinar si la fecha es válida o no (Recibe en 
parámetros y retorna el mensaje correspondiente). Recuerde que un método puede convocar a otro método.'''

def bisiesto(año):
    if año % 4 == 0:
        return 'bisiesto'
    else:
        return 'no bisiesto'
#Analiza los meses y días del año

def principal():
    print("1. El día mayor o igual a 1 y menor o igual a 31.")
    print("2. El año debe ser mayor a 1000 y menor a 10000.")
    print("3. El mes debe estar entre 1 y 12.")

    año=int(input("Ingrese el año --> "))
    mes=int(input("Ingrese el mes --> "))
    dia=int(input("Ingrese el dia --> "))
    bisiesto_comprobar = bisiesto(año)

    if dia>=1 and dia<=29 and mes==2 and año>1000 and año<10000 and bisiesto_comprobar=='bisiesto':
        return "Año Bisiesto, FECHA CORRECTA!"
    elif dia>=1 and dia<=31 and mes>=1 and mes<=12 and año>1000 and año<10000 and bisiesto_comprobar=='no bisiesto':
        #controlar fechas abril, junio, septiembre, noviembre terminan en 30 el resto 31
        if mes in [4,6,9,11] and dia > 30:
            return 'ERROR EN FECHA!'
        else:
            return "Año No Bisieto, FECHA CORRECTA!"

    else:
        return 'ERROR EN FECHA!'

imprimir = principal()
print(imprimir)



