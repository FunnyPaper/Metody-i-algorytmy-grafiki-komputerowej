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

    return func(window, axis=0)


def enlarge_img(src: np.ndarray, frame_size: int) -> np.ndarray:
    ext = frame_size // 2
    return np.pad(src, ((ext, ext), (ext, ext)), "edge")


def median_filter(src: np.ndarray, frame_size: int, adaptive: bool = False) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger, copy = enlarge_img(src, frame_size), np.empty_like(src)

    img_var = np.var(bigger)
    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            frag = bigger[ri:ri + frame_size, rc:rc + frame_size]
            if adaptive:
                v = np.var(frag)
                if v <= img_var:
                    copy[ri, rc] = np.median(frag)
            else:
                copy[ri, rc] = np.median(frag)
    return copy


def show_answer(img_name: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0, 0].imshow(src, cmap="gray")
    axes[0, 0].set_title(img_name)
    axes[1, 0].imshow(src, cmap="gray")
    axes[1, 0].set_title(img_name)
    for i, ax in enumerate(axes[0, 1:]):
        ax.imshow(median_filter(src, 2 * (i + 1) + 1), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_filter {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")

    for i, ax in enumerate(axes[1, 1:]):
        ax.imshow(median_filter(src, 2 * (i + 1) + 1, True), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_adaptive_filter {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


# inicjalizacja
filename, n = "clown_noise_10.png", 3
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(2, n + 1, num='Zadanie 4')

# wyświetlanie rozwiązania
show_answer(filename, a, img)

plt.show()
