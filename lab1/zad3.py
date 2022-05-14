import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('lab1_gray.png')

hor = np.copy(img) # Płytka kopia - aby nie oddziaływać na wartości zapisane w img
ver = img[::, ::-1]

rows, cols = img.shape
for x in range(rows):
    for y in range(cols):
        hor[x, y] = img[rows - x - 1, y]

plt.figure("Oryginał")
plt.imshow(img, cmap="gray")

plt.figure("Odbicie w pionie")
plt.imshow(hor, cmap="gray")

plt.figure("Odbicie w poziomie")
plt.imshow(ver, cmap="gray")

plt.show()
