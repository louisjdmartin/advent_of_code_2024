import sys


def find_next(x,y,symbol,map):
    y += 1
    while(x<len(map)):
        while(y<len(map[0])):
            if(map[x][y] == symbol):
                return(x,y)
            y+=1       
        x+=1
        y=0
    return(-1,-1)

def gen_antinodes(x1,y1,x2,y2,antinode_map):
    if(x2 == -1):
        return
    dist_x = x1-x2
    dist_y = y1-y2

    try:
        if(x2-dist_x>=0 and y2-dist_y>=0):
            antinode_map[x2-dist_x][y2-dist_y] = "#"
    except IndexError:
        pass

    try:
        if(x1+dist_x>=0 and y1+dist_y>=0):
            antinode_map[x1+dist_x][y1+dist_y] = "#"
    except IndexError:
        pass

def gen_antinodes_2(x1,y1,x2,y2,antinode_map):
    if(x2 == -1):
        return
    dist_x = x1-x2
    dist_y = y1-y2

    try:
        i = 0
        while(x2-dist_x*i>=0 and y2-dist_y*i>=0):
            antinode_map[x2-dist_x*i][y2-dist_y*i] = "#"
            i+=1
    except IndexError:
        pass

    try:
        i = 0
        while(x1+dist_x*i>=0 and y1+dist_y*i>=0):
            antinode_map[x1+dist_x*i][y1+dist_y*i] = "#"
            i+=1
    except IndexError:
        pass

if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')

    antinode_map = []
    antinode_part2_map = []
    antenna_map = []
    for line in input_file.readlines():
        antenna_map.append(list(line.strip()))
        antinode_map.append(list("."*len(line.strip())))
        antinode_part2_map.append(list("."*len(line.strip())))


    xs = range(len(antenna_map))
    ys = range(len(antenna_map[0]))
    for x in xs:
        for y in ys:
            if(antenna_map[x][y] != "."):
                compar_x, compar_y = x, y
                next_x, next_y = x, y
                symbol = antenna_map[x][y]
                while((next_x, next_y) != (-1, -1)):
                    next_x, next_y = find_next(next_x,next_y,symbol,antenna_map)
                    gen_antinodes(compar_x, compar_y, next_x, next_y, antinode_map)
                    gen_antinodes_2(compar_x, compar_y, next_x, next_y, antinode_part2_map)

    part_1 = 0
    for line in antinode_map:
        part_1 += line.count("#")
    print("Part 1: %d" % part_1)


    part_2 = 0
    for line in antinode_part2_map:
        part_2 += line.count("#")
    print("Part 2: %d" % part_2)