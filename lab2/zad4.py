import matplotlib.image as mpimg
import numpy as np


def calc_bright(src: np.ndarray) -> float:
    # return sum(map(lambda x: sum(x), src)) / (src.shape[0] * src.shape[1])
    res, size = 0.0, src.shape
    for row in src:
        for col in row:
            res += col

    return res / (size[0] * size[1])


def calc_con(src: np.ndarray, dev: float = None) -> float:
    # return (sum(map(lambda x: sum((x - dev) ** 2), src)) / (src.shape[0] * src.shape[1])) ** 0.5
    if dev is None:
        dev = calc_bright(src)

    res, size = 0.0, src.shape
    for row in src:
        for col in row:
            res += (col - dev) ** 2

    return (res / (size[0] * size[1])) ** 0.5


def convert_to(src: np.ndarray, dst_min: int, dst_max: int, dst_type: type) -> np.ndarray:
    src_min = src.min()
    src_max = src.max()

    scale = (dst_max - dst_min) / (src_max - src_min)
    return (scale * src).astype(dst_type)


img = mpimg.imread("lab1_gray.png").astype(np.float64)
brightness, contrast = calc_bright(img), calc_con(img)

uint8img = convert_to(img, 0, 255, np.uint8)
brightness2, contrast2 = calc_bright(uint8img), calc_con(uint8img)

print("Double brightness: ", brightness)
print("Double contrast: ", contrast)
print("Uint8 brightness: ", brightness2)
print("Uint8 contrast: ", contrast2)