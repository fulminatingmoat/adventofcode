import pprint
import itertools
with open('./2021/8/data', 'r') as f:
    data = f.readlines()

segs = [[0,1,2,4,5,6],[2,5],[0,2,3,4,6],[0,2,3,5,6],[1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]]

def solve(data):
    data = [(line.split('|')[0].split(), line.split('|')[1].split()) for line in data]
    segments = [[] for _ in range(7+1)]
    count = 0
    for signals, outputs in data:
        for signal in signals:
            siglen = len(signal)
            if siglen == 2:
                # 2
                segments[2].append(tuple(signal))
                segments[5].append(tuple(signal))
            if siglen == 4:
                # 4 
                segments[1].append(tuple(signal))
                segments[2].append(tuple(signal))
                segments[3].append(tuple(signal))
                segments[5].append(tuple(signal))
            if siglen == 3:
                # 7
                segments[0].append(tuple(signal))
                segments[2].append(tuple(signal))
                segments[5].append(tuple(signal))
            if siglen == 7:
                # 8
                pass
        for output in outputs:
            if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
                count+=1
    return count

def solve_2(data):
    data = [(line.split('|')[0].split(), line.split('|')[1].split()) for line in data]
    count = 0
    for signals, outputs in data:
        #1 4 7 8 9
        segments = [[] for _ in range(7)]
        seven = set(list(filter(lambda x: len(x) == 3, signals))[0])
        one = set(list(filter(lambda x: len(x) == 2, signals))[0])
        eight = set(list(filter(lambda x: len(x) == 7, signals))[0])
        four = set(list(filter(lambda x: len(x) == 4, signals))[0])
        segments[0] = set(seven - one)
        segments[5] = set(filter(lambda x: list(''.join(signals)).count(x) == 9, list('abcdefg')))
        segments[1] = set(filter(lambda x: list(''.join(signals)).count(x) == 6, list('abcdefg')))
        segments[2] = one - segments[5]
        segments[4] = set(filter(lambda x: list(''.join(signals)).count(x) == 4, list('abcdefg')))
        segments[3] = (four - one) - segments[1]
        segments[6] = eight - four - segments[0] - segments[4]
        val = []
        for output in outputs:
            numseg = []
            added = False
            for x in range(7):
                if list(segments[x])[0] in output:
                    numseg.append(x)
            for i, y in enumerate(segs):
                if y == sorted(numseg):
                    val.append(str(i))
        count+=int(''.join(val))
    return count


def solve_2_clean(data):
    data = [(line.split('|')[0].split(), line.split('|')[1].split()) for line in data]
    count = 0
    for signals, outputs in data:
        seven = set(list(filter(lambda x: len(x) == 3, signals))[0])
        one = set(list(filter(lambda x: len(x) == 2, signals))[0])
        eight = set(list(filter(lambda x: len(x) == 7, signals))[0])
        four = set(list(filter(lambda x: len(x) == 4, signals))[0])
        val = []
        for output in outputs:
            if len(set(output)) == 6:
                if set(output).issuperset(four):
                    val.append(9)
                elif set(output).issuperset(one) and not set(output).issuperset(four):
                    val.append(0)
                else:
                    val.append(6)
            elif len(set(output)) == 5:
                if set(output).issuperset(one):
                    val.append(3)
                elif len(set(output).intersection(four)) == 3:
                    val.append(5)
                else:
                    val.append(2)
            else:
                if len(output) == 3:
                    val.append(7)
                elif len(output) == 2:
                    val.append(1)
                elif len(output) == 4:
                    val.append(4)
                else:
                    val.append(8)
        count+=int(''.join(list(map(str, val))))
    return count

print(solve(data))
print(solve_2(data))

print(solve_2_clean(data))