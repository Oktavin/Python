# -*- coding: cp1252 -*-
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import visual as vis
import numpy as np
import math
from visual import *

#Aqui foi definido o tamanho do display da tela, assim como a
#definicao do centro do ambiente  
centro      = vis.vector(0,0,0)
centroCena  = centro
larguraCena = vis.vector(10, 10, 10)

cena1 = vis.display(title="Solar System alpha phase", x=0, y=0,\
                    width=1000, height=800)

#Neste local se define o vetor matriz 'v' que será usado
#para guiar os planetas/movimenta-los no espaço
v = vector(0.5,0,0)

#A posição,cor,raio e material do sol, Terra e Lua são definidos aqui
Sun = sphere(pos=(0,0,0), radius = 100, color = color.orange)
#Nota: para tirar as "trilhas" do Sol e Lua, basta colocar "make_trail = False"
Earth = sphere(pos=(200,0,0), radius = 15, material = materials.earth,
                       make_trail = True)
Moon = sphere(pos=(240,0,0), radius = 10, color = color.cyan,
              make_trail = True)
#Os vetores da Terra e da Lua são definidos neste pedaço do código
Earth.v = vector(0,-8,0)
Moon.v = vector(0.5,-3,0.3)

#Criou-se um loop para que os planetas girem infinitamente em torno do Sol
#o programa interrompe a rotação quando a Terra está quase a se chocar com o Sol
#Cada volta no Sol = 360º, a Terra precisa de 60.385 voltas para se chocar
#167 voltas vezes 360º são aproximadamente 60.385 voltas
for i in range(0,60385):
    rate(60)
    #Aqui teoricamente se iniciar a rotação da Lua em torno do Sol
    
    #calculo da distancia da lua com o centro
    dist_M = (Moon.x**2 + Moon.y**2 + Moon.z**2)**0.5
    #raio do vetor da lua 
    radialVector_2 = (Earth.pos - Moon.pos)/dist_M
    #inicio do circulo sobre a terra para com a Lua. Nota: 'EM' = Earth-Moon
    Fgrav_EM = 10000*radialVector_2/dist_M**2
    #Os vetores são somados aqui, eles funcionam como uma força centrípeta
    #de modo que a Lua fica incapaz de sair da elipse 
    Moon.v += Fgrav_EM*2
    Moon.pos += Earth.v
    
    #Já neste local inicia-se a rotação da Terra em torno do Sol
    #É praticamente o mesmo código que o da Lua, apenas substituimos o
    #vetor da Lua pelo do Sol e o da Terra
    rate(60)
    dist = (Earth.x**2 + Earth.y**2 + Earth.z**2)**0.5
    radialVector = (Sun.pos - Earth.pos)/dist
    #Aqui se define a elipse e a simulacao da gravidade
    Fgrav = 10000*radialVector/dist**2
    Earth.v += Fgrav
    Earth.pos += Earth.v

    #Neste local definimos um limite até onde a Terra poderia se aproximar da lua
    if dist <= Sun.radius: break
    #Enquanto que aqui o limite é para que a Lua não se choque/aproxime com a Terra
    if dist_M <= Earth.radius: break

