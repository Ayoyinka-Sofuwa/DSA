import fire

def insert_sort(A, n):
    sorted_arr = []
    for i in range(1, n):
        key = A[i]
        #insert A[i] into the sorted sub-array A[1:i-1]
        j = i-1
        while j>0 and A[j]>key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    
    for item in range(len(A)):
        sorted_arr.append(A[item])
    return sorted_arr

    


def main(arr:list): 
    len_arr = len(arr)
    return insert_sort(arr, len_arr)


if __name__ == "__main__": 
    fire.Fire(main)
