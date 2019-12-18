import turtle as t
import math
a = int(input("Escreva o valor de lados: "))
b = 180/a

if a<3:
    print("Não forma um poligono.")
else:    
    d = math.cos(math.radians(180/(2*a)))
    d2 = math.sin(math.radians(180/(2*a)))
    
    area = ((200*d2)*(500*d))/2
    areap = area*a
    perimetro = (200*d2)*a
    pi = (perimetro*2)/(200*d)
    
    print("\n|------------------------------------------|")
    print("  Perimetro: %.2f"%perimetro)
    print("  Altura: %.2f"%(200*d))
    print("  Area do poligono: %.2f"%areap)
    print("  Valor de pi: %.15f"%pi)
    print("|------------------------------------------|")
    
    soma = (a-2)*180
    g = (soma/a)
    f = 180-g
    
    while(0<=a):   
        t.fd(200*d2)
        t.rt(f)
        a+=-1
       
        


    
