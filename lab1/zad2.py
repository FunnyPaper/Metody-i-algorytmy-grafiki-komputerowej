import matplotlib.pyplot as plt
import matplotlib.image as mpimg

size = 150, 77 # wymiary fragmentu
coord = 50, 100 # współrzędne punktu początkowego fragmentu

img = mpimg.imread('lab1_color.png')

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Wycięty fragment")
plt.imshow(img[coord[0]:coord[0] + size[0], coord[1]:coord[1] + size[1]])

plt.imsave('ZapisDoPliku.jpg', img[coord[0]:coord[0] + size[0], coord[1]:coord[1] + size[1]])
plt.show()
