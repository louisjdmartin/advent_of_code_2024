import sys, re

def mul(a,b):
    return a*b

if __name__ == "__main__":

    ## READ FILE
    input_file = open(sys.argv[1])

    sum_part_1 = 0
    lines = input_file.readlines()
    for data in lines:
        mul_liste = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)    
        for m in mul_liste:
            sum_part_1 += eval(m)
    print("Part 1: %d" % sum_part_1)

    sum_part_2 = 0
    active = True
    for data in lines:
        mul_liste = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))", data)
        for m in mul_liste:
            if(m=="do()"):
                active = True
            elif(m=="don't()"):
                active = False
            elif(active):
                sum_part_2 += eval(m)
    print("Part 2: %d" % sum_part_2)
