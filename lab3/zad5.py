import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from skimage.exposure import rescale_intensity


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
    show_hist(title, axes[1], src.flatten())


# funkcja rozciągająca histogram (z opcjonalnymi parametrami dla wysokiego i niskiego progu)
def stretch_histogram(src: np.ndarray, low: int = None, high: int = None) -> np.ndarray:
    low = np.min(src) if low is None else low
    high = np.max(src) if high is None else high
    assert high > low  # sprawdzanie progów

    r = src.copy()
    r[r < low], r[r > high] = 0, 255
    r = (r - low) / (high - low)
    return np.asarray(255 * r, dtype=np.uint8)


# wczytywanie obrazków
filenames = ["hist_gray.jpg", "hist_couple.bmp"]
imgs = [np.asarray(Image.open(img)) for img in filenames]
fig, a = plt.subplots(2, 6, num='Zadanie 5')

# wyświetlanie wyniku
for index, (name, img) in enumerate(zip(filenames, imgs)):
    res = rescale_intensity(img), stretch_histogram(img)
    show_answer(name, a[index, :2], img)                    # oryginalny histogram
    show_answer('[gotowa funkcja]', a[index, 2:4], res[0])  # rozciągnięty histogram ("gotowa" funkcja)
    show_answer('[własna funkcja]', a[index, 4:], res[1])   # rozciągnięty histogram (własna funkcja)

plt.show()
