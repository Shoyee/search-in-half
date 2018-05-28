#!/usr/bin/env python3
#coding:utf-8
#在升序列表中查找元素，封装成方法
def search_ele(lst0,key):
    #lst0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #key = int(input("请输入要找的数："))
    min_index = 0
    max_index = len(lst0) - 1
    mid_index = (min_index + max_index) // 2
    '''while lst0[mid_index] != key:
        if lst0[mid_index] > key:
            max_index -= 1
        elif lst0[mid_index] < key:
            min_index += 1
        if min_index > max_index:
            print("在列表lst0中未找到",key)
            break
        else:
            mid_index = (min_index + max_index) // 2
    else:
        print("在列表lst0中找到了",key,"，其索引位置为：",mid_index)
        break
        '''

    while min_index <= max_index:
        if lst0[mid_index] > key:
            max_index -= 1
        elif lst0[mid_index] < key:
            min_index += 1
        else:
            return mid_index
            #print("在列表lst0中找到了", key, "，其索引位置为：", mid_index)
        mid_index = (min_index + max_index) // 2
    else:
        return -1
        #print("在列表lst0中未找到", key)
lst0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lst1 = [5,6,9,12,753,852,1465,9543]
print(search_ele(lst0,18))
print(search_ele(lst0,8))
print(search_ele(lst0,0))
print(search_ele(lst0,4))
print(search_ele(lst1,34))
print(search_ele(lst1,753))
