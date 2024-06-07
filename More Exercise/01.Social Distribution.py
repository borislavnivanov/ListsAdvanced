population = list(map(int, input().split(', ')))
minimum = int(input())

if sum(population) < len(population)*minimum:
    print('No equal distribution possible')
else:
    for i in range(len(population) - 1):
        if population[i] < minimum:
            dif = minimum - population[i]
            if population[-1] - dif >= minimum:
                population[-1] -= dif
            elif population[-2] - dif >= minimum:
                population[-2] -= dif
            elif population[-3] - dif >= minimum:
                population[-3] -= dif
            elif population[-4] - dif >= minimum:
                population[-4] -= dif
            else:
                print('No equal distribution possible')
                break
            population[i] += dif
    print(population)