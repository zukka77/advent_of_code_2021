from pathlib import Path

with open(Path(__file__).parent/'07.in','r',encoding='utf8') as f:
    positions=list(map(int,f.readlines()[0].split(',')))

def part1():
    #positions=list(map(int,"16,1,2,0,4,2,7,1,2,14".split(',')))
    max_pos=max(positions)
    pos_fuel=[0 for _ in range(max_pos)]
    for i in range(len(pos_fuel)):
        for c in positions:
            pos_fuel[i]+=abs(c-i)
    print(min(pos_fuel))

def part2():
    #positions=list(map(int,"16,1,2,0,4,2,7,1,2,14".split(',')))
    max_pos=max(positions)
    pos_fuel=[0 for _ in range(max_pos)]
    for i in range(len(pos_fuel)):
        for c in positions:
            #pos_fuel[i]+=sum(range(abs(c-i)+1))
            pos_fuel[i]+=abs(c-i)*(abs(c-i)+1)//2
    print(min(pos_fuel))



if __name__ == '__main__':
    part1()
    part2()