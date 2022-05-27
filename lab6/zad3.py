import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def disk(x: float, y: float) -> np.ndarray:
    ret = np.zeros((x, y), np.uint8)
    xx, yy = np.mgrid[:x, :y]
    radius_x, radius_y = x // 2, y // 2
    ret[(xx - radius_x) ** 2 + (yy - radius_y) ** 2 <= radius_x * radius_y] = 1
    return ret


filename = "church.jpg"
img = np.asarray(Image.open(filename).convert('L'), dtype=np.int16)
mask = disk(5, 5)

dilated_img = cv.dilate(img, mask, iterations=1)

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(img, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Dylatacja")
plt.imshow(dilated_img, cmap="gray")

plt.show()
