size = int(input())

train = [int(0) for x in range(size)]

while True:
    action = input().split()
    if action[0] == 'End':
        break
    elif action[0] == 'add':
        train[-1] = train[-1] + int(action[1])
    elif action[0] == 'insert':
        train[int(action[1])] = train[int(action[1])] + int(action[2])
    elif action[0] == 'leave':
        train[int(action[1])] = train[int(action[1])] - int(action[2])

print(train)
