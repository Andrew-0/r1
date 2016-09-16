import copy
import numpy

class Sort:
    @staticmethod
    def bubble_sort(carr):
        arr = copy.deepcopy(carr)
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


    @staticmethod
    def shaking_sort(carr):
        arr = copy.deepcopy(carr)
        last_swapped_position = 0
        for i in range(len(arr)):
            if i%2 == 0:
                for j in range(last_swapped_position, len(arr)-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        last_swapped_position = j
                print(arr, last_swapped_position)

            else:
                if last_swapped_position == 0:
                    break
                for j in range(last_swapped_position, 0, -1):
                    if arr[j] < arr[j-1]:
                        arr[j], arr[j-1] = arr[j-1], arr[j]
                        last_swapped_position = j - 1
                    print(arr, last_swapped_position)
                    
        return arr



#if __name__ == '__main__':
csort = Sort()
a = [4,3,2,1]
b = csort.shaking_sort(a)
print(a, b)

