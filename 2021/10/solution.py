from pprint import pprint
import statistics


with open('./2021/10/data', 'r') as f:
    data = [list(x.strip()) for x in f.readlines()]

d = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

scores2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def solve(data):
    score = 0
    for line in data:
        o = []
        found = False
        for x in line:
            if x in "([{<":
                o.append(x)
            else:
                if o[-1] == d[x]:
                    o.pop()
                elif found == False:
                    score += scores[x]
                    found = True
    
    return score

def solve_2(data):
    
    inc = []
    for line in data:
        o = []
        score = 0
        found = False
        for x in line:
            if x in "([{<":
                o.append(x)
            else:
                if o[-1] == d[x]:
                    o.pop()
                elif found == False:
                    found = True
        if not found and o:
            for x in o[::-1]:
                score *= 5
                score += scores2[x]
                
            inc.append(score)
    return sorted(inc)


print(solve(data))

print(statistics.median(solve_2(data)))