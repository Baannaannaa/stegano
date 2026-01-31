from PIL import Image


def recupererpixel(a,img):
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            r,v,b=img.getpixel((x,y))
            a[x][y] = [r,v,b]
    print("fin")
    return a


def cree_image(a,nom):
    nouvelle_image = Image.new('RGB', (1920, 1080))
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            nouvelle_image.putpixel((x,y),(a[x][y][0],a[x][y][1],a[x][y][2]))
    nouvelle_image.save(nom)


def tab_int_to_bin(a):
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            for j in range(3):
                a[x][y][j]= format(a[x][y][j], '08b')
    return a


def tab_bin_to_int(a):
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            for j in range(3):
                a[x][y][j]= int(a[x][y][j], 2)
    return a


def merge_tab_bin(tabv,tabc):
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            for j in range(3):
                tabv[x][y][j]=tabv[x][y][j][:4] + tabc[x][y][j][:4]
    return tabv


def decodebin(tab):
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            for j in range(3):
                tab[x][y][j]=tab[x][y][j][4:] + "0000"
    return tab


def main():
    tabimgv = [[[0,0,0] for j in range(1080)] for i in range(1920)]
    tabimgc = [[[0,0,0] for j in range(1080)] for i in range(1920)]

    imgv = Image.open("image_de_base/image_visible/cars.jpg")
    imgc = Image.open("image_de_base/image_cache/madagascar.jpg")

    tabimgv = recupererpixel(tabimgv,imgv)
    tabimgc = recupererpixel(tabimgc,imgc)

    tabimgv = tab_int_to_bin(tabimgv)
    tabimgc = tab_int_to_bin(tabimgc)

    tabimgv = merge_tab_bin(tabimgv,tabimgc)

    tabimgv = tab_bin_to_int(tabimgv)

    cree_image(tabimgv,"code.jpg")

    #decoder l'image
    tabimgcode = [[[0,0,0] for j in range(1080)] for i in range(1920)]
    imgcode = Image.open("/home/matt/Code/stegano/stegano/code.jpg")
    tabimgcode = recupererpixel(tabimgcode, imgcode)
    tabimgcode = tab_int_to_bin(tabimgv)
    tabimgcode = decodebin(tabimgcode)
    tabimgcode = tab_bin_to_int(tabimgcode)

    cree_image(tabimgcode,"decode.jpg")
    
    return 0


main()