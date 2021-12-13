from pathlib import Path
from collections import namedtuple

Point=namedtuple('Point',["x","y"])
Fold=namedtuple('Fold',["direction","value"])
points=set()
folds=[]
max_x=0
max_y=0
with open(Path(__file__).parent/'13.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        parts=l.split(',')
        if len(parts)==2:
            parts=list(map(int,parts))
            points.add(Point(*parts))
            max_x=max(max_x,parts[0])
            max_y=max(max_y,parts[1])
        else:
            l=l[len("fold along "):]
            parts=l.split("=")
            folds.append(Fold(parts[0],int(parts[1])))

def part1():
    global max_x,max_y
    for fold in [folds[0]]:
        if fold.direction == 'x':
            for p in list(points):
                if p.x > fold.value:
                    points.remove(p)
                    points.add(Point(fold.value-(p.x-fold.value),p.y))
                    max_x=max_x-(max_x-fold.value)
        else:
            for p in list(points):
                if p.y > fold.value:
                    points.remove(p)
                    points.add(Point(p.x,fold.value-(p.y-fold.value)))
                    max_y=max_y-(max_y-fold.value)
    print(len(points))

def part2():
    global max_x,max_y
    for fold in folds[1:]:
        if fold.direction == 'x':
            for p in list(points):
                if p.x > fold.value:
                    points.remove(p)
                    points.add(Point(fold.value-(p.x-fold.value),p.y))
                    max_x=max_x-(max_x-fold.value)
        else:
            for p in list(points):
                if p.y > fold.value:
                    points.remove(p)
                    points.add(Point(p.x,fold.value-(p.y-fold.value)))
                    max_y=max_y-(max_y-fold.value)
    for y in range (max_y+1):
        for x in range(max_x+1):
            if Point(x,y) in points:
               print("#",end='')
            else:
               print(".",end='')
        print()
if __name__=='__main__':
    part1()
    part2()
  