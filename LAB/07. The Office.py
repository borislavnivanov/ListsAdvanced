empl_happiness = map(int, input().split())
factor = int(input())

empl_happiness = list(map(lambda x: x * factor, empl_happiness))
average_score = list(filter(lambda a: a >= sum(empl_happiness) / len(empl_happiness), empl_happiness))

if len(average_score) >= len(empl_happiness) / 2:
    print(f'Score: {len(average_score)}/{len(empl_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(average_score)}/{len(empl_happiness)}. Employees are not happy!')