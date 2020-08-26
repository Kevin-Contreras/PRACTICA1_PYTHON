from argparse import  ArgumentParser
from pathlib import Path
import json
from string import Template
import webbrowser as wb
archivoHTML = open("index.html")
temple = Template(archivoHTML.read())
cargarDatos = input()

def cargar(datos):

  if datos.find("CARGAR") == 0:
    remplazable = datos.replace("CARGAR","")
    print (remplazable.split())
    mypath = Path().absolute()
    for nombreArchivo in remplazable.split():
      with open(nombreArchivo) as archivoJson:
        jsonArchivo = json.load(archivoJson)
        print("SE HA CARGADO EL ARCHIVO")         

cargar(cargarDatos)

def procesos(datos):
  remplazable = datos.replace("CARGAR","")
  while True:
    proceso = input()

    if proceso.find("SELECCIONAR") == 0:
       if proceso.find("SELECCIONAR *")== 0:
        for nombreArchivo in remplazable.split():
          with open(nombreArchivo) as archivoJson:
            jsonArchivo = json.load(archivoJson)
            for linea in jsonArchivo:
              print ("nombre: "+str(linea.get("nombre")))
              print ("edad "+str(linea.get("edad")))
              print ("activo: "+str(linea.get("activo")))
              print ("promedio: "+ str(linea.get("promedio"))) 
       elif proceso.find("SELECCIONAR nombre, edad, promedio, activo DONDE nombre =")==0:
                        
        nuevo = proceso.replace("SELECCIONAR nombre, edad, promedio, activo DONDE nombre =","")
        sincomillas = nuevo.strip('"')
       
        for nombreArchivo in remplazable.split():
          with open(nombreArchivo) as archivoJson:
            jsonArchivo = json.load(archivoJson)
            for linea in jsonArchivo:
              if linea.get("nombre") == sincomillas:
                print ("nombre: "+str(linea.get("nombre")))
                print ("edad "+str(linea.get("edad")))
                print ("activo: "+str(linea.get("activo")))
                print ("promedio: "+ str(linea.get("promedio")))
       elif proceso.find("SELECCIONAR nombre, edad DONDE promedio")==0:
         nuevo2 = proceso.replace("SELECCIONAR nombre, edad DONDE promedio = ","")
         for nombreArchivo in remplazable.split():
          with open(nombreArchivo) as archivoJson:
            jsonArchivo = json.load(archivoJson)
            for linea in jsonArchivo:
              if str(linea.get("promedio")) == nuevo2 :
                print ("nombre: "+str(linea.get("nombre")))
                print ("edad: "+str(linea.get("edad")))
    elif proceso.find("MAXIMO edad") == 0:
      lista =[]
      n =0
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)

          for linea in jsonArchivo:
            lista.append(linea.get("edad"))
      print(max(lista))
    elif proceso.find("MAXIMO promedio") == 0:
      listaPromedio =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)

          for linea in jsonArchivo:
            listaPromedio.append(linea.get("promedio"))
      print(max(listaPromedio))  
    elif proceso.find("MINIMO edad") == 0:
      listaEdad =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)

          for linea in jsonArchivo:
            listaEdad.append(linea.get("edad"))
      print(min(listaEdad))  
    elif proceso.find("MINIMO promedio") == 0:
      listaPromedioMinimo =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)

          for linea in jsonArchivo:
            listaPromedioMinimo.append(linea.get("promedio"))
      print(min(listaPromedioMinimo))
    elif proceso.find("SUMA edad") == 0:
      incremento=0
      listaSumaEdad =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)
          for linea in jsonArchivo:
            listaSumaEdad.append(linea.get("edad"))
      for edad in listaSumaEdad:
        incremento = incremento + edad
      print(incremento)  
    elif proceso.find("SUMA promedio") == 0:
      incrementos=0
      listaSumaPromedio =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)
          for linea in jsonArchivo:
            listaSumaPromedio.append(linea.get("promedio"))
      for promedio in listaSumaPromedio:
        incrementos = incrementos + promedio
      print(incrementos)
    elif proceso.find("CUENTA") == 0:
      incrementoCuenta=0
      listaSumaPromedio =[]
      for nombreArchivo in remplazable.split():
        with open(nombreArchivo) as archivoJson:
          jsonArchivo = json.load(archivoJson)
          for linea in jsonArchivo:
            incrementoCuenta = 1 + incrementoCuenta 
      print(incrementoCuenta) 
    elif proceso.find("REPORTE")== 0:
      incrementoNumero=0
      nombres =""
      edad = ""
      activo = ""
      promedio = "" 
      numero = proceso.replace("REPORTE ","")
      for nombreArchivo in remplazable.split():
          with open(nombreArchivo) as archivoJson:
            jsonArchivo = json.load(archivoJson)
            for linea in jsonArchivo:
              if int (numero)-1>=incrementoNumero:
                nombres = nombres + str(linea.get("nombre"))+ " "
                edad = edad + str(linea.get("edad")) +" "
                activo = activo + str(linea.get("activo")) + " "
                promedio = promedio + str(linea.get("promedio")) + " "
                incrementoNumero = 1+ incrementoNumero

      for i in range(int(numero)):
        if int(numero) == 1:
          file2 = open("json.html","w")
          resultado = temple.substitute({'nombre':nombres, 'edad': edad, 'activa':activo, 'promedio': promedio})
          file2.writelines(resultado) 
        file2 = open("json.html","w")
        resultado = temple.substitute({'nombre':nombres, 'edad': edad, 'activa':activo, 'promedio': promedio})
        file2.writelines(resultado)
      wb.open_new("json.html")  



procesos(cargarDatos)      
