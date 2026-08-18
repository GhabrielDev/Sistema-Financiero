import motivacion as mot
import Validaciones as val
import time

#Sitema de gianancia neta al mes  al año para saber cuantos son tus ingresos al año y al mes

print("---Motivacion---")
print(mot.frase_millonaria())
print("---- Welcome a la calculadora de ingresos ----")

#Calculadora de exito y motivacion

name = val.mensaje(f"Ingresa tu nombre: ")

age = val.preguntar_numero("¿Cual es tu edad?: ")
 
eleccion = val.menu_inicio(name)

if eleccion == 1:
      print('=' * 30)
      time.sleep(0.5)
      income = float(input(f"¿Cuanto es tu ingreso semanal?:$"))
      val.ingresos_extras(name)
          
      time.sleep(0.5)
      yes_or_no = input('Tienes gastos fijos? si/no :')
      
      if yes_or_no.lower() == "si":
           print('=' * 50)
           time.sleep(0.5)
           gastos_fixed = float(input(f"¿Cueles son tus gatos fijos?:$"))
           user_choice = val.opciones_ganancia()
           
           if user_choice == '1':
            #Calculos para ver la ganancia mensual y anuel.Dolares
                  val.calculos_Dolares(income,name)
             
                  if income >= 100 and age <= 16:
                       print(f"Excelente capital  a tus {age} años {name}")
                  else:
                       print(f"Tienes que aumentar tu capital\npara tener liberta financiera")    
                       exito =input(f"Quieres tener exito? si/no: ")
                       if exito.lower() == "si":
                              print('=' * 50 )
                              mot.exito_m()
                              print(f"Tienes que tener todo esto para ser exitoso") 
                              print(f"Para tener exito no depende de tener plata sino valores {name}")
                  
                       else:
                        print(f"{name} como que no quieres ser exito y cumplir tus metas") 
            
           else:
                 #Calculos para ver la ganancia mensual y anual
                mes = (income* 4) - gastos_fixed  * 4
                year = mes * 12 
                print('------ GANANCIA EN DORALES MENOS LOS GASTOS FIJOS --------') 
                print(f'_-_-_-_-_-_-_ {name} _-_-_-_-_-_-_ ')
                print()
      else:
         print("como no tienes gastos fijo es mejor para ser millonario")


elif eleccion == 2:     
        time.sleep(0.5)
        tasa_bcv = float(input(f"En cuanto esta el Bcv: "))
        time.sleep(0.5)
        ingreso =  float(input(f'Cuanto es tu ingreso semanal en bolivares?:bs'))
        gastos_fijos = input(f"Tienes gastos fijos? si/no: ")
    
        if gastos_fijos.lower() == "si":
              gastos_fijos = float(input(f"¿Cueles son tus gastos fijos?: "))
              user_choice= val.opciones_ganancia()

              if user_choice == "1":
                  val.calculos_financieros(ingreso,name,tasa_bcv)
            
                  if ingreso >= 100 and age <= 16:
                      print(f"Excelente capital  a tus {age} años {name}")
          
                  else:
                       print(f"Tienes que aumentar tu capital\npara tener liberta financiera")    
                       exito =input(f"Quieres tener exito? si/no: ")

                       if exito.lower() == "si":
                              mot.exito_m()
                              print(f"\nTienes que tener todo esto para ser exitoso") 
                              print(f"Para tener exito no depende de tener plata sino valores {name}")
                       else:
                            print(f"{name} como que no quieres ser exito y cumplir tus metas") 
    
        else:   
         print("\nComo no tienes gastos fijos")
       
else:
   print(f"Trabaje carajo")  
   
 
     
