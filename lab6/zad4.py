import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from typing import Callable


# funkcja pomocnicza
def enlarge_img(src: np.ndarray, kernel_shape: tuple[int, int]) -> np.ndarray:
    ext_x, ext_y = kernel_shape[0] // 2, kernel_shape[1] // 2
    return np.pad(src, ((ext_x, ext_y), (ext_x, ext_y)), "edge")


# funkcja do zadania
def img_adaptive_filter(src: np.ndarray, frame_size: int, func: Callable[[np.ndarray], int] = np.median) -> np.ndarray:
    assert frame_size >= 3 and frame_size & 1
    bigger, copy = enlarge_img(src, (frame_size, frame_size)), np.empty_like(src)

    shape = src.shape
    for ri in range(shape[0]):
        for rc in range(shape[1]):
            frag = bigger[ri:ri + frame_size, rc:rc + frame_size]
            frag_var = np.var(frag[frag != src[ri, rc]])
            var = np.var(frag)
            if frag_var >= var:
                copy[ri, rc] = src[ri, rc]
            else:
                copy[ri, rc] = func(frag)

    return copy


# inicjalizacja (wczytanie zdjęcia)
filename = "clown_noise_10.png"
img = np.asarray(Image.open(filename).convert("L"))

# tworzenie listy ze zdjęciami do wyświetlenia w postaci [str, np.ndarray]
imgs = [[f"{filename}", img]] + \
       [[f"{filename} [img_adaptive_filter]", img_adaptive_filter(img, 5)]]

# tworzenie okien i wyświetlanie listy wynikowej
fig, axes = plt.subplots(1, len(imgs), num="Zadanie 4")
for ax, (title, img) in zip(axes.flatten(), imgs):
    ax.imshow(img, cmap="gray")
    ax.set_title(title)

plt.show()
