import sys

if __name__ == "__main__":

    ## READ FILE
    input_file = open(sys.argv[1])
    col1, col2 = [], []
    for line in input_file.readlines():
        c1,c2 = line.split()
        col1.append(int(c1))
        col2.append(int(c2))

    ## SORT LISTS
    col1.sort()
    col2.sort()

    # Answers
    sum = 0
    value = 0
    for i in range(len(col1)):
        sum += abs(col1[i] - col2[i])
        value += col1[i] * col2.count(col1[i])
    print("Part 1: %d" % sum)
    print("Part 2: %d" % value)