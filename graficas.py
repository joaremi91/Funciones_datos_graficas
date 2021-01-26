# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:31:56 2021

@author: jrequena
"""
"Importar librerias necesarias"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
    
    
    

def graficos(d):    
    
    Ventilador1= d['Ventilador1']
    Ventilador2= d['Ventilador2']
    Revoluciones=d['Revoluciones']
    Potencia=d['Potencia']
    Par=d['Par']
    TEMP_MKE=d['TEMP_MKE']
    KICK_DOWN1=d['KICK_DOWN1']
    KICK_DOWN2=d['KICK_DOWN2']
    Regulador=d['Regulador']
    Desconexion_1400=d['Desconexion_1400']
    Desconexion_1200=d['Desconexion_1200']
    Temp_max_perdida=d['Temp_max_perdida']
    Temp_min_perdida=d['Temp_min_perdida']
    Max_perdida=d['Max_perdida']
    Min_perdida=d['Min_perdida']
    Vent1_puntos=d['Vent1_puntos']
    Vent2_puntos=d['Vent2_puntos']
    Kick_down1_puntos=d['Kick_down1_puntos']
    Kick_down2_puntos=d['Kick_down2_puntos']
    Potencia_puntos=d['Potencia_puntos']
    i1=d['i1']
    i2=d['i2']
    i3=d['i3']
    i4=d['i4']
    i5=d['i5']
    i6=d['i6']
    i7=d['i7']
    i8=d['i8']
    
    y1=np.zeros(i1)
    y2=np.zeros(i2)

#%%
    'Conexión/desconexión ventiladores'
    Ventilador_graf= plt.figure(figsize=(15,10))

    ax0=plt.subplot(311)
    P=ax0.plot(np.linspace(0, len(Potencia), len(Potencia), endpoint=True), Potencia,'tab:cyan', label='Potencia real')
    #plt.legend(loc='center right')
    plt.ylabel('Potencia (kW)')
    plt.xlabel('Número de muestreo')
    ax0.grid(True)

    ax1 = ax0.twinx()

    T=ax1.plot(np.linspace(0, len(Potencia), len(Potencia), endpoint=True), TEMP_MKE,'crimson', label='Temperatura')
    plt.ylabel('Temperatura (°C)')
    #plt.legend(loc='best')
    lns = T+P
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs,bbox_to_anchor=(1,0.6,0,0.2),loc='upper right')



    plt.subplot(312)
    plt.plot(np.linspace(0, len(Ventilador1), len(Ventilador1), endpoint=True), Ventilador1,'orange', label='Ventilador 1')
    plt.plot(Vent1_puntos[0:i1,1],y1+1,'go',label='Con/des')


    plt.grid(True)
    plt.legend(loc='best')
    plt.ylabel('Estado ventilador 1')
    plt.xlabel('Número de muestreo')

    plt.subplot(313)
    plt.plot(np.linspace(0, len(Ventilador2), len(Ventilador2), endpoint=True), Ventilador2, label='Ventilador 2')
    plt.plot(Vent2_puntos[0:i2,1],y2+1,'ro',label='Con/des')
    plt.legend(loc='best')
    plt.ylabel('Estado ventilador 2')
    plt.xlabel('Número de muestreo')
    plt.grid(True)



    columnas=('Temperatura Conexión (°C)','Temperatura desconexión (°C)')
    filas=('Ventilador 1','Ventilador 2')
    n_filas=i1
    y_offset = np.zeros(len(columnas))
    cellText = [[Vent1_puntos[0,0],Vent1_puntos[1,0]],[Vent2_puntos[0,0],Vent2_puntos[1,0]]]
    tabla = plt.table(cellText=cellText, rowLoc='right',
                 rowLabels=filas,
                 colWidths=[.5,.5], colLabels=columnas,
                 colLoc='center', loc='bottom',bbox=[0,-0.8,1,0.5],zorder=20)

    tabla.auto_set_font_size(True)
    tabla.scale(1,1)
    plt.grid(True)
    ax0.set_title('Conexión/desconexión de ventiladores', fontsize=16)

    plt.tight_layout()
    plt.savefig("Ventilador_graf.png", dpi = 1080)
 

    #%%
    'Conexión Kick-Down'
    y3=np.zeros(i3)
    y4=np.zeros(i4)

    Kic_down_graf, ax= plt.subplots(figsize=(15,10))
    ax=plt.subplot(311)
    P=ax.plot(np.linspace(0, len(Potencia), len(Potencia), endpoint=True), Potencia,'tab:cyan', label='Potencia')
    plt.ylabel('Potencia (kW)')
    ax1 = ax.twinx()

    T=ax1.plot(np.linspace(0, len(Par), len(Par), endpoint=True), Par,'crimson', label='Par')
    lns = T+P
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs,bbox_to_anchor=(1,0.6,0,0.2),loc='upper right')
    plt.ylabel('Par (N·m)')
    plt.xlabel('Número de muestreo')
    plt.grid(True)
    plt.xlabel('Número de muestreo')
    Kic_down_graf.suptitle('Conexión Kick-Down', y=1.002, fontsize=16)


    plt.subplot(312)
    plt.plot(np.linspace(0, len(KICK_DOWN1), len(KICK_DOWN1), endpoint=True), KICK_DOWN1,'orange', label='Kick-Down 1')
    plt.plot(Kick_down1_puntos[0:i3,1],y3+1,'go',label='Punto de conexión')


    plt.grid(True)
    plt.legend(loc='best')
    plt.ylabel('Estado Kick-Down 1')
    plt.xlabel('Número de muestreo')

    plt.subplot(313)
    plt.plot(np.linspace(0, len(KICK_DOWN2), len(KICK_DOWN2), endpoint=True), KICK_DOWN2,'b', label='Kick-Down 2')
    plt.plot(Kick_down2_puntos[0:i4,1],y4+1,'go',label='Punto de conexión')
    plt.legend(loc='best')
    plt.ylabel('Estado Kick-Down 2')
    plt.xlabel('Número de muestreo')

    columnas=('Par (N·m)','Potencia (kW)')
    filas=('Kick-Down 1','Kick-Down 2')
    n_filas=i4
    y_offset = np.zeros(len(columnas))
    cellText = [[int(Kick_down1_puntos[0,0]),int(Potencia[Kick_down1_puntos[0,1]])],[int(Kick_down2_puntos[0,0]),int(Potencia[Kick_down2_puntos[0,1]])]]
    tabla = plt.table(cellText=cellText, rowLoc='right',
                  rowLabels=filas,
                  colWidths=[.5,.5], colLabels=columnas,
                   colLoc='center', loc='bottom',bbox=[0,-0.8,1,0.5],zorder=20)

    tabla.auto_set_font_size(True)
    tabla.scale(1,1)
    plt.grid(True)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Kick_down_graf.png", dpi = 1080)



    #%%
    'Perdida potencia-temperatura'
    Perdida_potencia ,ax1= plt.subplots(figsize=(15,10))
    P=ax1.plot(Potencia_puntos[:i5,2], Potencia_puntos[:i5,0],'orange', label='Potencia real')
    plt.ylabel('Potencia(kW)')
    plt.xlabel('Número de muestra')
    plt.plot(Max_perdida[0,1],Max_perdida[0,0],'go',label='Máximo')
    plt.plot(Min_perdida[0,1],Min_perdida[0,0],'ro',label='Mínimo')

    ax2 = ax1.twinx()

    T=ax2.plot(Potencia_puntos[:i5,2], TEMP_MKE[Potencia_puntos[:i5,1]],'b', label='Temperatura MKE')
    plt.ylabel('Temperatura (°C)')
    lns = T+P
    labs = [l.get_label() for l in lns]
    Perdida_potencia.legend(lns, labs,bbox_to_anchor=(0.3,0.6,0,0.2),loc='best')
    ax1.yaxis.grid() # horizontal lines
    ax1.xaxis.grid() # vertical lines 
    columnas=('Potencia kW','Temperatura MKE (°C)')
    filas=('Máximo valor','VenMínimo valor')
    n_filas=2
    y_offset = np.zeros(len(columnas))
    cellText = [[round(Max_perdida[0,0],2),round(Temp_max_perdida,1)],[round(Min_perdida[0,0],2),round(Temp_min_perdida,1)]]
    tabla = plt.table(cellText=cellText, rowLoc='right',
                  rowLabels=filas,
                  colWidths=[.5,.5], colLabels=columnas,
                  colLoc='center', loc='bottom',bbox=[0,-0.6,1,0.4],zorder=20)

    tabla.auto_set_font_size(True)
    tabla.scale(1,1)
    plt.title('Pérdida de potencia', fontsize=16)
    plt.tight_layout()
    plt.savefig("Perdida_potencia.png", dpi = 1080)
 

    #%%
    'Gráfico desconexión 1200 rpm' 

    Des_1200_graf, ax= plt.subplots(figsize=(15,5))
    plt.subplot(311)
    plt.plot(Revoluciones[Desconexion_1200[0:i6]],'tab:cyan', label='RPM motor')
    plt.legend(loc='best')
    plt.ylabel('Revoluciones/minuto')
    plt.xlabel('Número de muestreo')
    plt.grid(True)

    plt.subplot(312)
    plt.plot(Ventilador1[Desconexion_1200[0:i6]],'r', label='Ventilador 1')
    plt.plot(Ventilador2[Desconexion_1200[0:i6]],'b--', label='Ventilador 2')



    plt.grid(True)
    plt.legend(loc='best')
    plt.ylabel('Estado Ventiladores')
    plt.xlabel('Número de muestreo')

    plt.subplot(313)
    plt.plot(KICK_DOWN1[Desconexion_1200[0:i6]],'r', label='KICK_DOWN1')
    plt.plot(KICK_DOWN1[Desconexion_1200[0:i6]],'b--', label='KICK_DOWN2')
    plt.legend(loc='best')
    plt.ylabel('Estado Kick-Down')
    plt.xlabel('Número de muestreo')


    plt.grid(True)
    Des_1200_graf.suptitle('Desconexión 1200 rpm',y=1, fontsize=16)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Des_1200_graf.png", dpi = 1080)


    #%%
    'Gráfico desconexión 1400 rpm' 

    Des_1400_graf=plt.figure(figsize=(15,5))
    ax0=plt.subplot(311)
    ax0.plot(Revoluciones[Desconexion_1400[0:i7]],'tab:cyan', label='RPM motor')
    ax0.legend(loc='best')
    ax0.set_ylabel('Revoluciones/minuto')
    ax0.set_xlabel('Número de muestreo')
    plt.grid(True)

    ax1=plt.subplot(312)
    ax1.plot(Ventilador1[Desconexion_1400[0:i7]],'r', label='Ventilador 1')
    ax1.plot(Ventilador2[Desconexion_1400[0:i7]],'b--', label='Ventilador 2')
    ax1.set_ylim([0,1.05])



    plt.grid(True)
    ax1.legend(loc='lower right')
    ax1.set_ylabel('Estado ventiladores')

    ax1.set_xlabel('Número de muestreo')

    ax2=plt.subplot(313)
    ax2.plot(KICK_DOWN1[Desconexion_1400[0:i7]],'r', label='Kick-Down 1')
    ax2.plot(KICK_DOWN1[Desconexion_1400[0:i7]],'b--', label='Kick-Down 2')
    ax2.legend(loc='best')
    ax2.set_ylabel('Estado Kick-Down')
    ax2.set_xlabel('Número de muestreo')


    plt.grid(True)
    Des_1400_graf.suptitle('Desconexión 1400 rpm', fontsize=16)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Des_1400_graf.png", dpi = 1080)


    #%%
    'Prueba regulador'
    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)


    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)

    p1, = host.plot(np.linspace(0, i8*5, i8),Potencia[Regulador[0:i8]],'r--', label='Potencia real')
    p2, = par1.plot(np.linspace(0, i8*5, i8),Par[Regulador[0:i8]],'b--', label='Par')
    p3, = par2.plot(np.linspace(0, i8*5, i8),Revoluciones[Regulador[0:i8]],'g', label='Revoluciones')



    host.set_xlabel("Tiempo (s)")
    host.set_ylabel("Potencia (kW)")
    par1.set_ylabel("Par (Nm)")
    par2.set_ylabel("Revoluciones (rpm)")



    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)



    lines = [p1, p2, p3]
    plt.title('Regulador 2680',fontsize=16)
    plt.grid(color='grey', linestyle='-.', linewidth=0.3)

    host.legend(lines, [l.get_label() for l in lines],loc='center right')

    plt.tight_layout()
    plt.title('Regulador 2680',fontsize=16)    
    plt.savefig("Regulador_2680.png", dpi = 1080)