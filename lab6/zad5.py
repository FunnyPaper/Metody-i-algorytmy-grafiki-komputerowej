import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from skimage.exposure import equalize_hist


# funkcja pomocnicza
def enlarge_img(src: np.ndarray, kernel_shape: tuple[int, int]) -> np.ndarray:
    ext_x, ext_y = kernel_shape[0] // 2, kernel_shape[1] // 2
    return np.pad(src, ((ext_x, ext_y), (ext_x, ext_y)))


# funkcja do zadania
def conv2(src: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    k_shape = kernel.shape
    bigger, copy = enlarge_img(src, k_shape), np.empty_like(src, dtype=np.int16)

    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            frag = bigger[ri:ri + k_shape[0], rc:rc + k_shape[1]]
            frag_var = np.var(frag[frag != src[ri, rc]])
            var = np.var(frag)
            if frag_var < var:
                copy[ri, rc] = src[ri, rc]
            else:
                copy[ri, rc] = np.sum(frag * kernel)

    return equalize_hist(copy)


# inicjalizacja (wczytanie zdjęcia + definicja maski)
filename = "Lenna.jpg"
img = np.asarray(Image.open(filename).convert("L"))
mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# tworzenie listy ze zdjęciami do wyświetlenia w postaci [str, np.ndarray]
imgs = [[f"{filename}", img]] + \
       [[f"{filename} [adaptive_sharpen]", conv2(img, mask)]]

# tworzenie okien i wyświetlanie listy wynikowej
fig, axes = plt.subplots(1, len(imgs), num="Zadanie 5")
for ax, (title, img) in zip(axes.flatten(), imgs):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)

plt.show()
