# -*- coding: cp1252 -*-
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import visual as vis
import numpy as np
from random import randint
from visual import *
 
centro = vis.vector(0,0,0)
raio   = 5

centroCena  = centro
larguraCena = vis.vector(10, 10, 10)
 
cena1 = vis.display(title="Encounter", x=0, y=0,\
  width=1000, height=800, background=(1,1,1), \
  center=centroCena, range=larguraCena)

#Esses sao vetores para orientacao:
vis.arrow(pos=(0,0,0), axis=(0,0,10), shaftwidth=0.5, display=cena1,color=(0,0,1))
#vis.arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.5, display=cena1)
vis.arrow(pos=(0,0,0), axis=(0,10,0), shaftwidth=0.5, display=cena1, color=(1,0,0))
flash = vis.arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.5, display=cena1,color=(0,1,0))

#Aqui defini-se o formato, tamanho e o material para a Terra. 
esfera1 = vis.sphere(pos=centro, radius=raio,material = materials.earth,opacity=1, \
  display=cena1)

#O raio 'r' das esferas 1 (verde) e 2 (vermelha) sao padronizados neste local
#nao somente o raio como tambem a cor e o formato das esferas menores
r = 0.8
bola1 = vis.sphere( radius=r,\
  color=(1,0,0), display=cena1)
bola2 = vis.sphere( radius=r,\
  color=(0,1,0), display=cena1)

for b in range(100):
    a = (randint(1,2))
    c = (randint(1,2))
    while c != a:
        if(a==1):
            vis.rate(55)
            x = (5+r)*np.sin(b)
            y = (5+r)*np.cos(b)
            z = 0
            novaPos = vis.vector(x, y, z) 
            bola1.pos = novaPos
            b+=0.01
        
        else:
            if(a==2):
                vis.rate(55)
                b+=0.01
                x = 0
                y = 6.0*np.sin(b)
                z = 6.0*np.cos(b)
    
                novaPos = vis.vector(x, y, z) 
                bola1.pos = novaPos



        if(c==1):
            vis.rate(55)
            x = 6.0*np.sin(b)
            y = 6.0*np.cos(b)
            z = 0
            novaPos = vis.vector(x, y, z) 
            bola2.pos = novaPos
            b+=0.01
        
        else:
            if(c==2):
                vis.rate(55)
                b+=0.01
                q = 0
                w = 6.0*np.sin(b)
                e = 6.0*np.cos(b)
    
                novaPos = vis.vector(q, w, e) 
                bola2.pos = novaPos
        #Neste local define-se os "contadores"; eles avisam ao usuario se houve o encontro entra a bola1 e 2
        #Enquanto nenhuma delas se encontrarem, uma mensagem será mostrada na tela
        if (c == a):
            progress_end = label(pos=(-4,4,3), background=(-3,0,1),text = 'Se encontraram!!')
            break

        else:
            progress_procura = label(pos=(-6,2,3), background=(-3,0,1),text = 'Procurando...')
                

#progress_1 = label(pos=(-6,2,3), background=(-3,0,1), text = 'Ainda nao se encontraram! Clique para continuar procurando')
