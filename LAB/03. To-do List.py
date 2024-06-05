to_do_list = [0] * 10

while True:
    com = input().split('-')
    if com[0] == 'End':
        break
    else:
        to_do_list.pop(int(com[0])-1)
        to_do_list.insert(int(com[0])-1, com[1])

print([x for x in to_do_list if x != 0])