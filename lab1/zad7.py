import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('lab1_gray.png')
x, y = img.shape

imgOX = np.copy(img) # Płytka kopia - aby nie oddziaływać na wartości zapisane w img
imgOX[x//2:] = imgOX[x//2-1::-1]

imgOY = np.copy(img) # Płytka kopia - aby nie oddziaływać na wartości zapisane w img
imgOY[:, y//2:] = imgOY[:, y//2::-1]

plt.subplot(1, 3, 1)
plt.title("Oryginał")
plt.imshow(img, cmap="gray")

plt.subplot(1, 3, 2)
plt.title("Odbicie w poziomie")
plt.imshow(imgOY, cmap="gray")

plt.subplot(1, 3, 3)
plt.title("Odbicie w pionie")
plt.imshow(imgOX, cmap="gray")

plt.show()
