import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import skimage.exposure as exp
import scipy.signal as sp


# funkcja pomocnicza
def conv2(src: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return exp.equalize_hist(sp.convolve2d(src, mask, "same"))


# inicjalizacja (wczytanie zdjęcia + tworzenie masek)
filename = "Airplane24.jpg"
img = np.asarray(Image.open(filename).convert('L'))
edges = np.array([[ 0, -1,  0], [-1,  4, -1], [ 0, -1,  0]]), \
        np.array([[-1, -1, -1], [-1,  8, -1], [-1, -1, -1]]), \
        np.array([[-1, -2, -1], [-2, 12, -2], [-1, -2, -1]])


# tworzenie listy wynikowej w postaci [str, np.ndarray]
res = [["Oryginał:", img]] + [[f"Maska\n{e}", conv2(img, e)] for e in edges]

# tworzenie okien i wyświetlanie listy wynikowej
fig, ax = plt.subplots(1, len(res), num="Zadanie 2")
for a, (t, r) in zip(ax, res):
    a.imshow(r, cmap="gray")
    a.set_title(t)

plt.show()
