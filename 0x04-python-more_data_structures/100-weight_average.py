#!/usr/bin/python3

def weight_average(my_list=[]):
    summation = 0
    divident = 0
    if not my_list:
        return 0
    for i in range(len(my_list)):
        mul = 1
        divident += my_list[i][len(my_list[i])-1]
        for j in my_list[i]:
            mul = mul * j

        summation = summation + mul

    return float(summation/divident)
