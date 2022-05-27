import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def thresh(src: np.ndarray, val: np.uint8) -> np.ndarray:
    ret = src.copy()
    ret[ret < val], ret[ret >= val] = 0, 255
    return ret


filename = "church.jpg"
img = np.asarray(Image.open(filename).convert('L'), dtype=np.int16)

res = [["Oryginał", img]] + \
      [[f"Thresh value: {x}", thresh(img, x)] for x in range(50, 250, 50)] + \
      [["Oryginał", img]] + \
      [[f"Thresh (OpenCV) value: {x}", cv.threshold(img, x, 255, cv.THRESH_BINARY)[1]] for x in range(50, 250, 50)]

fig, ax = plt.subplots(2, len(res) // 2, num="Zadanie 2")
for a, (t, r) in zip(ax.flatten(), res):
    a.imshow(r, cmap="gray")
    a.set_title(t)

plt.show()
