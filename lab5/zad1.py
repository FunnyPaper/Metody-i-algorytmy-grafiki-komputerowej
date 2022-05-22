import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import skimage.exposure as exp
import scipy.signal as sp


# funkcje pomocnicza
def conv2(src: np.ndarray, mask: np.ndarray, absolute: bool = False) -> np.ndarray:
    result = sp.convolve2d(src, mask, "same")
    return np.absolute(result) if absolute else exp.equalize_hist(result)


def show_figure(axes: plt.Axes, data: list[list]) -> None:
    for a, (t, r) in zip(axes.flatten(), data):
        a.imshow(r, cmap="gray")
        a.set_title(t)


# inicjalizacja (wczytanie zdjęcia + tworzenie masek)
filename = "church.jpg"
img = np.asarray(Image.open(filename).convert('L'))
prewitt = np.array([[-1, -1, -1], [ 0,  0, 0], [ 1, 1, 1]]), \
          np.array([[-1,  0,  1], [-1,  0, 1], [-1, 0, 1]])
sobel =   np.array([[-1, -2, -1], [ 0,  0, 0], [ 1, 2, 1]]), \
          np.array([[-1,  0,  1], [-2,  0, 2], [-1, 0, 1]])
edges =   np.array([[ 0,  0,  0], [ 1, -1, 0], [ 0, 0, 0]]), \
          np.array([[ 0,  1,  0], [ 0, -1, 0], [ 0, 0, 0]]), \
          np.array([[ 1,  0,  0], [ 0, -1, 0], [ 0, 0, 0]])

# tworzenie listy wynikowej w postaci [str, np.ndarray] dla pierwszego ekranu
first =  [["Oryginał:", img]] + \
         [[f"Maska\n{e}",            conv2(img, e)] for e in edges] + \
         [[f"Maska Prewitta\n{e}",   conv2(img, e)] for e in prewitt] + \
         [[f"Maska Sobela\n{e}",     conv2(img, e)] for e in sobel]

# tworzenie listy wynikowej w postaci [str, np.ndarray] dla drugiego ekranu
second = [[f"|Suma masek Prewitta|",              conv2(img, prewitt[0] + prewitt[1], True)]] + \
         [[f"|Suma masek Sobela|",                conv2(img, sobel  [0] + sobel  [1], True)]] + \
         [[f"|Suma masek Sobela i Prewitta (1)|", conv2(img, sobel  [0] + prewitt[0], True)]] + \
         [[f"|Suma masek Sobela i Prewitta (2)|", conv2(img, sobel  [1] + prewitt[1], True)]] + \
         [[f"|Suma masek Sobela 1 i Prewitta 2|", conv2(img, sobel  [0] + prewitt[1], True)]] + \
         [[f"|Suma masek Sobela 2 i Prewitta 1|", conv2(img, sobel  [1] + prewitt[0], True)]]

# tworzenie okien i wyświetlanie listy wynikowej
ax = plt.subplots(2, len(first)  // 2, num="Zadanie 1.1")[1],\
     plt.subplots(2, len(second) // 2, num="Zadanie 1.2")[1]

show_figure(ax[0], first)
show_figure(ax[1], second)

plt.show()
