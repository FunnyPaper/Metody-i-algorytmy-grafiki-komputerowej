import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


# funkcja pomocnicza
def disk(diameter: int) -> np.ndarray:
    radius = diameter // 2
    x, y = np.mgrid[:diameter, :diameter]
    circle = (x - radius) ** 2 + (y - radius) ** 2
    res = np.zeros_like(circle)
    res[circle <= radius ** 2] = 1
    return res.astype(np.uint8)


# inicjalizacja (wczytanie zdjęcia)
filename = "Lenna.jpg"
img = cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2GRAY)

# tworzenie listy ze zdjęciami do wyświetlenia w postaci [str, np.ndarray]
imgs = [[f"{filename}", img]] + \
       [[f"{filename} [dilate]", cv.dilate(img, disk(5), iterations=1)]]

# tworzenie okien i wyświetlanie listy wynikowej
fig, axes = plt.subplots(1, len(imgs), num="Zadanie 3")
for ax, (title, img) in zip(axes.flatten(), imgs):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)

plt.show()
