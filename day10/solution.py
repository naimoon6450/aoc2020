import csv
import sys



with open(sys.argv[1]) as input_file:
    csv_reader = csv.reader(input_file)

    adapters = []
    for row in csv_reader:
        # adapters.append[int(row[0])]
        adapters.append(int(row[0]))
    
        
    
    device_joltage = max(adapters) + 3
    adapters.append(0)
    adapters.append(device_joltage)
    sorted_adapters = sorted(adapters)
    
    
    pt = 0
    prev = -1
    sorted_groups = []
    one_jolts = []
    three_jolts = []
    while pt < len(sorted_adapters):
        # calculate delta
        delta = sorted_adapters[pt] - sorted_adapters[prev]
        # check difference of first element to init
        # seems like delta will always be <= 3
        if delta <= 3:
            if delta == 1:
                one_jolts.append(True)
            elif delta == 3:
                three_jolts.append(True)
            pt += 1
        
        # move prev up 
        prev += 1



    # print(len(one_jolts) * len(three_jolts))
    print(sorted_adapters)
    dp = [0] * (device_joltage + 1)
    dp[0] = 1 # 1 way to get to 0
    # dp[i] is the number of ways to get to the ith adapter

    for adapter in sorted_adapters:
        if adapter == 0:
            continue
        dp[adapter] = dp[adapter-1] + dp[adapter-2] + dp[adapter-3]




    print(dp)
    # dict_j = {}
    # dict_j[0] = 1
    # for adapter in sorted_adapters:
    #     for i in range(1, 4):
    #         possible_adapter = adapter + i
    #         if possible_adapter in sorted_adapters:
    #             if dict_j.get(possible_adapter):
    #                 dict_j[possible_adapter] += dict_j[adapter]
    #             else:
    #                 dict_j[possible_adapter] = dict_j[adapter]
    # print(dict_j[device_joltage])



    # print('combos', dp)

