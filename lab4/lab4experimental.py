import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from typing import Callable
from timeit import timeit


def enlarge_img(src: np.ndarray, frame_size: int) -> np.ndarray:
    ext = frame_size // 2

    # scale = (ext, 1)
    # copy = np.empty([x + 2 * ext for x in src.shape], dtype=src.dtype)
    # copy[ext:-ext, ext:-ext] = src.copy()
    # copy[:ext, :] = np.tile(copy[ext, :], scale)
    # copy[-ext:, :] = np.tile(copy[-ext - 1, :], scale)
    # copy[:, :ext] = np.tile(copy[:, ext], scale).T
    # copy[:, -ext:] = np.tile(copy[:, -ext - 1], scale).T
    # return copy

    return np.pad(src, ((ext, ext), (ext, ext)), "edge")


def circle_mask(frame_size: int) -> np.ndarray:
    radius = frame_size // 2
    x, y = np.mgrid[:frame_size, :frame_size]

    return (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2


def median_filter(src: np.ndarray, frame_size: int, frame_shape: Callable[[int], np.ndarray] = None) \
        -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger, copy = enlarge_img(src, frame_size), np.empty_like(src)

    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            frame = bigger[ri:ri + frame_size, rc:rc + frame_size]
            copy[ri, rc] = np.median(frame if not frame_shape else frame[frame_shape(frame_size)])

    return copy


def median_filter_rev(src: np.ndarray, frame_size: int) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger = enlarge_img(src, frame_size)
    ext = frame_size // 2

    window = tuple(map(
        lambda e: bigger[ext + e[0]:-ext + e[0] or None, ext + e[1]:-ext + e[1] or None],
        np.array(np.meshgrid(np.arange(-ext, ext + 1), np.arange(-ext, ext + 1))).T.reshape(-1, 2)
    ))

    return np.median(window, axis=0)


def show_answer(img_name: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].imshow(src, cmap="gray")
    axes[0].set_title(img_name)
    for i, ax in enumerate(axes[1:]):
        ax.imshow(median_filter(src, 2 * (i + 1) + 1), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_filter {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


def show_answer_exp(img_name: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].imshow(src, cmap="gray")
    axes[0].set_title(img_name)
    for i, ax in enumerate(axes[1:]):
        ax.imshow(median_filter_rev(src, 2 * (i + 1) + 1), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_filter_rev {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


n = 3
filename = "clown_noise_10.png"
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(1, n + 1, num='Zadanie 4 [eksperyment]')

#show_answer(filename, a, img)
show_answer_exp(filename, a, img)

#print("median_filter(img, 9) [number=100]", timeit(lambda: median_filter(img, 9), number=100), 's')
print("median_filter_rev(img, 9) [number=100]", timeit(lambda: median_filter_rev(img, 9), number=10), 's')

plt.show()
