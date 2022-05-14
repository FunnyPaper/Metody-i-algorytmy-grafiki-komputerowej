import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np

img = np.asarray(Image.open("gray2.jpg"))
max_thresh, min_thresh = 192, 64  # wartości progów
max_val, min_val = 255, 0  # wynikowe wartości dla progów

thresh_img = img.copy()  # płytka kopia obrazu
thresh_img[thresh_img > max_thresh] = max_val  # indeksowanie logiczne

plt.figure("Zadanie 6")

plt.subplot(1, 2, 1)
plt.title("Oryginał")
plt.imshow(img, cmap="gray")

for r, row in enumerate(thresh_img):
    for c, col in enumerate(row):
        if thresh_img[r, c] < min_thresh:
            thresh_img[r, c] = min_val

plt.subplot(1, 2, 2)
plt.title("Progowanie")
plt.imshow(thresh_img, cmap="gray")

plt.show()
