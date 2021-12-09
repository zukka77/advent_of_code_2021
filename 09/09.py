from os import name
from pathlib import Path
from collections import namedtuple
from functools import reduce
Point=namedtuple("Point",["r","c","value"])
field=[]
mins=[]
with open(Path(__file__).parent/'09.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        field.append(list(map(int,l)))


def part1():
    for r in range(len(field)):
        for c in range(len(field[0])):
            if r>=1 and field[r][c]>=field[r-1][c]:
                continue
            if r<=len(field)-2 and field[r][c]>=field[r+1][c]:
                continue
            if c>=1 and field[r][c] >= field[r][c-1]:
                continue
            if c<=len(field[0])-2 and field[r][c] >= field[r][c+1]:
                continue
            mins.append(Point(r,c,field[r][c]))
    print(sum(map(lambda x:x.value+1,mins)))

def find_basin(start:Point,neighbour:set):
    if start.r>=1 and field[start.r-1][start.c]!=9:
        up=Point(start.r-1,start.c,field[start.r-1][start.c])
        if up not in neighbour:
            neighbour.add(up)
            find_basin(up,neighbour)
    if start.r<=len(field)-2 and field[start.r+1][start.c]!=9:
        down=Point(start.r+1,start.c, field[start.r+1][start.c])
        if down not in neighbour:
            neighbour.add(down)
            find_basin(down,neighbour)
    if start.c>=1 and field[start.r][start.c-1]!=9:
        left=Point(start.r,start.c-1,field[start.r][start.c-1])
        if left not in neighbour:
            neighbour.add(left)
            find_basin(left,neighbour)
    if start.c<=len(field[0])-2 and field[start.r][start.c+1]!=9:
        right=Point(start.r,start.c+1,field[start.r][start.c+1])
        if right not in neighbour:
            neighbour.add(right)
            find_basin(right,neighbour)

def part2():
    basins=[]
    for p in mins:
        members=set()
        find_basin(p,members)
        basins.append({'min':p,'members':members,'size':len(members)})
    basins.sort(key=lambda x:x['size'],reverse=True)
    print(reduce(lambda a,e:a*e,map(lambda x:x['size'],basins[:3]),1))


if __name__=='__main__':
    part1()
    part2()