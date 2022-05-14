import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np

UINT8_DIM = (0, 255)  # zakres kolorów dla uint8


def change_contrast(src: np.ndarray, val: float) -> np.ndarray:
    return np.clip(src * float(val), *UINT8_DIM).astype(np.uint8)  # przycinamy zakres po mnożeniu


def change_brightness(src: np.ndarray, val: float) -> np.ndarray:
    return np.clip(src + float(val), *UINT8_DIM).astype(np.uint8)  # przycinamy zakres po sumowaniu


examples = 4  # ilość wytworzonych przykładów (powyżej 5 wynik staje się nieczytelny)

files = ["gray1.jpeg", "2.jpg", "3.jpg", "4.jpg", "lab1_color.png"] # wczytane obrazy są w trybie RGB
imgs = [np.asarray(Image.open(f)) for f in files]  # tablica z obrazami

brightness = [x * 25 * (-1) ** x for x in range(1, examples + 2)]  # tablica z poziomami jasności
contrast = [(5 / x) ** ((-1) ** x) for x in range(1, examples + 2)]  # tablica z poziomami kontrastu

for i, img in enumerate(imgs):
    fig, ax = plt.subplots(2, examples + 1, num=f"zadanie 5.{i+1}: ({files[i]})")
    fig.tight_layout()
    ax[0, 0].imshow(img, cmap="gray")
    ax[0, 0].set_title("Contrast [Oryginał]")
    ax[1, 0].imshow(img, cmap="gray")
    ax[1, 0].set_title("Brightness [Oryginał]")
    for e in range(examples):
        ax[0, e + 1].imshow(change_contrast(img, contrast[e]), cmap="gray")
        ax[0, e + 1].set_title(f"Contrast [{contrast[e]}]")
        ax[1, e + 1].imshow(change_brightness(img, brightness[e]), cmap="gray")
        ax[1, e + 1].set_title(f"Brightness [{brightness[e]}]")

plt.show()
