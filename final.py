import time
import random

def generate_random_array(N, MAX):
    return [random.randint(1, MAX) for _ in range(N)]

class Sorting:
    def BubbleSort(array):
        n = len(array)

        for i in range(n):
            already_sorted = True

            for j in range( n-i-1):
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1], array[j]
                    already_sorted = False

            if already_sorted:
                break
        return array
    
    def CountSort(array):
        max_val = max(array)
        min_val = min(array)

        count = [0]*(max_val - min_val + 1)

        for num in array:
            count[num- min_val] += 1
        sorted_arr = []

        for i in range(len(count)):
            sorted_arr.extend([i + min_val] * count[i])

        return sorted_arr
    
    def mergeSort(myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            Sorting.mergeSort(left)
            Sorting.mergeSort(right)

            i = 0
            j = 0
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    myList[k] = left[i]
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1

            return myList
        
    def partition(array, low, high): 
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1               
                (array[i], array[j]) = (array[j], array[i])
    
        (array[i+1], array[high]) = (array[high], array[i+1])
        return i + 1
 
    def quickSort(array, low, high):
        if low < high:
            pi = Sorting.partition(array, low, high)
    
            Sorting.quickSort(array, low, pi - 1)
            Sorting.quickSort(array, pi + 1, high)
        return array
    
    def verificare_sortare(func):
        for i in range(len(func)-1):
            if func[i] > func[i+1]:
                return False
        return True

lines = []
f = open("c:\\Users\\alexm\\Downloads\\input.txt", "r")
T = int(f.readline().strip())
for line in f:
    line = line.strip()
    if line:
        pairs = [int(num) for num in line.split(',') if num.strip()]
        lines.append(pairs)
f.close()

for line in lines:
    print("Line:", line)
    print("N:", line[0], "MAX:", line[1])
    N, MAX = line[0], line[1]
    for i in range(T):
        print("T:", i+1)
        given_array = generate_random_array(N, MAX)


        ### BUBBLE SORT
        start_time1 = time.time()
        bubble_sort = Sorting.BubbleSort(given_array.copy())
        end_time1 = time.time()

        if Sorting.verificare_sortare(bubble_sort) != True:
            print("Eroare de ordonare la utilizarea BUBBLE SORT")
        else: 
            pass

        print("BUBBLE SORT: ", "\nTIME: " ,end_time1-start_time1)


        ### COUNT SORT
        start_time2 = time.time()
        count_sort = Sorting.CountSort(given_array)
        end_time2 = time.time()

        if Sorting.verificare_sortare(count_sort) != True:
            print("Eroare de ordonare la utilizarea COUNT SORT")
        else: 
            pass

        print("COUNT SORT: ","\nTIME: " ,end_time2-start_time2)

        ### MERGE SORT
        start_time3 = time.time()
        merge_sort = Sorting.mergeSort(given_array.copy())
        end_time3 = time.time()

        if Sorting.verificare_sortare(merge_sort) != True:
            print("Eroare de ordonare la utilizarea MERGE SORT")
        else: 
            pass
        print("MERGE SORT: ", "\nTIME: " ,end_time3-start_time3)


        ### QUICK SORT
        x = len(given_array)
        start_time4 = time.time()
        quick_sort = Sorting.quickSort(given_array,0,x-1)
        end_time4 = time.time()

        if Sorting.verificare_sortare(quick_sort) != True:
            print("Eroare de ordonare la utilizarea QUICK SORT")
        else: 
            pass

        print("QUICK SORT: ","\nTIME: " ,end_time4-start_time4)
        print("--------------------------------")

        print()
    print()
