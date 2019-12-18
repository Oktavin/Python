import visual as vis
import math


#Aqui definimos as propriedades do plano 3D:
centro = vis.vector(0,0,0)
Plano = vis.vector(15, 15, 15)

#Aqui definimos as propriedades do display:
cena1 = vis.display(title = "Projeto: Beta 4", x = 0, y = 0,\
  width = 500, height = 500, background=(0,0,0), \
  center = centro, range = Plano)

#Esses sao vetores para orientacao:
#vis.arrow(pos=(0,0,0), axis=(0,0,10), shaftwidth=0.5, display=cena1,color=(0,0,1))
#vis.arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.5, display=cena1)
#vis.arrow(pos=(0,0,0), axis=(0,10,0), shaftwidth=0.5, display=cena1, color=(1,0,0))
#flash = vis.arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.5, display=cena1,color=(0,1,0))
#Aqui sao as propriedades do cubo que nao estao no laco:
cubo = vis.box(pos = centro,color = (0,1,1),opacity = 1)

loop = 2
contaVoltas = 0
c = 0
d = 0
e = 0

while True:
    if(c>1):
        d = 1
    else:
        if(c==0):
            d=0
     
    #Aqui definimos que o "t" sempre voltara a ser zero no inicio do laco.
    t = 0
    #Com "if" definimos o criterio p/loop, dividindo o numero de voltas pelo loop.
    if(contaVoltas==0):
        #"t" soma 30 ate 360.
        for t in range(360):
            
            #Aqui definimos as coordenadas do vetor: 
            b = math.cos(math.radians(t))
            a = math.sin(math.radians(t))

            #Aqui eu defino as propriedades do cubo:        
            vis.rate(100)        
            #cubo.axis = (1,0,0)
            cubo.axis = (b,a,e)
            cubo.height = 4
            cubo.width = 3
            cubo.length = 2
            
            #O "t" ira¡ somar 30 graus ate completar uma volta completa.    
            t+=+30
            e+=-0.0015
    else:
        if(contaVoltas%loop==0):
        #"t" soma 30 ate 360.
             for t in range(360):           
                    #Aqui definimos as coordenadas do vetor: 
                    b = math.cos(math.radians(t))
                    a = math.sin(math.radians(t))
                    #Aqui eu defino as propriedades do cubo:        
                    vis.rate(100)        
                    #cubo.axis = (1,0,0)
                    cubo.axis = (b,a,a-0.5)
                    cubo.height = 4
                    cubo.width = 3
                    cubo.length = 2
            
                    #O "t" ira¡ somar 30 graus ate completar uma volta completa.    
                    t+=+30
                    if(d==1):
                        c+=-0.1
                    else:
                        if(d==0):
                            c+=+0.1
                    
        else:
            for t in range(360):           
                    #Aqui definimos as coordenadas do vetor: 
                    b = math.cos(math.radians(t))
                    a = math.sin(math.radians(t))
                    #Aqui eu defino as propriedades do cubo:        
                    vis.rate(100)        
                    #cubo.axis = (1,0,0)
                    cubo.axis = (b,a,a-0.4)
                    cubo.height = 4
                    cubo.width = 3
                    cubo.length = 2
            
                    #O "t" ira¡ somar 30 graus ate completar uma volta completa.    
                    t+=+30
                    if(d==1):
                        c+=-0.1
                    else:
                        if(d==0):
                            c+=+0.1
                
                
        #Aqui somamos as voltas.
    contaVoltas+=+1
    
    
        
            
    
    
    
   
 

    









    
    
    
