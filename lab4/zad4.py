import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from typing import Callable


def img_filter_rev(src: np.ndarray, frame_size: int, func: Callable[[np.ndarray], int]) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger = enlarge_img(src, frame_size)
    ext = frame_size // 2

    window = tuple(map(
        lambda e: bigger[ext + e[0]:-ext + e[0] or None, ext + e[1]:-ext + e[1] or None],
        np.array(np.meshgrid(np.arange(-ext, ext + 1), np.arange(-ext, ext + 1))).T.reshape(-1, 2)
    ))

    """ 
    powyższa metoda jest szybszym (dla małych wartości iteracji) odpowiednikiem tego (operacje na pętlach):
    window = [
        bigger[ext + row:-ext + row or None, ext + col:-ext + col or None]
        for row in range(-ext, ext + 1)
        for col in range(-ext, ext + 1)
    ]
    """

    return func(window, axis=0)


def enlarge_img(src: np.ndarray, frame_size: int) -> np.ndarray:
    ext = frame_size // 2

    """
    własnoręczne powiększanie (czas egzekucji podobny do powyższego rozwiązania):
    scale = (ext, 1)
    copy = np.empty([x + 2 * ext for x in src.shape], dtype=src.dtype)
    copy[ext:-ext, ext:-ext] = src.copy()
    copy[:ext, :] = np.tile(copy[ext, :], scale)
    copy[-ext:, :] = np.tile(copy[-ext - 1, :], scale)
    copy[:, :ext] = np.tile(copy[:, ext], scale).T
    copy[:, -ext:] = np.tile(copy[:, -ext - 1], scale).T
    return copy

    gotowy odpowiednik:
    """

    return np.pad(src, ((ext, ext), (ext, ext)), "edge")


def img_filter(src: np.ndarray, frame_size: int, func: Callable[[np.ndarray], int]) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger, copy = enlarge_img(src, frame_size), np.empty_like(src)

    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            copy[ri, rc] = func(bigger[ri:ri + frame_size, rc:rc + frame_size])

    return copy


def show_answer(img_name: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].imshow(src, cmap="gray")
    axes[0].set_title(img_name)
    for i, ax in enumerate(axes[1:]):
        ax.imshow(img_filter(src, 2 * (i + 1) + 1, np.median), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_filter {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


# inicjalizacja
filename, n = "clown_noise_10.png", 3
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(1, n + 1, num='Zadanie 4')

# wyświetlanie rozwiązania
show_answer(filename, a, img)

plt.show()
