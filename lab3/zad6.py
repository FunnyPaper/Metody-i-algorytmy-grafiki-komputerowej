import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from skimage.exposure import equalize_hist


# funkcja wyświetlająca histogram
def show_hist(title: str, ax: plt.Axes, src: np.ndarray, ran: tuple[int, int] = (0, 255)) -> None:
    ax.hist(src, bins=255)
    ax.set_xlim(ran)
    ax.set_title(title)


# funkcja wyświetlająca obrazek
def show_img(title: str, ax: plt.Axes, src: np.ndarray) -> None:
    ax.imshow(src, cmap="gray")
    ax.set_title(title)


# funkcja spersonalizowana (wyświetla podany obrazek i jego histogram obok)
def show_answer(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    show_img(title, axes[0], src)
    show_hist(f'{title} - histogram', axes[1], src.flatten())


# funkcja wyrównująca histogram
def equalize_histogram(src: np.ndarray) -> np.ndarray:
    shape = src.shape
    # histogram kumulacyjny (lista składana - przyspieszenie kalkulacji)
    c_hist = np.asarray([np.size(src[src <= x]) for x in range(256)])
    mapping = (255 * c_hist) // (shape[0] * shape[1])
    return mapping[src]


# wczytywanie obrazków
filenames = ["hist_gray.jpg", "hist_couple.bmp"]
imgs = [np.asarray(Image.open(img)) for img in filenames]
fig, a = plt.subplots(2, 6, num='Zadanie 6')

# wyświetlanie wyniku
for index, (name, img) in enumerate(zip(filenames, imgs)):
    res = np.asarray(equalize_hist(img) * 255, dtype=np.uint8), equalize_histogram(img)
    show_answer(name, a[index, :2], img)                    # oryginalny histogram
    show_answer('[gotowa funkcja]', a[index, 2:4], res[0])  # wyrównany histogram ("gotowa" funkcja)
    show_answer('[własna funkcja]', a[index, 4:], res[1])   # wyrównany histogram (własna funkcja)

plt.show()
