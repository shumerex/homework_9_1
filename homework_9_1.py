def by_3(x):
    return x ** 2

def is_odd(x):
    return x % 2

my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(by_3, filter(is_odd, my_numbers))
print(list(result))


my_numbers1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = [x ** 2 for x in my_numbers1 if x % 2]
print(result)