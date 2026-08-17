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
      ---- Elige una Opcion ----"
     1.Cuanto ganas al mes y al año.
     2.Cuanto ganas al año y al mes restando tu gastos fijos. 
     -----------------------------------------------------""")   

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
              print(f"Capital semanal:{income}$|Capital al mes:{mes}$|Capital al año:{year}$")
              print("-" * 70)

def calculos_Bolivares(ingreso,name,tasa_bcv):
            mensual = ingreso * 4
            anual = mensual * 12
            sema_bcv = ingreso * tasa_bcv
            men_bcv = mensual * tasa_bcv
            anu_bcv = anual * tasa_bcv
            time.sleep(0.5)
            print('-------GANANCIA EN BOLIVARES -----')
            print(f'------ {name.capitalize()} ----')
            print(f"Capital semanal:{sema_bcv:,.2f}bs|Capital al mes:{men_bcv:,.2f}bs|Capital al año:{anu_bcv:,.2f}bs")
            print('=' * 70)
            