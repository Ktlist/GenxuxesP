import os
import random
n_iter=300

LabelSW = {
    "cocacola":0,
    "corazon":1,
    "dedo":2,
    "fresa":3,
    "jamon":4,
    "mora":5,
    "nube":6,
    "platano":7,
    "taco":8,
    "tarta":9
}


#os.system("mkdir ~/Resultados_Genxuxes/cocacola")
#os.system("python3 ./Genxuxes.py -i1 cocacola -i2 cocacola -n 5500 -m False -d ~/Resultados_Genxuxes/cocacola ")
#os.system("mkdir ~/Resultados_Genxuxes/corazon")
#os.system("python3 ./Genxuxes.py -i1 corazon -i2 corazon -n 5500 -m False -d ~/Resultados_Genxuxes/corazon ")
#os.system("mkdir ~/Resultados_Genxuxes/dedo")
#os.system("python3 ./Genxuxes.py -i1 dedo -i2 dedo -n 5500 -m False -d ~/Resultados_Genxuxes/dedo ")
#os.system("mkdir ~/Resultados_Genxuxes/fresa")
#os.system("python3 ./Genxuxes.py -i1 fresa -i2 fresa -n 5500 -m False -d ~/Resultados_Genxuxes/fresa ")
#os.system("mkdir ~/Resultados_Genxuxes/jamon")
#os.system("python3 ./Genxuxes.py -i1 jamon -i2 jamon -n 5500 -m False -d ~/Resultados_Genxuxes/jamon ")
#os.system("mkdir ~/Resultados_Genxuxes/mora")
#os.system("python3 ./Genxuxes.py -i1 mora -i2 mora -n 5500 -m False -d ~/Resultados_Genxuxes/mora ")
#os.system("mkdir ~/Resultados_Genxuxes/nube")
#os.system("python3 ./Genxuxes.py -i1 nube -i2 nube -n 5500 -m False -d ~/Resultados_Genxuxes/nube ")
#os.system("mkdir ~/Resultados_Genxuxes/platano")
#os.system("python3 ./Genxuxes.py -i1 platano -i2 platano -n 5500 -m False -d ~/Resultados_Genxuxes/platano ")
#os.system("mkdir ~/Resultados_Genxuxes/taco")
#os.system("python3 ./Genxuxes.py -i1 taco -i2 taco -n 5500 -m False -d ~/Resultados_Genxuxes/taco ")
#os.system("mkdir ~/Resultados_Genxuxes/tarta")
#os.system("python3 ./Genxuxes.py -i1 tarta -i2 tarta -n 5500 -m False -d ~/Resultados_Genxuxes/tarta ")
os.system("mkdir ~/Resultados_Genxuxes/NoValidoTemp")
os.system("mkdir ~/Resultados_Genxuxes/novalido")

for i in range(5500):
    x1=random.randint(0,9)
    x2=random.randint(0,10)
    print(x1,x2)
    for xuxe1,id1 in LabelSW.items():
        if id1 == x1:
            x1=xuxe1
    if x2 is not 10:
        for xuxe2,id2 in LabelSW.items():
            if id2 == x2:
                x2=xuxe2
    if x1==x2:
        x2=10
    print(x1,x2)
    if x2 is not 10:
        os.system("python3 ./Genxuxes.py -i1 " + str(x1) + " -i2 " + str(x2) + " -n 1 -m False -d ~/Resultados_Genxuxes/NoValidoTemp ")
    else:
        os.system("python3 ./Genxuxes.py -i1 " + str(x1) + " -n 1 -m False -d ~/Resultados_Genxuxes/NoValidoTemp ")
    os.system("mv ~/Resultados_Genxuxes/NoValidoTemp/*.jpg ~/Resultados_Genxuxes/NoValido/novalido"+str(i)+".jpg")
    os.system("rm ~/Resultados_Genxuxes/NoValidoTemp/*.jpg")
os.system("rm ~/Resultados_Genxuxes/NoValidoTemp")