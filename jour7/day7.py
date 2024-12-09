import sys, itertools, gc


global cache_subsets
cache_subsets = dict()

def all_subsets(terms, size):
    global cache_subsets
    id_cache = "".join(terms)+str(size)
    permutations = set()
    if(id_cache in cache_subsets):
        return cache_subsets[id_cache]
    
    for t in itertools.combinations_with_replacement(terms, size):
        for p in itertools.permutations(t, size):
            permutations.add(p)
    
    cache_subsets[id_cache] = list(dict.fromkeys(permutations))
    return cache_subsets[id_cache]

def decode_line(line):
    total, equation = line.split(":")
    equations_terms = equation.strip().split(" ")
    return int(total), [int(i) for i in equations_terms]

def solve(numbers, operators):
    total = numbers[0]
    for i in range(len(numbers)-1):
        if(operators[i] == "+"):
            total += numbers[i+1]
        if(operators[i] == "*"):
            total *= numbers[i+1]
        if(operators[i] == "|"):
            total = int(str(total)+str(numbers[i+1]))
    return total

def resolve_eq(total, equation, terms=["*", "+"]):
    all_subs = all_subsets(terms, len(equation)-1)
    for term in all_subs:
        if(total == solve(equation, term)):
            print("OK", end=" ")
            return total
    print("NO", end=" ")
    return 0


if __name__ == "__main__":
    input_file = open(sys.argv[1])
    part_1_sum = 0
    part_2_sum = 0
    
    test = 0
    for line in input_file.readlines():
        total, equation = decode_line(line)
        print("Try to solve", total, equation, end=" ")
        
        part_1_sum += resolve_eq(total, equation)
        part_2_sum += resolve_eq(total, equation, terms=["*", "+", "|"])
        print()

    print("Part 1: %d" % part_1_sum)
    print("Part 2: %d" % part_2_sum)