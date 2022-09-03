import numpy as np


def insert_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:

            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key 
    for item in range(len(arr)):
        sorted_arr.append(arr[item])
    return sorted_arr


if __name__ == "__main__":
    array = np.random.rand(1000)
    arr = ['chief', 'ayoyinka', 'titilayo']
    print(insert_sort(arr))
