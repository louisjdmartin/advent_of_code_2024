import sys
"""
1X
2X
3X
4X
\ Y Y Y Y Y
  1 2 3 4 5
"""

def count_xmas(XMAS_TABLE, x, y):
    return [get_letters(XMAS_TABLE, x, y, 4, i, j)=="XMAS" for j in range(-1,2) for i in range(-1,2)].count(True)

def count_cross_mas(XMAS_TABLE, x, y):
    if(XMAS_TABLE[x][y] != "A"):
        return 0

    word_1 = get_letters(XMAS_TABLE, x-1,y-1,3,1,1)
    word_2 = get_letters(XMAS_TABLE, x-1,y+1,3,1,-1)
    
    if(word_1 == "MAS" or word_1 == "SAM"):
        if(word_2 == "MAS" or word_2 == "SAM"):
            return 1

    return 0

def get_letters(XMAS_TABLE, x, y, size, direction_x, direction_y):
    word = ""
    for i in range(size):
        if(x+direction_x*i < 0 or y+direction_y*i < 0):
            break
        try:
            word+=XMAS_TABLE[x+direction_x*i][y+direction_y*i]
        except IndexError:
            word+=""
    return word


if __name__ == "__main__":

    ## READ FILE
    input_file = open(sys.argv[1])
    XMAS_TABLE = input_file.readlines()
    number_of_xmas = 0
    number_of_mas_cross = 0
    for x in range(len(XMAS_TABLE)):
        for y in range(len(XMAS_TABLE[x])):
            number_of_xmas += count_xmas(XMAS_TABLE, x, y)
            number_of_mas_cross += count_cross_mas(XMAS_TABLE, x, y)
    print("Part 1: %d" % number_of_xmas)
    print("Part 2: %d" % number_of_mas_cross)
    

