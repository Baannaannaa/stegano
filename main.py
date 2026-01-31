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

def cree_image(a):
    nouvelle_image = Image.new('RGB', (1920, 1080))
    largeur_image=1920
    hauteur_image=1080
    for y in range(hauteur_image):
        for x in range(largeur_image):
            nouvelle_image.putpixel((x,y),(a[x][y][0],a[x][y][1],a[x][y][2]))
    nouvelle_image.save("test.jpg")
    
def main():
    a = [[[0,0,0] for j in range(1080)] for i in range(1920)]
    imgv = Image.open("/home/matt/Code/stegano/stegano/image_de_base/image_visible/cars.jpg")
    a = recupererpixel(a,imgv)
    cree_image(a)
    return 0


main()