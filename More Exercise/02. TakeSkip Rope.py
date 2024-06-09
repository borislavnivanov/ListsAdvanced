start_list = list(input())

numbers = []
even_n = []
odd_n = []
text = []
result = ''


for char in start_list:
    if char.isdigit():
        numbers.append(int(char))
    else:
        text.append(char)

for i in range(len(numbers)):
    if i % 2 == 0:
        even_n.append(numbers[i])
    else:
        odd_n.append(numbers[i])

for take, skip in zip(even_n, odd_n):
    if take != 0:
        result = result + ''.join(text[:take])
        text = text[skip + take:]
    else:
        text = text[skip + take:]

print(result)
