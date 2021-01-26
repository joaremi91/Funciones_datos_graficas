# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:14:01 2021

@author: jrequena
"""

"Importar librerias necesarias"
import pandas as pd    
import numpy as np


def extraccion_datos(ruta):
    
    "Extraer datos y declarar matrices"
    
    datos= pd.read_csv(ruta,sep="\t")

    Ventilador1=datos['VENTILADOR1']
    Ventilador2=datos['VENTILADOR2']
    Revoluciones=datos['Revoluciones']
    Potencia=datos['KW+']
    Par=datos['Par']
    TEMP_MKE=datos['TEMP_MKE']
    Fases=datos['Pattern Phase']
    KICK_DOWN1=datos['KICK-DOWN1']
    KICK_DOWN2=datos['KICK-DOWN2']
    
    
    
    'Puntos de temperatura'
    datos= pd.read_csv(ruta,sep="\t")
    Ventilador1=datos['VENTILADOR1']
    Ventilador2=datos['VENTILADOR2']
    TEMP_MKE=datos['TEMP_MKE']
    Fases=datos['Pattern Phase']

    Vent1_puntos=np.zeros([len(Ventilador1),2])#matriz de los puntos donde se enchufa y se apaga el ventilador
    Vent2_puntos=np.zeros([len(Ventilador2),2])#matriz de los puntos donde se enchufa y se apaga el ventilador
    i1=0
    i2=0
    for z in range(1, len(Ventilador1),1):
        if Ventilador1[z]!=Ventilador1[z-1] and (Fases[z]== 'F0- TABLA CONEX VENTIADORES'or Fases[z]=='F0- TABLA DESCONEX VENTIADORES'):#Ventilador1.diff() funcion diferencial
            Vent1_puntos[i1,0]=TEMP_MKE[z]
            Vent1_puntos[i1,1]=z        
            i1=i1+1
        if Ventilador2[z]!=Ventilador2[z-1] and (Fases[z]== 'F0- TABLA CONEX VENTIADORES'or Fases[z]=='F0- TABLA DESCONEX VENTIADORES'):
            Vent2_puntos[i2,0]=TEMP_MKE[z]
            Vent2_puntos[i2,1]=z        
            i2=i2+1
           

    

    'Puntos de Kick-down1 y Kick-down2 '
    datos= pd.read_csv(ruta,sep="\t")
    KICK_DOWN1=datos['KICK-DOWN1']
    KICK_DOWN2=datos['KICK-DOWN2']
    Par=datos['Par']
    Fases=datos['Pattern Phase']
    Kick_down1_puntos=np.zeros([len(KICK_DOWN1),2])#matriz de los puntos donde se enchufa y se apaga el kick-down1
    Kick_down2_puntos=np.zeros([len(KICK_DOWN2),2])#matriz de los puntos donde se enchufa y se apaga el kick-down2
    i3=0
    i4=0
    for z in range(1, len(KICK_DOWN1),1):
        if KICK_DOWN1[z]!=KICK_DOWN1[z-1] and (Fases[z]== 'F1_APROXIMACION KD1'or Fases[z]=='F1_TABLA CONEX KICKDOWN 1'):
            Kick_down1_puntos[i3,0]=Par[z]
            Kick_down1_puntos[i3,1]=z        
            i3=i3+1
        if KICK_DOWN2[z]!=KICK_DOWN2[z-1] and (Fases[z]== 'F2_APROXIMACION KD2'or Fases[z]=='F2_TABLA CONEX KICKDOWN 2'):
            Kick_down2_puntos[i4,0]=Par[z]
            Kick_down2_puntos[i4,1]=z        
            i4=i4+1      


        
    'Puntos caida de potencia temperatura'
    datos= pd.read_csv(ruta,sep="\t")
    KICK_DOWN1=datos['KICK-DOWN1']
    KICK_DOWN2=datos['KICK-DOWN2']
    Potencia=datos['KW+']
    Fases=datos['Pattern Phase']
    TEMP_MKE=datos['TEMP_MKE']
    
    Potencia_puntos=np.zeros([len(KICK_DOWN2),3])#matriz de los puntos donde baja la potencia en funcion de la temperatura
    i5=0  
    for z in range(0, len(Potencia),1):
        if Fases[z]== 'F3_TABLA_PERD. POT':
            Potencia_puntos[i5,0]=Potencia[z]
            Potencia_puntos[i5,1]=z
            Potencia_puntos[i5,2]=i5         
            i5=i5+1
        
    #buscamos el máximo y mínimo y su posicion
    Max_perdida=np.zeros([1,3])
    Min_perdida=np.zeros([1,3])
          
    Max_perdida[0,0]=np.amax(Potencia_puntos[:i5,0])
    Min_perdida[0,0]=np.amin(Potencia_puntos[:i5,0])


    Max_perdida[0,1]=Potencia_puntos[np.argmax(Potencia_puntos[:i5,0]),2]      
    Min_perdida[0,1]=Potencia_puntos[np.argmin(Potencia_puntos[:i5,0]),2]

    Max_perdida[0,2]=Potencia_puntos[np.argmax(Potencia_puntos[:i5,0]),1]      
    Min_perdida[0,2]=Potencia_puntos[np.argmin(Potencia_puntos[:i5,0]),1]


    Temp_max_perdida=TEMP_MKE[Max_perdida[0,2]]
    Temp_min_perdida=TEMP_MKE[Min_perdida[0,2]]    



    "Rampa desconexión 1200rpm"
    datos= pd.read_csv(ruta,sep="\t")
    Fases=datos['Pattern Phase']
    Potencia=datos['KW+']
    Desconexion_1200=np.zeros(len(Fases))
    i6=0  
    for z in range(0, len(Potencia),1):
        if Fases[z]=='F7_TABLA_DESC. VENTILA 1200':
            Desconexion_1200[i6]=z        
            i6=i6+1        
             


    "Rampa desconexión 1400rpm"
    datos= pd.read_csv(ruta,sep="\t")
    Fases=datos['Pattern Phase']
    Potencia=datos['KW+']    
    Desconexion_1400=np.zeros(len(Fases))
    i7=0  
    for z in range(0, len(Potencia),1):
        if Fases[z]=='F9_TABLA_DESC. VENTILA 1400':
            Desconexion_1400[i7]=z        
            i7=i7+1 
     

        
       
    "Prueba regulador"
    datos= pd.read_csv(ruta,sep="\t")
    Fases=datos['Pattern Phase']
    Potencia=datos['KW+']
    Regulador=np.zeros(len(Fases))
    i8=0
    for z in range(0, len(Potencia),1):
        if Fases[z]=='F5_PRB REGULADOR':
            Regulador[i8]=z        
            i8=i8+1  
    
    d={
       "Ventilador1": Ventilador1,
       "Ventilador2": Ventilador2,
       "Revoluciones": Revoluciones,
       "Potencia": Potencia,
       "Par": Par,
       "TEMP_MKE": TEMP_MKE,
       "Fases": Fases,
       "KICK_DOWN1":KICK_DOWN1,
       "KICK_DOWN2":KICK_DOWN2,
       "Regulador": Regulador,
       "Desconexion_1400":Desconexion_1400,
       "Desconexion_1200":Desconexion_1200,
       "Temp_max_perdida":Temp_max_perdida,
       "Temp_min_perdida":Temp_min_perdida,
       "Max_perdida":Max_perdida,
       "Min_perdida":Min_perdida,
       "Kick_down1_puntos":Kick_down1_puntos,
       "Kick_down2_puntos":Kick_down2_puntos,
       "Vent1_puntos":Vent1_puntos,
       "Vent2_puntos":Vent2_puntos,
       "Potencia_puntos":Potencia_puntos,
       "i1":i1,
       "i2":i2,
       "i3":i3,
       "i4":i4,
       "i5":i5,
       "i6":i6,
       "i7":i7,
       "i8":i8    
       }
    return d