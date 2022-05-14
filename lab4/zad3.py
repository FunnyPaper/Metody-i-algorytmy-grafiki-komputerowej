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


def show_answer(img_name: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].imshow(src, cmap="gray")
    axes[0].set_title(img_name)
    for i, ax in enumerate(axes[1:]):
        ax.imshow(img_filter(src, 2 * (i + 1) + 1, np.median), cmap="gray")
        ax.set_title(f"{img_name}\nmedian_filter {2 * (i + 1) + 1}x{2 * (i + 1) + 1}")


# inicjalizacja
filename, n = "clown_noise_5.png", 3
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(1, n + 1, num='Zadanie 3')

# wyświetlanie rozwiązania
show_answer(filename, a, img)

plt.show()
