
with open('01.in','r',encoding='utf-8') as f:
    data=f.read()

def part1():
    l=data.splitlines()
    l=list(map(lambda x:int(x),l))
    last=0
    up=0
    for n in l:
        if n>last:
            up+=1
        last=n
    print (up-1)

def part2():
    l=data.splitlines()
    l=list(map(lambda x:int(x),l))
    last=0
    up=0
    for i in range(len(l)):
        if len(l[i:i+3])==3 and sum(l[i:i+3])>last:
            up+=1
        last=sum(l[i:i+3])
    print (up-1)

if __name__=='__main__':
    part1()
    part2()