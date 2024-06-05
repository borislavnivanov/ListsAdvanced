words = input().split(' ')
word_to_count = input()
result = []
for word in words:
    if word == ''.join(reversed(word)):
        result.append(word)

print(result)
print(f'Found palindrome {result.count(word_to_count)} times')