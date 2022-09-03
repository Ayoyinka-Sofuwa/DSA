import fire

def insert_sort(arr:list, n:int):
    sorted_arr = []
    for i in range(1, n):
        key = arr[i]
        j = i-1
	while j>0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
	arr[j+1] = key

    for item in range(len(arr)):
        sorted_arr.append(arr[item])
    return sorted_arr

def main(arr):
    len_arr = len(arr)
    return insert_sort(arr, len_arr)
if __name__ == "__main__":
    fire.Fire(main)	
