import matplotlib.pyplot as plt
import matplotlib.image as mpimg

size = 200, 200 # wymiary fragmentu
coord = 100, 350 # współrzędne punktu początkowego fragmentu

plt.figure("Oryginał")
img = mpimg.imread('lab1_gray.png')
plt.imshow(img, cmap='gray')

plt.figure("Wycięty fragment")
plt.imshow(img[coord[0]:coord[0] + size[0], coord[1]:coord[1] + size[1]], cmap='gray')

plt.show()
