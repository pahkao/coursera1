def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 11, 13]  # не находит, если числа не по возрастанию.
my_list2 = my_list[::-1]
# print(my_list2)

print(binary_search(my_list, 3))
print(binary_search(my_list2, 5))  # возвращает None
