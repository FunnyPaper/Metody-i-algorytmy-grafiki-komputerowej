import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from scipy.signal import convolve2d
from skimage.exposure import rescale_intensity
from functools import partial  # funkcja pomocnicza

# inicjalizacja (wczytanie zdjęcia + tworzenie masek)
filename = "Airplane24.jpg"
img = np.asarray(Image.open(filename).convert("L"))
edges = np.array([[ 0, -1,  0], [-1, 4, -1], [ 0, -1,  0]]), \
        np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
sobel = np.array([[ 1,  0, -1], [ 2, 0, -2], [ 1,  0, -1]]), \
        np.array([[ 1,  2,  1], [ 0, 0,  0], [-1, -2, -1]])

# definicje funkcji częściowych z przywiązanymi wartościami
stretch = partial(rescale_intensity, in_range=(0, 255))
conv2 = partial(convolve2d, img)
im_sum = partial(np.sum, axis=0)

# konwolucja i składanie obrazów wynikowych
s_abs = stretch(im_sum([np.absolute(conv2(s)) for s in sobel]))
s_sqrt = stretch(im_sum([conv2(s) ** 2 for s in sobel]) ** 0.5)

# tworzenie listy ze zdjęciami do wyświetlenia w postaci [str, np.ndarray]
imgs = [[f"{filename}", img]] + \
       [[f"{e}", stretch(conv2(e))] for e in edges] + \
       [["Sobel\nsuma wartości\nbezwględnych", s_abs]] + \
       [["Sobel\npierwiastek sumy\nkwadratów", s_sqrt]]

# tworzenie okien i wyświetlanie listy wynikowej
fig, axes = plt.subplots(1, len(imgs), num="Zadanie 1")
for ax, (title, img) in zip(axes.flatten(), imgs):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)

plt.show()
