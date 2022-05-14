import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('24_bit.jpg')
swapped = np.copy(img) # Płytka kopia - aby nie oddziaływać na wartości zapisane w img

swapped[:, :, 0], swapped[:, :, 2] = swapped[:, :, 2], swapped[:, :, 0]

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Zamiana miejscami kanałów R i B")
plt.imshow(swapped)

plt.show()
