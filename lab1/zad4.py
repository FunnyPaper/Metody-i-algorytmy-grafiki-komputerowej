import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('24_bit.jpg')

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Oryginał')

plt.subplot(2, 2, 2)
plt.imshow(img[:, :, 0])
plt.title('Kanał [R]')

plt.subplot(2, 2, 3)
plt.imshow(img[:, :, 1])
plt.title('Kanał [G]')

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, 2])
plt.title('Kanał [B]')

plt.show()
