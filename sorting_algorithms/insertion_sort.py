'''
    the insertion sort algorithm
'''
import numpy as np

def insert_sort(item, steps):
    
    for i in range(1, steps):
        key = i
        
        while key>0 and (item[key] < item[key-1]):
            item[key], item[key-1] = item[key-1], item[key]
            key -= 1 
        #sorted_list.append(item)
    return item 



if __name__ == "__main__": 
    arr = np.random.randint(100)
    num = [3,2,4,6,5,7,9,10,8] 
    words = ['chief', 'babe', 'babie'] 
    words2 = ['chief', 'ayoyinka', 'titilayo']
    print(insert_sort(words2, len(words2)))

            


