from os import close
from pathlib import Path
from collections import Counter

chunks=[]
with open(Path(__file__).parent/'10.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        chunks.append(l)

close_open=dict(zip((')',']','}','>'),('(','[','{','<')))
open_close=dict(zip(close_open.values(),close_open.keys()))
wrong_points={
    ')': 3 ,
    ']': 57 ,
    '}': 1197 ,
    '>': 25137 ,
}
close_points={
    ')': 1 ,    
    ']': 2 ,
    '}': 3 ,
    '>': 4 ,
}
def part1():
    wrongs=Counter()
    for chunk in chunks:
        sep=[]
        for c in chunk:
            if c in '([{<':
                sep.append(c)
                continue
            if close_open[c] != sep[-1]:
                wrongs[c]+=1
                break
            sep.pop()
    print(sum(map(lambda x:wrongs[x]*wrong_points[x],wrongs.keys())))
    
def part2():
    completions=[]
    for chunk in chunks:
        sep=[]
        completion=[]
        corrupted=False
        for c in chunk:
            if c in '([{<':
                sep.append(c)
                continue
            if close_open[c] != sep[-1]:
                corrupted=True
                break
            sep.pop()
        if not corrupted:
            for s in reversed(sep):
                completion.append(open_close[s])
            completions.append(completion)
    scores=[]
    for completion in completions:
        score=0
        for c in completion:
            score=score*5+close_points[c]
        scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])



if __name__=='__main__':
    part1()
    part2()