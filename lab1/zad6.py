import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('24_bit.jpg')
x, y, z = img.shape

res = np.zeros([x, y*2, z], dtype=int) # tworzenie tablicy 2x większej w oparciu o zdjęcie oryginalne
res[:x, :y] = img
res[:x, y:] = img[:, ::-1]

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Odbicie w poziomie sklejone z oryginałem")
plt.imshow(res)

plt.show()
