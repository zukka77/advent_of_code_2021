from pathlib import Path

with open(Path(__file__).parent/'03.in','r',encoding='utf8') as f:
    lines=list(map(lambda l:l.strip(),f.readlines()))

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
    part2()