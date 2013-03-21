def findAllSequence(pre, array):
    if len(array) == 0:
        print (pre)
        return

    for i in range(0, len(array)):        
        findAllSequence(pre + str(array[i]), array[:i] + array[i + 1:])    
                  
        

