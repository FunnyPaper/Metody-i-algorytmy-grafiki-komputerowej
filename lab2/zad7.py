import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np


def gamma_correct(src: np.ndarray, fac: float) -> np.ndarray:
    return (src / 255) ** (1 / fac) * 255


factor = 0.5, 2  # współczynniki gamma
img = np.asarray(Image.open("lab1_gray.png"))

plt.figure("Zadanie 7")

plt.subplot(1, 3, 1)
plt.title("Oryginał")
plt.imshow(img, cmap="gray")

plt.subplot(1, 3, 2)
plt.title(f"Gamma factor {factor[0]}")
plt.imshow(gamma_correct(img, factor[0]), cmap="gray")

plt.subplot(1, 3, 3)
plt.title(f"Gamma factor {factor[1]}")
plt.imshow(gamma_correct(img, factor[1]), cmap="gray")

plt.show()
