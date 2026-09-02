#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel
#* Programa para procesar modelos lineales mediante correlación por cuadrados mínimos
#* 
#* UADER - FCyT
#* Ingeniería de Software II
#*
#* Dr. Pedro E. Colla
#* copyright (c) 2023,2024
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=

import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Almacena dataset histórico
#*------------------------------------------------------------------------------------------------

data = {
    'LOC': [794, 1336, 1572, 1572, 1126],
    'Esfuerzo': [1.07, 1.34, 2.27, 2.39, 0.93]
}

#*------------------------------------------------------------------------------------------------
#* Inicialización del programa
#*------------------------------------------------------------------------------------------------

version="7.0"
linear=False
exponential=False

# Modificado para Windows
os.system('cls')

#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version",required=False,help="version",action="store_true")
ap.add_argument("-x", "--exponential", required=False,help="Exponential model",action="store_true")
ap.add_argument("-l", "--linear", required=False,help="Linear model",action="store_true")

# Punto 9.b - permite indicar LOC de un nuevo proyecto
ap.add_argument("-c", "--loc", required=False, help="Complejidad del proyecto en LOC")

args = vars(ap.parse_args())

if args['version'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   sys.exit(0)

if args['linear'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Linear correlation model selected")
   linear=True

if args['exponential'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Exponential correlation model selected")
   exponential=True

if linear==False and exponential==False:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

#*-----------------------------------------------------------------------------------------------
#* Definir dataset y procesar correlación entre LOC (complejidad) y Esfuerzo (PM)
#*-----------------------------------------------------------------------------------------------

df = pd.DataFrame(data)
correlation = df['LOC'].corr(df['Esfuerzo'])

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal, usa numpy polyfit()
#*------------------------------------------------------------------------------------------------

if linear==True:

   a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
   R = np.corrcoef(df['LOC'], df['Esfuerzo'], 1)
   R2=R*R
   r_value=R2[1][0]

   print("Modelo lineal E=%.6f + %.6f*LOC)" % (b,a))
   print("El R-squared=%.4f (lineal)" % (r_value))

   # Punto 9.b - estima esfuerzo para un LOC ingresado
   if args['loc'] is not None:
      loc_nuevo = float(args['loc'])
      esfuerzo_estimado = a * loc_nuevo + b

      print("Para LOC=%.0f se estima un esfuerzo de %.2f PM" %
            (loc_nuevo, esfuerzo_estimado))

      plt.scatter(
         loc_nuevo,
         esfuerzo_estimado,
         label='Proyecto estimado LOC=%.0f' % loc_nuevo,
         marker='x',
         s=100
      )

   lbl=("modelo lineal (R-Sq=%.2f)" % (r_value))

   # Si se indicó un LOC, extiende la recta hasta ese valor
   if args['loc'] is not None:
      x_modelo = np.linspace(min(df['LOC']), loc_nuevo, 100)
   else:
      x_modelo = df['LOC']

   plt.plot(x_modelo, a*x_modelo+b,label=lbl,color='red')

#*------------------------------------------------------------------------------------------------
#* procesa modelo exponencial utiliza OLS fit()
#*------------------------------------------------------------------------------------------------

if exponential==True:

   df['logEsfuerzo']=np.log(df['Esfuerzo'])
   df['logLOC']=np.log(df['LOC'])

   X = df['logLOC']
   Y = df['logEsfuerzo']
   X = sm.add_constant(X)  # Añadir una constante para el intercepto

   mx= sm.OLS(Y, X).fit()
   print(mx.summary())

   k=np.exp(mx.params['const'])
   b=mx.params['logLOC']

   print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k,b))
   print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

   lbl=("modelo exponencial (R-Sq=%.2f)" % (mx.rsquared))

   plt.plot(
      df['LOC'],
      k*(df['LOC']**b),
      label=lbl,
      color='green'
   )

#*------------------------------------------------------------------------------------------------
#* Hace plot del dataset histórico
#*------------------------------------------------------------------------------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()
