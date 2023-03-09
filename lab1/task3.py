def find_four_numbers(arr, k):
    arr.sort() # сортируем массив, чтобы гарантировать, что q1 <= q2 <= q3 <= q4
    result = set() # используем множество для хранения уникальных четверок
    n = len(arr)
    for i in range(n-3): # перебираем все возможные четверки
        for j in range(i+1, n-2):
            left = j+1 # начинаем справа от j
            right = n-1 # начинаем с конца массива
            while left < right: # пока есть непроверенные пары
                if arr[i]+arr[j]+arr[left]+arr[right] == k: # если нашли четверку, добавляем её в результат
                    result.add((arr[i], arr[j], arr[left], arr[right]))
                    left += 1 # и продолжаем искать другие четверки
                    right -= 1
                elif arr[i]+arr[j]+arr[left]+arr[right] < k: # если сумма меньше k, двигаем левый указатель
                    left += 1
                else: # если сумма больше k, двигаем правый указатель
                    right -= 1
    return sorted(result) # возвращаем результат в лексикографическом порядке

# пример использования функции с вводом значений пользователем
arr = []
n = int(input("Введите размер массива: "))
for i in range(n):
    while True: # повторяем запрос, пока не будет введено корректное значение
        try:
            arr.append(int(input(f"Введите число {i+1}: ")))
            break # если введено корректное значение, выходим из цикла
        except ValueError: # если введено некорректное значение, печатаем ошибку и продолжаем цикл
            print("Ошибка: введите целое число.")
while True: # повторяем запрос, пока не будет введено корректное значение
    try:
        k = int(input("Введите целевое значение: "))
        break # если введено корректное значение, выходим из цикла
    except ValueError: # если введено некорректное значение, печатаем ошибку и продолжаем цикл
        print("Ошибка: введите целое число.")
result = find_four_numbers(arr, k)
print(result)