import argparse
import os.path
import random
from PIL import Image, ImageDraw
from tfmaux import *


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


# entrada de datos,
# xuxe1
# xuxe2
# numero imagenes
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True, help="name of xuxe kind")
ap.add_argument("-i2", "--image2", required=False, help="name of second xuxe kind, optional")
ap.add_argument("-n", "--number", required=True, help="Number of images resulting")
ap.add_argument("-d", "--outdir", required=False, help="output directory, default is Results")
args = vars(ap.parse_args())

if args["outdir"] is None:
    outdir = "Results/"
else:
    outdir = args["outdir"] + "/"

# variables auxiliares
n1 = 0
n2 = 0
Tags = 1
BB2 = 1
BB2s=1
numeroFondos= 4

# cuenta el numero de imagenes en el directorio
for root1, dirs1, files1 in os.walk("Xuxes/" + args["image1"]):
    for f in files1:
        if f.endswith(".png"):
            n1 = n1 + 1

# cuenta el numero de imagenes en el directorio
if args["image2"] is not None:
    Tags = 2
    for root2, dirs2, files2 in os.walk("Xuxes/" + args["image2"]):
        for f in files2:
            if f.endswith(".png"):
                n2 = n2 + 1

# bucle que se repite segun el numero especificado
for i in range(int(args["number"])):
    # for i in range(4):
    pathf = "Xuxes/fondos/" + "fondo" + str(random.randint(1, numeroFondos)) + ".jpg"
    fondo = Image.open(pathf)
    # cargar xuxe 1 aleatoria de las existenetes en el directorio
    path1 = "Xuxes/" + args["image1"] + "/" + args["image1"] + str(random.randint(1, n1)) + ".png"
    xuxe1 = Image.open(path1)
    xuxe1.load()
    # xuxe1.show()
    xuxe1.thumbnail((128, 128))
    # xuxe1.show()
    xuxe1 = xuxe1.rotate(random.randint(0, 360))  # se rota de forma aleatoria
    BB1 = xuxe1.getbbox()
    #test=ImageDraw.Draw(xuxe1)
    #test.rectangle(BB1,outline='red')
    # xuxe1.show()
    # print(str(BB1))

    # lo mismo para xuxe2 en caso de existir nombre
    if args["image2"] is not None:
        path2 = "Xuxes/" + args["image2"] + "/" + args["image2"] + str(random.randint(1, n2)) + ".png"
        xuxe2 = Image.open(path2)
        # xuxe2.show()
        xuxe2.thumbnail((128, 128))
        # xuxe2.show()
        xuxe2 = xuxe2.rotate(random.randint(0, 360))  # se rota de forma aleatoria
        BB2 = xuxe2.getbbox()
        # xuxe2.show()
        # print(path1)

    # una vez obtenido ambas xuxes y el fondo hay que juntarlo
    position = (random.randint(0 - BB1[0], (fondo.width - BB1[2])),
                random.randint(0 - BB1[0], (fondo.height - BB1[3])))
    fondo.paste(xuxe1, position, xuxe1)
    b = (float(BB1[0])+position[0], float(BB1[2])+position[0], float(BB1[1])+ position[1], float(BB1[3])+ position[1])
    BB1s =convert((141,141),b)
    # se repite para segunda xuxe si necesario
    if args["image2"] is not None:
        position = (random.randint(0 - BB2[0], (fondo.width - (BB2[2]))),
                    random.randint(0 - BB2[1], (fondo.height - (BB2[3]))))
        fondo.paste(xuxe2, position, xuxe2)
        BB2s = [position[0] + BB2[0], position[1] + BB2[1], BB2[2] + position[0], BB2[3] + position[1]]

    #test2=ImageDraw.Draw(fondo)
    #test2.rectangle(BB1,outline='red')
    #fondo.show()
    fondo.save(outdir + str(args["image1"]) + str(i) + ".jpg")
    fondo.close()
    f = open(outdir + str(args["image1"]) + str(i) + ".txt", 'w')
    if args["image2"] is not None:
        f.write(str(Tags) + ";" + str(args["image1"]) + ";" + BB1s + ";" + str(args["image2"]) + ";" + str(BB2s))
    else:
        f.write(str(LabelSW.get(args["image1"])) + " " + str(BB1s[0])+" " +str(BB1s[1])+" " +str(BB1s[2])+" " +str(BB1s[3]))
    f.close()
    # cv2.waitKey()
# print(fondo)
