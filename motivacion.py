import random as rd
def exito_m():
    key_of_the_exito = ["Resistencia","Constancia","Intencidad","Tener una rutina","Desarrollar Mentalidad de exito","Solucionar Problemas,Diciplina"]
    for e in key_of_the_exito:
         print(f'El exito es:{e}')
    return

def frase_millonaria():
     frase = ["El precio de la disciplina siempre es menor que el dolor del arrepentimiento.","No midas tu riqueza por el dinero que tienes, mídela por las habilidades que has construido y que nadie te puede quitar.","El éxito no se persigue; se atrae por la persona en la que te conviertes mientras trabajas en tus metas.","Los aficionados esperan tener motivación; los profesionales se levantan y construyen una rutina sin importar cómo se sientan.","Tu mente es tu activo más valioso. Si la alimentas con educación, constancia y solución de problemas, tu bolsillo se encargará del resto."]
     seleccion = rd.choice(frase)
     return seleccion