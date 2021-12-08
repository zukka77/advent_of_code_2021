from pathlib import Path
from collections import namedtuple

Pattern=namedtuple("Pattern",['wires','output'])
patterns=[]
with open(Path(__file__).parent/'08.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        wires,output=list(map(lambda x:x.split(),l.split('|')))
        p=Pattern(list(map(lambda x:''.join(sorted(x)),wires)),list(map(lambda x:''.join(sorted(x)),output)))
        patterns.append(p)


def part1():
    print (len(list(filter(lambda x:len(x) in [2,3,4,7],[y for x in patterns for y in x.output ]))))

def part2():
    s=0
    for p in patterns:
        combo=[None for x in range(10)]
        combo[1]=list(filter(lambda x:len(x)==2,p.wires))[0]
        combo[7]=list(filter(lambda x:len(x)==3,p.wires))[0]
        combo[4]=list(filter(lambda x:len(x)==4,p.wires))[0]
        combo[8]=list(filter(lambda x:len(x)==7,p.wires))[0]
        #find 0 (contains 7), 6 or 9(contains 4)
        for tmp in filter(lambda x:len(x)==6,p.wires):
            if all(l in tmp for l in combo[4]):
                combo[9]=tmp
            elif all(l in tmp for l in combo[7]):
                combo[0]=tmp
            else:
                combo[6] = tmp
        #find 3 (contains 7), 5 (is contained in 9) and 2
        for tmp in filter(lambda x:len(x)==5,p.wires):
            if all(l in tmp for l in combo[7]):
                combo[3]=tmp
            elif all(l in combo[9] for l in tmp):
                combo[5]=tmp
            else:
                combo[2]=tmp
        #reverse lookup
        combo2n={c:str(n) for n,c in enumerate(combo)}
        number=""
        for o in p.output:
            try:
                number+=combo2n[o]
            except:
                print (f"{p}\n{combo}\n{combo2n}\n{o}")
                return
            
        s+=int(number)
    print (s)
if __name__=='__main__':
    part1()
    part2()