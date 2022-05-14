import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np

UINT8_DIM, DOUBLE_DIM = (0, 255), (0, 1)  # zakresy kolorów ([0..255] dla uint8 i [0, 1] dla double)


def calc_bright(src: np.ndarray) -> float:
    size = src.shape
    # wynik zbliżony do natywnej metody src.mean(dtype="float64") -> utrata precyzji
    return sum(map(lambda x: sum(x), src)) / (size[0] * size[1])


def calc_con(src: np.ndarray, dev: float = None) -> float:
    if dev is None:
        dev = calc_bright(src)
    size = src.shape
    # wynik zbiżony do natywnej metody src.std(dtype="float64) -> utrata precyzji
    return (sum(map(lambda x: sum((x - dev) ** 2), src)) / (size[0] * size[1])) ** 0.5


def convert_to(src: np.ndarray, dst_minmax: tuple[int], dst_type: type) -> np.ndarray:
    src_min, src_max = src.min(), src.max()
    if (src_min, src_max) == dst_minmax:
        return src.astype(dst_type)
    dst_min, dst_max = dst_minmax
    a = (dst_max - dst_min) / (src_max - src_min)
    # b = (dst_min - src_min * a)
    # y = ax + b -> a * src + (dst_min - src_min * a) -> a * src - a * src_min + dst_min:
    return (a * (src - src_min) + dst_min).astype(dst_type)


def print_prop(name: str, dtype: type, prop: tuple[tuple[str], tuple[float]]) -> None:
    print(f"{name} [dtype: {dtype}]: ({prop[0][0]}: {prop[1][0]}), ({prop[0][1]}: {prop[1][1]})")


def zip_prop(src: np.ndarray) -> tuple[tuple[str], tuple[float]]:
    brightness = calc_bright(src)
    contrast = calc_con(src, brightness)
    return ("brightness", "contrast"), (brightness, contrast)


def print_decor_ax(ax: plt.Axes, src: np.ndarray, fname: str, color: list[str], ylim: tuple[int]) -> None:
    properties = zip_prop(src)
    ax.set_ylim(ylim)
    ax.set_title(f"{fname}: {src.dtype}")
    ax.bar(*properties, color=color)
    for ind, p in enumerate(properties[1]):
        ax.text(ind, p + 0.05 * ylim[1], str(p), ha="center")
    print_prop(fname, src.dtype, properties)


files = ["lab1_gray.png","gray1.jpeg", "gray2.jpg", "gray3.jpg"]
fig, ax = plt.subplots(len(files), 3, num="zadanie 4")
fig.tight_layout()
for i, f in enumerate(files):
    img = np.asarray(Image.open(f))  # wczytaj obraz
    uint8img = convert_to(img, UINT8_DIM, np.uint8)  # zkonwertuj obraz na uint8
    float64img = convert_to(img, DOUBLE_DIM, np.float64)  # zkonweruj obraz na float64 (double)

    ax[i, 0].set_title(f)
    ax[i, 0].imshow(img, cmap="gray") # pokaż obraz oryginalny

    print_decor_ax(ax[i, 1], uint8img, f, ["#0000aa", "#00aa00"], UINT8_DIM) # przedstaw dane dla typu uint8
    print_decor_ax(ax[i, 2], float64img, f, ["#0000ff", "#00ff00"], DOUBLE_DIM) # przedstaw dane dla typu float64

plt.show()
