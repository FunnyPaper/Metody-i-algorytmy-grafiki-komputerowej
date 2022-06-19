import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


# funkcja do zadania
def threshold(src: np.ndarray, thresh: int = 127) -> np.ndarray:
    res = src.copy()
    res[res < thresh] = 0
    res[res >= thresh] = 255
    return res


# inicjalizacja (wczytanie zdjęcia + wartości thresh)
filename = "Airplane24.jpg"
img = np.asarray(cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2GRAY))
threshes = [50 * i for i in range(1, 5)]

# tworzenie listy ze zdjęciami do wyświetlenia w postaci [str, np.ndarray]
imgs = [[f"{filename}", img]] + \
       [[f"OTSU", cv.threshold(img, 0, 255, cv.THRESH_OTSU)[1]]] + \
       [[f"threshold[{t}]", threshold(img, t)] for t in threshes]

# tworzenie okien i wyświetlanie listy wynikowej
fig, axes = plt.subplots(2, len(imgs) // 2, num="Zadanie 2")
for ax, (title, img) in zip(axes.flatten(), imgs):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)

plt.show()
