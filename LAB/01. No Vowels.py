text_list = [x for x in input()]

vowels = ['a', 'o', 'u', 'e', 'i']

print(''.join([char for char in text_list if char.lower() not in vowels]))
