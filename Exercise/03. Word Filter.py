word_list = input().split()
print('\n'.join(word for word in word_list if len(word) % 2 == 0))