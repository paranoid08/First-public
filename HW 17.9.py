while True:
    try:
        array = list(map(int, input('Введите ЧИСЛА через пробел:').split()))
        n = int(input('Введите число для поиска id его меньшего соседа:'))

    except ValueError:
        print("Неправильный формат ввода. Возможно, Вы ввели букву. Попробуйте еще раз.")
    else:
        print('Правильный ввод!')

        def vstavka_sort(array):
            for i in range(1, len(array)):
                x = array[i]
                idx = i
                while idx > 0 and array[idx - 1] > x:
                    array[idx] = array[idx - 1]
                    idx -= 1
                array[idx] = x
            return array


        def bi_search(n, array):
            left, right = 0, len(array)
            if n < array[left] or n > array[right-1]:
                return 'не получена. Введенное число для поиска вне диапазона списка чисел.'
            while left < right:
                middle = (left + right) // 2
                if array[middle] < n:
                    left = middle + 1
                elif array[middle] == n:
                    return left
                else:
                    right = middle
            return left - 1


        break
print("Отсортированный массив:", vstavka_sort(array))
print("Позиция элемента предшествующего числа:", bi_search(n, array))
















