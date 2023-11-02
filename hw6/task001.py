from typing import List


def binary_search(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = [1, 2, 7, 6, 11, 33, 45]

    print(f"Входящий массив: {arr}")
    number = int(input("Введите элемент к поиску: "))
    result = binary_search(arr, number)

    if result == -1:
        print("Элемент не найден в массиве")
    else:
        print(f"Элемент: {number} в массиве с индексом: {result}")


if __name__ == "__main__":
    main()
