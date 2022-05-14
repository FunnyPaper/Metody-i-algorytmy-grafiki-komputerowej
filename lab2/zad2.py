from functools import reduce
import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np

files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"] # nazwy plików do wczytania
imgs = [np.asarray(Image.open(name)) for name in files] # tablica na obrazy
length = len(imgs)

# sumowanie obrazów i podział przez ich ilość (jednakowa waga dla każdego)
# dtype=int -> przy sumowaniu wartości potrzebujemy więcej miejsca niż przy uint8
img_sum = reduce(lambda x, y: x + y, imgs, np.zeros(imgs[0].shape, dtype=int)) // length

plt.figure("Zadanie 2")
for i, img in enumerate(imgs):
    plt.subplot(1, length + 1, i + 1)
    plt.title(f"Obraz nr {i + 1}")
    plt.imshow(img)

plt.subplot(1, length + 1, length + 1)
plt.title("Kolaż")
plt.imshow(img_sum)

plt.show()
