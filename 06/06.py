from pathlib import Path

with open(Path(__file__).parent/'06.in','r',encoding='utf8') as f:
    fishes_list=list(map(int,f.readlines()[0].split(',')))

def part1():
    #fishes=[3,4,3,1,2]
    fishes=list(fishes_list)
    for day in range(80):
        for i in range(len(fishes)):
            if fishes[i]==0:
                fishes[i]=6
                fishes.append(8)
            else:
                fishes[i]-=1
    print (len(fishes))

def part2():
    fishes_stages=[0 for _ in range(9)]
    for f in fishes_list:
        fishes_stages[f]+=1
    #print(fishes_stages)
    for day in range(256):
        new_state=[0 for _ in range(9)]
        for i,n in enumerate(fishes_stages):
            if i == 0:
                new_state[8]+=n
                new_state[6]+=n
                new_state[0]-=n
            else:
                new_state[i]-=n
                new_state[i-1]+=n
        for i in range(len(fishes_stages)):
            fishes_stages[i]+=new_state[i]
        #print(f"\n{new_state}\n{fishes_stages}\n")
    print (sum(fishes_stages))
if __name__ == '__main__':
    part1()
    part2()