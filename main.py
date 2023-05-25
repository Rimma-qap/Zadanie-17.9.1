import re


def bubble_sort(array):
    """Сортировка методом пузырька"""

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(array, element, left, right):
    """
        Поиск элемента в массиве с помощью
        алгоритма двоичного поиска
    """

    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] < element <= array[middle + 1]:
        # если элемент удовлетворяет условию,
        return middle  # возвращаем этот индекс

    elif element <= array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)

    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


def main():
    numbers_string = input(
        'Введите произвольную последовательность чисел через пробел: '
    )
    try:
        numbers_list = re.split(' +', numbers_string.strip())
        numbers_list = list(map(float, numbers_list))

    except ValueError:
        print('Необходимо ввести числа через пробел!')

    else:
        try:
            number = float(input('Введите произвольное число: '))

        except ValueError:
            print('Необходимо ввести число!')

        else:
            print('Исходная последовательность: ', numbers_list)
            bubble_sort(numbers_list)
            print('Отсортированная последовательность: ', numbers_list)
            print('Исходное число: ', number)

            if numbers_list[0] < number <= numbers_list[-1]:
                result = binary_search(
                    numbers_list, number, 0, len(numbers_list) - 1
                )
                if isinstance(result, bool):
                    print('Позиция элемента не найдена!')

                else:
                    print('Искомая позиция:', result)
            else:
                print('Позиция элемента не найдена!')


if __name__ == "__main__":
    main()
