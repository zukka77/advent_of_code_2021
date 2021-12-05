from pathlib import Path

with open(Path(__file__).parent/'05.in','r',encoding='utf8') as f:
    lines=list(map(lambda l:l.strip(),f.readlines()))

def print_field(f):
    #print (f)
    for y in range(len(f)):
        for x in range(len(f)):
            print(f"{f[x][y]}",end='')
        print()
    

def part1():
    field=[[0 for y in range(1000)] for x in range(1000)]
    for l in lines:
        parts=l.split('->')
        x1,y1=list(map(int,parts[0].split(',')))
        x2,y2=list(map(int,parts[1].split(',')))
        if x1==x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                field[x1][y]+=1
        elif y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                field[x][y1]+=1
    dangerous=0
    for col in field:
        dangerous+=len(list(filter(lambda x: x>1,col)))
    print(dangerous)

def part2():
    field=[[0 for y in range(1000)] for x in range(1000)]
    for l in lines:
        parts=l.split('->')
        x1,y1=list(map(int,parts[0].split(',')))
        x2,y2=list(map(int,parts[1].split(',')))
        if x1==x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                field[x1][y]+=1
        elif y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                field[x][y1]+=1
        elif abs(x1-x2)==abs(y1-y2):
            for c  in range(abs(x1-x2)+1):
                field[x1 + (c * (1 if x1 <= x2 else -1))][y1 + (c * (1 if y1<=y2 else -1))]+=1
    dangerous=0
    for col in field:
        dangerous+=len(list(filter(lambda x: x>1,col)))
    print(dangerous)

if __name__=='__main__':
    part1()
    part2()
   