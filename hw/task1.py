from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'На вход принимаем непустой целочисленный список')
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(bubble_sort(numbers))