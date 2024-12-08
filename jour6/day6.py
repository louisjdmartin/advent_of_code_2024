import sys
import time
import os
import copy


def read_map(input_file, output_map):
    x, y = 0, 0
    line_count = 0
    for line in input_file.readlines():
        if("^") in line:
            x = line_count
            y = line.find("^")
        output_map.append(list(line.strip()))
        line_count += 1


    return x, y

def print_map(output_map):
    for line in output_map:
        for col in line:
            print(col, end="")
        print()

def move_guard(map_guard, guard_position):
    ## RULES: If nothing => Move forward
    ## If obstacle (#) => Turn right
    ## If outside (O) => STOP
    if(get_next_position(map_guard, guard_position) == "#"):
        turn_right(map_guard, guard_position)

    elif(get_next_position(map_guard, guard_position) == "O"):
        map_guard[guard_position[0]][guard_position[1]] = "X"
        return False
    
    else:
        forward(map_guard, guard_position)




    return True

def forward(map_guard, guard_position):
    orientation = map_guard[guard_position[0]][guard_position[1]]
    map_guard[guard_position[0]][guard_position[1]] = "X"
    if(orientation == "^"):
        guard_position[0] = guard_position[0] - 1
    if(orientation == ">"):
        guard_position[1] = guard_position[1] + 1
    if(orientation == "<"):
        guard_position[1] = guard_position[1] - 1
    if(orientation == "V"):
        guard_position[0] = guard_position[0] + 1
    map_guard[guard_position[0]][guard_position[1]] = orientation


def turn_right(map_guard, guard_position):
    orientation = map_guard[guard_position[0]][guard_position[1]]
    if(orientation == "^"):
        next_o = ">"
    if(orientation == ">"):
        next_o = "V"
    if(orientation == "V"):
        next_o = "<"
    if(orientation == "<"):
        next_o = "^"
    map_guard[guard_position[0]][guard_position[1]] = next_o

def get_next_position(map_guard, guard_position):
    orientation = map_guard[guard_position[0]][guard_position[1]]
    if(orientation == "^"):
        if(guard_position[0] == 0):
            return "O"
        else:
            return map_guard[guard_position[0]-1][guard_position[1]]
    if(orientation == ">"):
        if(guard_position[1] == len(map_guard[0])-1):
            return "O"
        else:
            return map_guard[guard_position[0]][guard_position[1]+1]
    if(orientation == "<"):
        if(guard_position[1] == 0):
            return "O"
        else:
            return map_guard[guard_position[0]][guard_position[1]-1]
    if(orientation == "V"):
        if(guard_position[0] == len(map_guard)-1):
            return "O"
        else:
            return map_guard[guard_position[0]+1][guard_position[1]]


if __name__ == "__main__":
    input_file = open(sys.argv[1],"r")

    map_guard = []

    guard_position_start = read_map(input_file, map_guard)

    original_map = copy.deepcopy(map_guard)


    guard_position = [guard_position_start[0], guard_position_start[1]]

    while(move_guard(map_guard, guard_position)):
        #os.system('cls' if os.name == 'nt' else 'clear')
        #print_map(map_guard)
        #print("GUARD AT %d,%d" % (guard_position[0], guard_position[1]), end="\r")
        #time.sleep(.1)
        pass

    print()
    positions = 0
    for line in map_guard:
        positions += line.count("X")
    
    final_map = copy.deepcopy(map_guard)
    print("Part 1: %d" % positions)
    retry_map = []
    map_size_y = len(final_map[0])
    boucles = 0
    count_trys = 0
    for x in range(len(final_map)):
        for y in range(map_size_y):
            if(final_map[x][y]=="X"):
                
                count_trys += 1
                del retry_map
                retry_map = copy.deepcopy(original_map)
                retry_map[x][y] = "#"
                iters = 0
                stop_iter = False
                
                guard_position = [guard_position_start[0], guard_position_start[1]]
                while(move_guard(retry_map, guard_position) and not stop_iter):
                    iters += 1
                    if (iters>100000):
                        boucles += 1
                        stop_iter = True
                if(count_trys%100 == 0):
                    print("Try %d/%d"%(count_trys,positions))
    print("Part 2: %d" % (boucles-1))
