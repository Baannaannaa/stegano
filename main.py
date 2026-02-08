from PIL import Image
import glob


def recupererimages(a):
    erreur = False
    tab = glob.glob(a+"/*.jpg")
    if len(tab)!=1:
        print("Erreur: nombre de fichier dans image_de_base/"+a+" différent de 1")
        erreur = True
    if erreur:
        return (erreur)
    else:
        return(tab[0])


def recupererpixel(a, img, largeur, hauteur ):
    for y in range(hauteur):
        for x in range(largeur):
            r,v,b=img.getpixel((x,y))
            a[x][y] = [r,v,b]
    return a


def cree_image(a, largeur, hauteur, nom):
    nouvelle_image = Image.new('RGB', (1920, 1080))
    for y in range(hauteur):
        for x in range(largeur):
            nouvelle_image.putpixel((x,y),(a[x][y][0],a[x][y][1],a[x][y][2]))
    nouvelle_image.save(nom)


def tab_int_to_bin(a, largeur, hauteur):
    for y in range(hauteur):
        for x in range(largeur): 
            for j in range(3):
                a[x][y][j]= format(a[x][y][j], '08b')
    return a


def tab_bin_to_int(a, largeur, hauteur):
    for y in range(hauteur):
        for x in range(largeur):
            for j in range(3):
                a[x][y][j]= int(a[x][y][j], 2)
    return a


def merge_tab_bin(tabv,tabc,largeur, hauteur):
    for y in range(hauteur):
        for x in range(largeur):
            for j in range(3):
                tabv[x][y][j]=tabv[x][y][j][:4] + tabc[x][y][j][:4]
    return tabv


def decodebin(tab,largeur, hauteur ):
    for y in range(hauteur):
        for x in range(largeur):
            for j in range(3):
                tab[x][y][j]=tab[x][y][j][4:] + "0000"
    return tab


def coder_image():
    #coder l'image
    imv = recupererimages("image_de_base/image_visible")
    imc = recupererimages("image_de_base/image_cache")
    if imc != True and imv!= True:
        imgv = Image.open(imv)
        imgc = Image.open(imc)

        largeurv,hauteurv = imgv.size
        largeurc,hauteurc = imgv.size

        tabimgv = [[[0,0,0] for j in range(hauteurv)] for i in range(largeurv)]
        tabimgc = [[[0,0,0] for j in range(largeurc)] for i in range(largeurc)]

        tabimgv = recupererpixel(tabimgv, imgv, largeurv, hauteurv)
        tabimgc = recupererpixel(tabimgc, imgc, largeurc, hauteurc)

        tabimgv = tab_int_to_bin(tabimgv, largeurv, hauteurv)
        tabimgc = tab_int_to_bin(tabimgc, largeurc, hauteurc)

        tabimgv = merge_tab_bin(tabimgv,tabimgc, largeurc, hauteurc)

        tabimgv = tab_bin_to_int(tabimgv, largeurv, hauteurv)

        cree_image(tabimgv, largeurv, hauteurv, "code.jpg")


def decoder_image():
    #decoder l'image
    imcode = recupererimages("image_a_decoder")

    if imcode != True:
        imgcode = Image.open(imcode)

        largeurcode,hauteurcode = imgcode.size
        
        tabimgcode = [[[0,0,0] for j in range(hauteurcode)] for i in range(largeurcode)]
        
        tabimgcode = recupererpixel(tabimgcode, imgcode, largeurcode, hauteurcode)
        
        tabimgcode = tab_int_to_bin(tabimgcode, largeurcode, hauteurcode)
        
        tabimgcode = decodebin(tabimgcode, largeurcode, hauteurcode)
        
        tabimgcode = tab_bin_to_int(tabimgcode, largeurcode, hauteurcode)

        cree_image(tabimgcode, largeurcode, hauteurcode, "decode.jpg")


def main():
    coder_image()
    decoder_image()
    print("Fin")


main()