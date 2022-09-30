def año_biciesto(biciesto):
   biciesto =año
   if año % 4==0 and ((año % 100 != 0) or ( año % 400==0))
     print("es año biciesto")
   else:
    print("no es año biciesto")
  
  
 return biciesto 
  
def principal():
 dia = int (input("imgrece un dia"))
 año = int (input ("ingrece un año"))
 mes = int (input ("inrnesar mes "))

   if (32 > dia>0 and (1000 < año < 10000 and 0 < mes < 13)):
   
    if mes==1:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==2:
      if 00<dia<29:
       print("fecha correcta") 
      else:
       print("fecha incorrecta")
    if mes==3:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==4:
     if 00<dia<31:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==5:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==6:
     if 00<dia<31:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==7:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==8:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==9:
     if 00<dia<31:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==10:
     if 00<dia<32:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==11:
     if 00<dia<31:
       print("fecha correcta") 
     else:
       print("fecha incorrecta")
    if mes==12:
      if 00<dia<32:
       print("fecha correcta") 
      else:
        print("fecha incorrecta")
      
 else:
   print("ffecha incorrecta")
  
 varRecibe = año_biciesto(biciesto)
  
principal ()
