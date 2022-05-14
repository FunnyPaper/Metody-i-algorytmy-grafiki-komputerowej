import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


# funkcja wyświetlająca histogram
def show_hist(title: str, ax: plt.Axes, src: np.ndarray, ran: tuple[int, int] = (0, 255)) -> None:
    ax.hist(src, bins=255)
    ax.set_xlim(ran)
    ax.set_title(title)


# funkcja wyświetlająca wykres słupkowy
def show_bar(title: str, ax: plt.Axes, src: tuple[np.ndarray, np.ndarray], ran: tuple[int, int] = (0, 255)) -> None:
    ax.bar(*src)
    ax.set_xlim(ran)
    ax.set_title(title)


# funkcja wyświetlająca obrazek
def show_img(title: str, ax: plt.Axes, src: np.ndarray) -> None:
    ax.imshow(src, cmap="gray")
    ax.set_title(title)


# funkcja "licząca" histogram
def get_histogram(src: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    res_x, res_y = np.arange(255), np.zeros(255)
    for r in src:
        for c in r:
            res_y[c] += 1

    return res_x, res_y


# funkcja spersonalizowana (wyświetla podany obrazek i jego histogram obok)
def show_answer(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    show_img(title, axes[0], src)
    show_hist(f'{title} - histogram', axes[1], src.flatten())
    show_bar(f'{title} - get_histogram', axes[2], get_histogram(src))


# wczytywanie obrazka
filename = "hist_gray.jpg"
img = np.asarray(Image.open(filename))
fig, a = plt.subplots(1, 3, num='Zadanie 4')

# wyświetlanie wyniku
show_answer(filename, a, img)

plt.show()
