from pathlib import Path

with open(Path(__file__).parent/'03.in','r',encoding='utf8') as f:
    lines=list(map(lambda l:l.strip(),f.readlines()))

def part1():
    liness="""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    #lines=lines.splitlines()
    bit_counters=[]
    for bits in lines:
        for i,b in enumerate(bits.strip()):
            if len(bit_counters)<i+1:
                bit_counters.append({0:0,1:0})
            if b=='0':
                bit_counters[i][0]+=1
            else:
                bit_counters[i][1]+=1
    gamma=['0' if x[0]>x[1] else '1' for x in bit_counters]
    epsilon=['0' if x[0]<x[1] else '1' for x in bit_counters]

    gamma=''.join(gamma)
    epsilon=''.join(epsilon)
    print(f"gamma: {gamma} epsilon: {epsilon}")
    gamma=int(gamma,2)
    epsilon=int(epsilon,2)
    print(f"gamma: {gamma} epsilon: {epsilon} lines:{len(lines)} len_bit_counters:{len(bit_counters)}")
    print(bit_counters)
    print (gamma*epsilon)




def find_o2_regen(lines,pos=0,val=[]):
    bits=[b[pos] for b in lines]
    val.append('0' if bits.count('0') > bits.count('1') else '1')
    lines=list(filter(lambda l:l.startswith(''.join(val)),lines))
    if len(lines)==1:
        return lines[0]
    return find_o2_regen(lines,pos+1,val)

def find_co2_scrub(lines,pos=0,val=[]):
    bits=[b[pos] for b in lines]
    val.append('0' if bits.count('0') <= bits.count('1') else '1')
    lines=list(filter(lambda l:l.startswith(''.join(val)),lines))
    if len(lines)==1:
        return lines[0]
    return find_co2_scrub(lines,pos+1,val)


def part2(lines=lines):
    o2_regen=find_o2_regen(lines)
    co2_scrub=find_co2_scrub(lines)
    print(f"o2_regen: {o2_regen} {int(o2_regen,2)} co2_scrub:{co2_scrub} {int(co2_scrub,2)}support_rating={int(o2_regen,2)*int(co2_scrub,2)}")


if __name__=='__main__':
    part1()
    part2()