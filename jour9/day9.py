import sys

def checksum(disk):
    chksum = 0
    for i in range(len(disk)):
        if(disk[i]!="."):
            chksum += i*disk[i]
    return chksum

def find_last_file(disk):
    for i in range(len(disk)):
        if(disk[-1-i]!="."):
            return -1-i

def is_defrag(disk):
    is_int = True
    for x in range(len(disk)):
        if(is_int and disk[x]!="."):
            is_int = True
        elif(is_int and disk[x]=="."):
            is_int = False
        elif(not is_int and disk[x]!="."):
            return False
    return True

def get_free_space(disk, x):
    space = 0
    while(x+space<len(disk) and disk[x+space]=="."):
        space+=1

    return space

def get_last_file_from_id(disk, file_id):
    x = len(disk)-1
    while x>=0:
        if(disk[x]==file_id):
            file_size = 0
            while(disk[x-file_size]==file_id):
                file_size += 1


            return x-file_size,file_size
        x-=1
    return -1,-1

if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')
    disk_representation = input_file.readline().strip()
    disk = []
    file_id = 0
    print("Generating disk")
    for x in range(0, len(disk_representation)):
        if(not x%2):
            for i in range(int(disk_representation[x])):
                disk.append(file_id)
        else: 
            for i in range(int(disk_representation[x])):
                disk.append(".")
            file_id+=1
    
    disk_orig = disk.copy()

    print("Defrag disk bad algo")
    """for x in range(len(disk)):
        if(x%1000==0):
            print("Defrag %d/%d" % (x, len(disk)), end="\r")
        if(disk[x] == "."):
            last_file_pos = find_last_file(disk)
            disk[x], disk[last_file_pos] = disk[last_file_pos], disk[x]
        if(is_defrag(disk)):
            break

    print("Part 1: %d" % checksum(disk))"""

    print("Real Defrag")
    disk = disk_orig.copy()
    file_id = disk[-1]
    while file_id>=0:
        print("Defrag %d" % (file_id), end="\r")
        x = 0
        while x < len(disk):
            if(disk[x]=="."):
                space = get_free_space(disk, x)
                last_file_position, file_size = get_last_file_from_id(disk, file_id)
                if(last_file_position>=0 and file_size<=space and last_file_position>=x):
                    print("Move  %d" % (file_id), end="\r")
                    for i in range(file_size):
                        disk[x+i], disk[last_file_position+1+i] = disk[last_file_position+1+i], disk[x+i]
                    file_id -= 1
                    print("Defrag %d" % (file_id), end="\r")
            
            x+=1
        file_id += -1

    print("Part 2: %d" % checksum(disk))