# -*- coding: utf-8 -*-

'''
Q:一数组，要求求出所有这样的数a[i]——其左边的数都小于等于它，右边的数都大于等于它。
只用一个额外数组和少量其他空间实现

例子： 有数组 [4, 3, 6, 1, 2, 4, 9, 10]，则依题意元素9和10即为所求。


我的解法:
时间复杂度：O(n)
算法思路如下：
(1).先从左到右进行一次扫描，当找到比当前左侧的所有元素都大的元素时，记录下当前元素（在结果数组中做个标记）。
(2).再从右到左进行一次扫描，当找到比当前右侧的所有元素都小的元素时，记录下当前元素（在结果数组中做个标记）。
(3).取(1)(2)两个结果集中的交集即为所求。
'''

def findRightPosition(array):
    results = []

    # Step1. from left to right
    leftMax = array[0]
    for i in range(0, len(array)): # i in [ 0, len(array) )
        if array[i] >= leftMax: # 此元素为目前最大   
            leftMax = array[i]
            results.append(1) # 在结果数组中将该元素标记为1
        else:
            results.append(0) # 在结果数组中将其标记为0

    print results
    
    # Step2. from right to left
    rightMin = array[-1]
    for i in range(len(array) - 1, 0, -1):    
        if array[i] <= rightMin: # 此元素为目前最小
            rightMin = array[i] 
            results[i] += 1 # 在结果数组中做标记

    # Step3. output results
    for i in range(0, len(array)):
        if results[i] == 2: # 既是比左边都大又是右边都小
            print 'result:' + str(array[i])
