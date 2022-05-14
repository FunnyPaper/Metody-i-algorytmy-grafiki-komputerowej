import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def make_noise(src: np.ndarray, percent: int) -> np.ndarray:
    assert 100 >= percent >= 0
    percent /= 100
    ran = np.random.rand(*src.shape)
    src[ran < percent], src[ran > 1-percent] = 0, 255

    return src


# inicjalizacja
filename = "clown.jfif"
img = np.asarray(Image.open(filename).convert('L'))
fig, a = plt.subplots(1, 2, num='Zadanie 2')


# wyświetlanie rozwiązania
a[0].imshow(img, cmap="gray")
a[0].set_title(filename)
a[1].imshow(make_noise(img, 5), cmap="gray")
a[1].set_title(f"{filename} - noise")

plt.show()
