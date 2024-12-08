import sys
sys.path.append('..')
from resource import December1
from resource import December2


#1 December Part 1
def calculate_total_difference():
    list1 = December1.get_number_list1()
    list2 = December1.get_number_list2()
    
    # Sort both lists independently
    list1.sort()
    list2.sort()
    
    # Calculate difference between corresponding elements
    totalDifference = 0
    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        totalDifference += diff
    return totalDifference

#1 December Part 2
def find_matching_sum():
    list1 = December1.get_number_list1()
    list2 = December1.get_number_list2()
    sumOfAppearance = 0
    for x in list1:
        for i in range(len(list2)):
            if x == list2[i]:
                sumOfAppearance += x
    return sumOfAppearance

print(calculate_total_difference())
print(find_matching_sum())


#2 December part 1

def find_number_of_safe_reports():
    reports  = December2.format_data()
    maxScoreChange = 3
    minScoreChange = 1
    totalSafeReports = 0

    for scores in reports:

        is_increasing = all(scores[i] < scores[i+1] for i in range(len(scores) - 1))
        is_decreasing = all(scores[i] > scores[i+1] for i in range(len(scores) - 1))

        # Check if adjacent levels differ by at least 1 and at most 3
        is_difference_valid = all(minScoreChange <= abs(scores[i]- scores[i+1]) <= maxScoreChange for i in range(len(scores) - 1))
        if (is_increasing or is_decreasing) and is_difference_valid:
            totalSafeReports += 1
    
    return totalSafeReports

print(find_number_of_safe_reports())