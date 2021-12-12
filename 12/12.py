from pathlib import Path
from collections import defaultdict,Counter

caves=defaultdict(set)

with open(Path(__file__).parent/'12.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        c,child=l.split('-')
        if child != 'start':
            caves[c].add(child)
        if c!='start':
            caves[child].add(c)


def find_path(cave:str,visited:list,paths:list):
    if cave=='end':
        paths.append([*visited]+['end'])
        return
    if cave.islower() and cave in visited:
        return
    visited.append(cave)
    for c in caves[cave]:
        find_path(c,visited,paths)
    visited.pop()

def find_path_one_lower_repeat(cave:str,visited:list,paths:list):
    if cave=='end':
        paths.append([*visited]+['end'])
        return
    if cave.islower() and cave in visited:
        c=Counter()
        for v in filter(lambda x:x.islower(),visited):
            c[v]+=1
        if 2 in c.values():
            return
    visited.append(cave)
    for c in caves[cave]:
        find_path_one_lower_repeat(c,visited,paths)
    visited.pop()

def part1():
    paths=[]
    visited=[]
    find_path('start',visited,paths)
    print(len(paths))

def part2():
    paths=[]
    visited=[]
    find_path_one_lower_repeat('start',visited,paths)
    print(len(paths))

if __name__=='__main__':
    part1()
    part2()