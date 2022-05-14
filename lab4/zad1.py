import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from typing import Callable


def img_filter(src: np.ndarray, frame_size: int, func: Callable[[np.ndarray], int]) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    result = np.zeros_like(src)

    ext, shape = frame_size // 2, src.shape
    for ri in range(shape[0] - frame_size + 1):
        for rc in range(shape[1] - frame_size + 1):
            result[ri + ext, rc + ext] = func(src[ri:ri + frame_size, rc:rc + frame_size])

    return result


def show_answer(img_name: str, axes: plt.Axes, src: np.ndarray, func: Callable[[np.ndarray], int], func_name: str) \
        -> None:
    axes[0].imshow(src, cmap="gray")
    axes[0].set_title(img_name)
    for i, ax in enumerate(axes[1:]):
        ax.imshow(img_filter(src, 2 * (i + 1) + 1, func), cmap="gray")
        ax.set_title(f"{img_name} - {func_name} {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


# inicjalizacja
filename, n = "clown.jfif", 3
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(2, n + 1, num='Zadanie 1')

# wyświetlanie rozwiązania
show_answer(filename, a[0], img, np.min, "min")
show_answer(filename, a[1], img, np.max, "max")

plt.show()
