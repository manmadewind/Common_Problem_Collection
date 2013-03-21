'''
输入一个字符串，输出它的全排列。
例如：输入"abc"
输出：
"abc", "acb", "bac", "bca", "cab", "cba"
'''

def findAllSequence(pre, array):
    if len(array) == 0:
        print (pre)
        return

    for i in range(0, len(array)):        
        findAllSequence(pre + str(array[i]), array[:i] + array[i + 1:])    
                  
        

