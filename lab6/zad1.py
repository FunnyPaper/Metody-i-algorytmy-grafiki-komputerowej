import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import skimage.exposure as exp
import scipy.signal as sp


# funkcja pomocnicza
def conv2(src: np.ndarray, mask: np.ndarray) -> np.ndarray:
    return sp.convolve2d(src, mask, "same")


# inicjalizacja (wczytanie zdjęcia + tworzenie masek)
filename = "church.jpg"
img = np.asarray(Image.open(filename).convert('L'), dtype=np.int16)
edges = np.array([[ 0, -1,  0], [-1, 4, -1], [ 0, -1,  0]]), \
        np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
sobel = np.array([[ 1,  2,  1], [ 0, 0,  0], [-1, -2, -1]]), \
        np.array([[ 1,  0, -1], [ 2, 0, -2], [ 1,  0, -1]])

sobel_pre = [conv2(img, e) for e in sobel]
# tworzenie listy wynikowej w postaci [str, np.ndarray]
res = [["Oryginał:", img]] + \
      [[f"Maska\n{e}", exp.equalize_hist(conv2(img, e))] for e in edges] + \
      [["Sobel - wartość bezwględna", exp.equalize_hist((sum([x ** 2 for x in sobel_pre])) ** 0.5)]] + \
      [["Sobel - suma kwadratów", exp.equalize_hist(sum(np.absolute(sobel_pre)))]]

# tworzenie okien i wyświetlanie listy wynikowej
fig, ax = plt.subplots(1, len(res), num="Zadanie 2")
for a, (t, r) in zip(ax, res):
    a.imshow(r, cmap="gray")
    a.set_title(t)

plt.show()
