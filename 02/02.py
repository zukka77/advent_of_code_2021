from collections import namedtuple


Command=namedtuple("Command",["dir","value"])

with open('02.in','r',encoding='utf-8') as f:
    lines=f.readlines()

def part1():
    pos=depth=0
    for l in lines:
        c=Command._make(l.split())
        if c.dir=='forward':
            pos+=int(c.value)
        if c.dir=="up":
            depth-=int(c.value)
        if c.dir=="down":
            depth+=int(c.value)
    print(depth*pos)

def part2():
    pos=depth=aim=0
    for l in lines:
        c=Command._make(l.split())
        if c.dir=='forward':
            pos+=int(c.value)
            depth+=aim*int(c.value)
        if c.dir=="up":
            aim-=int(c.value)
        if c.dir=="down":
            aim+=int(c.value)
    print(depth*pos)

if __name__=='__main__':
    part1()
    part2()