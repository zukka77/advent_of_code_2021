from pathlib import Path

class Board():
    def __init__(self,rows):
        self.rows=[[int(n) for n in r.split()] for r in rows]
        #traspose
        self.cols=list(map(list,zip(*self.rows)))
        self.win=False
    
    def mark(self,n):
        for r in self.rows:
            try:
                r.remove(n)
                if not r:
                    self.win=True
            except:
                pass
        for c in self.cols:
            try:
                c.remove(n)
                if not c:
                    self.win=True
            except:
                pass
    
    def get_remain_sum(self):
        sum=0
        for r in self.rows:
            for n in r:
                sum+=n
        return sum
        
    def __str__(self):
        return '\n'.join([' '.join(map(str,r))  for r in self.rows])

with open(Path(__file__).parent/'04.in','r',encoding='utf8') as f:
    lines=list(map(lambda l:l.strip(),f.readlines()))

numbers=lines[0]
numbers=list(map(int,numbers.split(',')))

lines=lines[2:]


def part1():
    boards=[]
    for i in range(0,len(lines),6):
        boards.append(Board(lines[i:i+5]))
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.win:
                print (b.get_remain_sum()*n)
                return

def part2():
    boards=[]
    for i in range(0,len(lines),6):
        boards.append(Board(lines[i:i+5]))
    for n in numbers:
        for b in boards:
            if b.win:
                continue
            b.mark(n)
            if b.win:
                print (b.get_remain_sum()*n)
                
if __name__=='__main__':
    part1()
    part2()
   