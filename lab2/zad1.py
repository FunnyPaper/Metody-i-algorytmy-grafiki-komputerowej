import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np

positive = np.asarray(Image.open("gray1.jpeg"))

# odejmij od wartości 255 lub 1 w zależności od typu danych
negative = (255 if positive.dtype == np.uint8 else 1) - positive[:, :]

plt.figure("Zadanie 1")

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(positive, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Negatyw")
plt.imshow(negative, cmap="gray")

plt.show()
