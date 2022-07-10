#!/usr/bin/python3

def weight_average(my_list=[]):
    '''Returns the weighted average of all integer tuple'''

    if len(my_list) == 0:
        return 0
    else:
        add = 0
        product = []
        for i in my_list:
            pro = i[0] * i[1]
            product.append(pro)
        for i in product:
            add += i

        add2 = 0
        for j in my_list:
            add2 += j[1]

        return add / add2
