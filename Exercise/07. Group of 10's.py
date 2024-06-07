def is_in_group(n: int, index: int):
    if (index * 10)-10 < n <= index * 10:
        return True
    else:
        return False


numbers = list(map(int, input().split(', ')))
result = []

for i in range(numbers[-1] // 10 + 1):
    temp = []
    for n in range(len(numbers)):
        if is_in_group(numbers[n], i+1):
            temp.append(numbers[n])
    result.append(temp)

if not result[-1]:
    result.pop(-1)
for i in range(len(result)):
    print(f'Group of {i + 1}0\'s: {result[i]}')
