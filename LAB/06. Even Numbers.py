numbers_list = list(map(int, input().split(', ')))
result = map(lambda x: x if numbers_list[x] % 2 == 0 else 'no', range(len(numbers_list)))
print(list(filter(lambda a: a != 'no', result)))