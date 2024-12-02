import sys

def is_safe(report_orig, tolerance=0, del_index=-1):
    report = report_orig.copy()
    
    if(tolerance<0):
        return False

    if(del_index>=0):
        del report[del_index]
        return(is_safe(report, tolerance))
    
    increase = report[1] > report[0]

    safe = True
    for i in range(len(report)-1):
        if(report[i+1] == report[i]):
            safe = False
            break
        
        if(increase != (report[i+1] > report[i])):
           safe = False
           break
        
        if(abs(report[i+1]-report[i])>3):
            safe = False
            break
           
    if(not safe):
        return is_safe(report, tolerance-1, i) or is_safe(report, tolerance-1, i+1) or is_safe(report, tolerance-1, 0)
    
    return True


if __name__ == "__main__":
    ## READ FILE
    input_file = open(sys.argv[1])
    safe_reports = 0
    safe_reports_tolerant = 0
    for line in input_file.readlines():
        line_clean = [int(i) for i in line.split()]
        if(is_safe(line_clean)):
            safe_reports += 1

        if(is_safe(line_clean, 1)):
            safe_reports_tolerant += 1
    print("Part 1: %d" % safe_reports)
    print("Part 2: %d" % safe_reports_tolerant)