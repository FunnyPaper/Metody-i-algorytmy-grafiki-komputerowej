import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import skimage.exposure as exp


# funkcja pomocnicza
def enlarge_img(src: np.ndarray, kernel_shape: tuple[int, int]) -> np.ndarray:
    ext_x, ext_y = kernel_shape[0] // 2, kernel_shape[1] // 2
    return np.pad(src, ((ext_x, ext_y), (ext_x, ext_y)))


# własna implementacja konwolucji 2D
def conv2(src: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    k_shape = kernel.shape
    bigger, copy = enlarge_img(src, k_shape), np.empty_like(src, dtype=np.int16)

    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            fragment = np.sum(bigger[ri:ri + k_shape[0], rc:rc + k_shape[1]] * kernel)
            copy[ri, rc] = fragment

    return exp.equalize_hist(copy)


# inicjalizacja (wczytanie zdjęcia + tworzenie masek)
filename = "Lenna.jpg"
img = np.asarray(Image.open(filename).convert('L'))
edges = np.array([[ 0, -1,  0], [-1,  5, -1], [ 0, -1,  0]]), \
        np.array([[-1, -1, -1], [-1,  9, -1], [-1, -1, -1]]), \
        np.array([[-1, -2, -1], [-2, 13, -2], [-1, -2, -1]])

# tworzenie listy wynikowej w postaci [str, np.ndarray]
res = [["Oryginał:", img]] + [[f"Maska\n{e}", conv2(img, e)] for e in edges]

# tworzenie okien i wyświetlanie listy wynikowej
fig, ax = plt.subplots(1, len(res), num="Zadanie 4")
for a, (t, r) in zip(ax, res):
    a.imshow(r, cmap="gray")
    a.set_title(t)

plt.show()
