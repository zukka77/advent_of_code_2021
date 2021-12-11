from pathlib import Path

start_field=[]
with open(Path(__file__).parent/'11.in','r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        if not l: continue
        start_field.append(list(map(int,l)))
nrows=len(start_field)
ncols=len(start_field[0])

def print_field(field):
    for r in field:
        print (r)
def part1():
    #get a copy of the field
    field=[list(row) for row in start_field]
    flashes=[]
    flash_count=0
    first_flash_found=False
    for step in range(100):
        for r in range(nrows):
            for c in range(ncols):
                field[r][c]+=1
                if field[r][c] > 9:
                    flash_count+=1
                    flashes.append((r,c))
        
        #increment neighbour
        while flashes:
            for f in flashes:
                rrange_from=f[0]-1 if f[0]-1 >=0 else 0
                rrange_to=f[0]+2 if f[0]+2<=nrows else nrows
                crange_from=f[1]-1 if f[1]-1 >=0 else 0
                crange_to=f[1]+2 if f[1]+2 <=ncols else ncols
                for r in range(rrange_from,rrange_to):
                    for c in range(crange_from,crange_to):
                        try:
                            if (r,c) != f and field[r][c]<=9:
                                field[r][c]+=1
                                if field[r][c] > 9:
                                    flash_count+=1
                                    flashes.append((r,c))
                        except:
                            print(f"r:{r} c:{c}")
                            print_field()
                            raise

                flashes.remove(f)

        #reset flashed to 0
        for r in range(nrows):
            for c in range(ncols):
                if field[r][c] > 9:
                    field[r][c]=0
    print (flash_count)

def part2():
    #get a copy of the field
    field=[list(row) for row in start_field]
    flashes=[]
    all_flashed=False
    step=0
    while not all_flashed:
        step+=1
        for r in range(nrows):
            for c in range(ncols):
                field[r][c]+=1
                if field[r][c] > 9:
                    flashes.append((r,c))
        
        #increment neighbour
        while flashes:
            for f in flashes:
                rrange_from=f[0]-1 if f[0]-1 >=0 else 0
                rrange_to=f[0]+2 if f[0]+2<=nrows else nrows
                crange_from=f[1]-1 if f[1]-1 >=0 else 0
                crange_to=f[1]+2 if f[1]+2 <=ncols else ncols
                for r in range(rrange_from,rrange_to):
                    for c in range(crange_from,crange_to):
                        try:
                            if (r,c) != f and field[r][c]<=9:
                                field[r][c]+=1
                                if field[r][c] > 9:
                                    flashes.append((r,c))
                        except:
                            print(f"r:{r} c:{c}")
                            print_field()
                            raise

                flashes.remove(f)

        #reset flashed to 0
        #if all are zeroed (100) we had all flash
        nzeroed=0
        for r in range(nrows):
            for c in range(ncols):
                if field[r][c] > 9:
                    field[r][c]=0
                    nzeroed+=1

        if nzeroed==(nrows*ncols):
            all_flashed=True
  
    print (step)
    
if __name__=='__main__':
    part1()
    part2()