import csv
import sys
import copy

def instruction_runner(instructions, visited_ind_map):
    global_acc = 0
    pt = 0
    while pt < len(instructions):
        # if we visited the instruction, break
        if visited_ind_map[pt]: 
            return (global_acc, pt)
        
        # otherwise grab the instruction
        inst = instructions[pt]
        op = inst[0]
        arg = int(inst[1])
        # print(inst)
        # update visited map
        visited_ind_map[pt] = True
        # perform the operation
        if op == 'nop':
            pt += 1
        elif op == 'acc':
            global_acc += arg
            pt += 1
        elif op == 'jmp':
            pt += arg
    
    # if it actually does terminate
    return (global_acc, pt)


with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)


    instructions = []
    visited_ind_map = {}

    ind = 0
    for row in csv_file:
        parsed = row[0].split(' ')
        # instructions.append((parsed[0], parsed[1]))
        instructions.append([parsed[0], parsed[1]])
        visited_ind_map[ind] = False
        ind += 1

    # global_acc = 0

    # pt = 0

    # while pt < len(instructions):
    #     # if we visited the instruction, break
    #     if visited_ind_map[pt]: 
    #         print(global_acc)
    #         break
        
    #     # otherwise grab the instruction
    #     inst = instructions[pt]
    #     op = inst[0]
    #     arg = int(inst[1])
    #     # print(inst)
    #     # update visited map
    #     visited_ind_map[pt] = True
    #     # perform the operation
    #     if op == 'nop':
    #         pt += 1
    #     elif op == 'acc':
    #         global_acc += arg
    #         pt += 1
    #     elif op == 'jmp':
    #         pt += arg

    # Part 2 naive solution
    # go through instructions and try changing each nop to jmp before running while loop to see where you end up?
    for i in range(len(instructions)):
        copy_ins_array = copy.deepcopy(instructions)
        # print(copy_ins_array, i)
        op = copy_ins_array[i][0]
        arg = copy_ins_array[i][1]
        if op == 'nop':
            # change in array
            copy_ins_array[i][0] = 'jmp'
            # run previous loop
            values = instruction_runner(copy_ins_array, dict(visited_ind_map))
            if values[1] == len(copy_ins_array): print(values[0])
        elif op == 'jmp':
            # change in array
            copy_ins_array[i][0] = 'nop'
            # run previous loop
            values = instruction_runner(copy_ins_array, dict(visited_ind_map))
            if values[1] == len(copy_ins_array): print(values[0])
        # print(copy_ins_array, 'after')

        
