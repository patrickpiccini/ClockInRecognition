import cv2
import glob


count = 0


#============== Salva Rostos cortados ===============
cascade = cv2.CascadeClassifier("C:\\Users\\patrick.piccini\\Pictures\\ComputacaoGrafica\\models\\haarcascade_frontalface_alt.xml")
lista = glob.glob("models\images\*.png")

for i in lista:
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detect = cascade.detectMultiScale(gray,1.1, 5)

    for (x, y, w, h) in detect:
        # print(detect)
        # cv2.rectangle(img, (x-50, y-50),(x+w+50, y+h+50), (0, 0, 255), 2)
        yp = int(y*0.30) 
        xp = int(x*0.20)
        faces = img[y-yp:y + h+yp, x-xp:x + w+xp] 
        # cv2.imshow('edge', faces)
        cv2.imwrite(f'models\\helmetImages\\hemlet_{count}.jpg', faces)
        print(f'salva a imagem teste{count}.jpg')
        count += 1


cv2.waitKey(0)
cv2.destroyAllWindows()


#============== Inverter imagens ===============
# lista = glob.glob("imgs\*.jpg")
# count = 1
# lenLista = len(lista)
# for i in lista:
#     image = cv2.imread(i)
#     imageRevert = image[:,::-1]  # vertical

#     cv2.imwrite(f'imgs/hemlet_{lenLista+count}.jpg', imageRevert)
#     print(f'salva a imagem teste{count}.jpg')
#     count+=1

# cv2.waitKey(0)
# cv2.destroyAllWindows()