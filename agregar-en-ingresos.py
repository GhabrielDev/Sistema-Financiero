import time

def ingresos_extras(name):
 datos=[]
 while True: 
     try:
        print('=' * 30)
        time.sleep(0.5)
        extras = input(f"Tienes ingresos extras {name} si/no?:")
        
        if extras.lower() == 'si':
          while True:
           print('--- Escriba ''listo'' cuando ya ingrese todos sus ingresos extras ---')
           entrada = input(f'Ingrese su ingreso extra:$')

           if entrada.lower() == 'listo':
             break
          monto = float(entrada)
          datos.append(monto)
        elif extras.lower() == "no":
         break
     except:
        print("Por favor ingrese numeros")      
 return datos
