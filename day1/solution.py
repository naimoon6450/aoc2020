import csv
import sys

TARGET_SUM = 2020
# TARGET_SUM = 18


with open(sys.argv[1]) as input_file:
    csv_reader = csv.reader(input_file)
    # Part 1
    # temp = {}
    # for row in csv_reader:
    #     temp[row[0]] = TARGET_SUM - int(row[0])
    
    # pairs = []
    # for key in temp:
    #     if temp.get(str(temp[key])):
    #         pairs.append([int(key), temp[key]])
    #         break

    # print(pairs[0][0] * pairs[0][1])

    # Part 2
    nums = []
    for row in csv_reader:
        nums.append(int(row[0]))
    
    # sort list to find 3rd number easily
    nums_sort = sorted(nums)
    # nums_sort = [2,3,4,5,8,9]
    
    #initialize vars... find scenario where left + right + curr soln = 2020
    curr_soln, left, right =0, 0, len(nums_sort)-1

    # you want to loop through each value up to len-2 as a potential solution
    for i in range(len(nums_sort)-2):
        bools = False
        left = i + 1
        right = len(nums_sort) - 1
        curr_sum = nums_sort[i] + nums_sort[left] + nums_sort[right]
        if curr_sum == TARGET_SUM:
            curr_soln = i
            break
        
        if curr_sum < TARGET_SUM or curr_sum > TARGET_SUM:
            # reset right
            right = len(nums_sort) - 1
            while left < right:
                new_sum = nums_sort[i] + nums_sort[left] + nums_sort[right]
                if new_sum < TARGET_SUM:
                    left += 1
                elif new_sum > TARGET_SUM:
                    right -= 1
                else:
                    curr_soln = i
                    bools = True
                    break
            
        if bools:
            break

    print(nums_sort[left], nums_sort[right], nums_sort[curr_soln])
    print(nums_sort[left]* nums_sort[right]* nums_sort[curr_soln])

            



