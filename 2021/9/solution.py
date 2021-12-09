import pprint, itertools, collections, sys, re, os, time, math, statistics, functools, copy

with open('./2021/9/data', 'r') as f:
    data = [list(map(int, list(x.strip()))) for x in f.readlines()]


def solve(data):
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            checks = True
            if x > 0:
                if data[y][x-1] <= data[y][x]:
                    checks = False
            if x < len(data[y])-1:
                if data[y][x+1] <= data[y][x]:
                    checks = False
            if y > 0:
                if data[y-1][x] <= data[y][x]:
                    checks = False
            if y < len(data)-1:
                if data[y+1][x] <= data[y][x]:
                    checks = False
            if checks:
                count += data[y][x]+1
    return count

def check_basin(data, basins):
    ilen = len(basins)
    endb = basins[::]
    for basin in basins:
        x,y = basin
        if x > 0:
            if data[y][x-1] >= data[y][x] and data[y][x-1] != 9:
                endb.append((x-1,y))
        if x < len(data[y])-1:
            if data[y][x+1] >= data[y][x] and data[y][x+1] != 9:
                endb.append((x+1,y))
        if y > 0:
            if data[y-1][x] >= data[y][x] and data[y-1][x] != 9:
                endb.append((x,y-1))
        if y < len(data)-1:
            if data[y+1][x] >= data[y][x] and data[y+1][x] != 9:
                endb.append((x,y+1))
        
    endb = list(set(endb))
    if len(endb) == ilen:
        return basins
    else:
        return check_basin(data, endb)

def solve_2(data):
    basins = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            checks = True
            if x > 0:
                if data[y][x-1] <= data[y][x]:
                    checks = False
            if x < len(data[y])-1:
                if data[y][x+1] <= data[y][x]:
                    checks = False
            if y > 0:
                if data[y-1][x] <= data[y][x]:
                    checks = False
            if y < len(data)-1:
                if data[y+1][x] <= data[y][x]:
                    checks = False
            if checks:
                basin = [(x,y)]
                basins.append(len(check_basin(data, basin)))

    return functools.reduce(lambda x,y : x*y, sorted(basins, reverse=True)[:3])

print(solve(data))
print(solve_2(data))