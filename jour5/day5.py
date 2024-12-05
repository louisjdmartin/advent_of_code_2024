import sys


def check_report(rules, report):
	# The idea is to check if a page is not breaking a rule
	# If for a given page, there is a rule thats forbid this page in previous seen pages, order is wrong
	already_seen = []
	for page in report:
		if(page in rules.keys()):
			forbidden_pages = rules[page]
			for forbidden in forbidden_pages:
				if(forbidden in already_seen):
					# If order is wrong, we invert false pages
					report[report.index(page)], report[report.index(forbidden)] = forbidden, page
					return False
		already_seen.append(page)
	return True


if __name__ == "__main__":
	file_input = open(sys.argv[1], 'r')
	lines_input = file_input.readlines()


	i=0
	rules = dict()
	# We try to get all rules and regroup item in dict for easier reading later
	while lines_input[i] != "\n":
		rule = lines_input[i].strip().split("|")
		if(rule[0] not in rules.keys()):
			rules[rule[0]] = [rule[1]]
		else:
			rules[rule[0]].append(rule[1])
		i+=1

	i += 1
	sum_part1 = 0
	sum_part2 = 0
	# We read all print reports
	while i < len(lines_input):
		report = lines_input[i].strip().split(",")

		if(check_report(rules, report)):
			# PART 1 if report is ok, we add middle element
			sum_part1 += int(report[len(report)//2])
		else:
			# PART 2: as check report reorder failed item, we check while report is false
			while(not check_report(rules, report)):
				pass
			sum_part2 += int(report[len(report)//2])

		i+=1
	
	print("Part 1: %d" % sum_part1)
	print("Part 2: %d" % sum_part2)
