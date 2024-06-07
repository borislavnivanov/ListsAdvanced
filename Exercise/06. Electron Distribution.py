def get_shell_size(index) -> int:
    return 2 * (index ** 2)


free_electrons = int(input())
distribution = []

while free_electrons > 0:
    space_for_electrons = get_shell_size(len(distribution) + 1)
    if free_electrons >= space_for_electrons:
        distribution.append(space_for_electrons)
        free_electrons -= space_for_electrons
    else:
        distribution.append(free_electrons)
        free_electrons = 0

print(distribution)

