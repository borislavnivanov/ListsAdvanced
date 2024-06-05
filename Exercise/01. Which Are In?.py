string_list1 = input().split(', ')
string_list2 = input().split(', ')
temp = []
result = []

for string in string_list2:
    for word in string_list1:
        if word in string and word not in result:
            temp.append(word)

result = list(x for x in string_list1 if x in temp)
print(result)