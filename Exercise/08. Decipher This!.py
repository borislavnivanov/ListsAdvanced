secret = input().split()
result = []

for word in secret:
    num = []
    let = []
    for i in range(len(word)):
        if 48 <= ord(word[i]) <= 57:
            num.append(word[i])
        else:
            let.append(word[i])
    num = chr(int(''.join(num)))
    let[0], let[-1] = let[-1], let[0]
    let = ''.join(let)
    result.append(''.join(num + let))

print(' '.join(result))
