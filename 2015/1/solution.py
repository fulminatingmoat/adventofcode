with open('2015/1/data', 'r') as f:
    data = f.read()

def solve(data):
    return data.count('(') - data.count(')')

def solve_2(data):
    floor = 0
    for i, c in enumerate(data):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1

print(solve(data))
print(solve_2(data))