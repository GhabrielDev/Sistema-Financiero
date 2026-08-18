import time

def preguntar_numero(mensaje):
     while True:
      try:
          print("-" * 20)
          ege = input(f"{mensaje}")
          return float(ege)
      except ValueError:
          print("¡ERROR! Coloque numeros")

def mensaje(mensaje):
     while True:
       try:
          texto = input(mensaje).strip().capitalize()
          if not texto:
               raise ValueError("No puede estar vacio el texto")
          return texto
       except ValueError as e:
            print(f"Error {e} intente de nuevo por favor")

def opciones_ganancia():
     time.sleep(0.5)
     print("""
      ---- Elige una Opcion ----
     1.Cuanto ganas al mes y al año.
     2.Cuanto ganas al año y al mes restando tu gastos fijos. 
     -----------------------------------------------------""")   
     while True:
                time.sleep(0.5)
                opciones = input(f"Selecciona el 1 o el 2: ")
                if opciones in ["1","2"]:
                     break
                else:
                    print("Intente de nuevo")
          
     return opciones            

def menu_inicio(nombre):
     while True:
        time.sleep(0.5)
        print("""---- MENU PRINCIPAL ----
      1.Ganancia en dolares
      2.Ganancia en Bolivares
      3.Anbas Ganancias""")
        try:
            choice = int(input(f'{nombre.capitalize()} selecciona un numero: '))
            if choice in [1,2,3]:
              return choice
            else:
              print("ERROR por favor elige una opcion valida (1,2,3).")
              print("-" * 30)
         
        except ValueError:
            print('Por favor Ingrese un numero valido,intente de nuevo')
            print("-" * 30)

def calculos_Dolares(income,name):
              mes = income * 4
              year = mes * 12
              time.sleep(0.5)
              print('------GANANCIA EN DOLARES -----')
              print(f'------ {name.capitalize()} ---- ')
              print(f"Capital semanal:{income}$\nCapital al mes:{mes}$\nCapital al año:{year}$")
              print("-" * 50)

def calculos_Bolivares(ingreso,name,tasa_bcv):
            mensual = ingreso * 4
            anual = mensual * 12
            sema_bcv = ingreso * tasa_bcv
            men_bcv = mensual * tasa_bcv
            anu_bcv = anual * tasa_bcv
            time.sleep(0.5)
            print('-------GANANCIA EN BOLIVARES -----')
            print(f'------ {name} ----')
            print(f"Capital semanal:{sema_bcv:,.2f}bs\nCapital al mes:{men_bcv:,.2f}bs\nCapital al año:{anu_bcv:,.2f}bs")
            print('=' * 50)

def calculos_menos_gastos_fijo(ingreso,name,tasa_bcv,gastos_fixed,income):
                mes = (income* 4) - gastos_fixed  * 4
                year = mes * 12 
                print('------ GANANCIA EN DORALES MENOS LOS GASTOS FIJOS --------') 
                print(f'_-_-_-_-_-_-_ {name} _-_-_-_-_-_-_ ')
                print(f"Capital semanal:\nCapital al mes:\nCapital al añó:")
                print('= * 50')


def ingresos_extras(name):
 datos=[]
 while True: 
     try:
        print('=' * 30)
        time.sleep(0.5)
        extras = input(f"Tienes ingresos extras {name} si/no?:")
        
        if extras.lower() == 'si':
          while True:
              try:
                  print('--- Escriba ''listo'' cuando ya ingrese todos sus ingresos extras ---')
                  entrada = input(f'Ingrese su ingreso extra:$')

                  if entrada.lower() == 'listo':
                       break
                  monto = float(entrada)
                  datos.append(monto)
              except ValueError as e:
                 print(f"Por favor ingrese numeros:{e}")  
          break
           
        elif extras.lower() == "no":
                  break
        else:
           print(f"Opcion invalida coloque si/no")
     except:
        print("Error intente de nuevo")           
     
 return datos

