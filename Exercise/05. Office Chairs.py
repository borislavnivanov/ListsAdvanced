rooms = int(input())
free_chairs = 0
flag = True

for i in range(rooms):
    placing = input().split()
    chairs: int = len(placing[0])
    attendees: int = int(placing[1])
    if attendees > chairs:
        print(f'{attendees - chairs} more chairs needed in room {i + 1}')
        flag = False
    else:
        free_chairs += chairs - attendees

if free_chairs >= 0 and flag:
    print(f'Game On, {free_chairs} free chairs left')
