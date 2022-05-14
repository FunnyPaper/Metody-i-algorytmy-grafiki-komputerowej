import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np
from typing import Callable  # czysto informacyjnie

def subplot(rows: int, cols: int, start: int = 1) -> Callable:  # funkcja z parametrami do wykorzystania we wrapperze
    def dec(func: Callable) -> Callable:
        num = start  # zmienna do wewnętrznej inkrementacji
        def wrapper(*args: any) -> None:
            nonlocal num
            func((rows, cols, num), *args)  # wywołaj pzesłaną funkcję
            num += 1
        return wrapper
    return dec

@subplot(1, 5)  # dekorator nadzorujący automatyczną zmianę funkcji subplot
def show(splot: tuple[int], title: str, src: np.ndarray) -> None:  # pomocnicza funkcja do wyświetlania obrazów
    plt.subplot(*splot)
    plt.title(title)
    plt.imshow(src)

img = np.asarray(Image.open("24_bit.jpg"))
size = img.shape

mc90 = np.zeros((size[1], size[0], size[2]), dtype=int)
for row in range(size[0]):
    for col in range(size[1]):
        mc90[col, size[0] - 1 - row] = img[row, col]

plt.figure("Zadanie 3")

show("Oryginał", img)
show("Obrót o 90 stopni w lewo", np.rot90(img))
show("Obrót o 90 stopni w prawo", np.rot90(img, -1))
show("Transpozycja oryginału", np.transpose(img, (1, 0, 2)))
show("Obrót o 90 stopni w prawo w pętli", mc90)

plt.show()
