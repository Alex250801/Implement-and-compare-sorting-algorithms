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
        pivot = array[high-1]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1               
                (array[i], array[j]) = (array[j], array[i])
    
        (array[i], array[high-1]) = (array[high-1], array[i])
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


given_array = generate_random_array(1000, 100000)

### BUBBLE SORT
start_time1 = time.time()
bubble_sort = Sorting.BubbleSort(given_array)
end_time1 = time.time()

if Sorting.verificare_sortare(bubble_sort) != True:
    print("Eroare de ordonare la utilizarea BUBBLE SORT")
else: 
    print(True)


### COUNT SORT
start_time2 = time.time()
count_sort = Sorting.CountSort(given_array)
end_time2 = time.time()

if Sorting.verificare_sortare(count_sort) != True:
    print("Eroare de ordonare la utilizarea COUNT SORT")
else: 
    print(True)

### MERGE SORT
start_time3 = time.time()
merge_sort = Sorting.mergeSort(given_array)
end_time3 = time.time()

if Sorting.verificare_sortare(merge_sort) != True:
    print("Eroare de ordonare la utilizarea MERGE SORT")
else: 
    print(True)

### QUICK SORT
start_time4 = time.time()
quick_sort = Sorting.quickSort(given_array,given_array[0],len(given_array))
end_time4 = time.time()

if Sorting.verificare_sortare(quick_sort) != True:
    print("Eroare de ordonare la utilizarea QUICK SORT")
else: 
    print(True)


print("BUBBLE SORT: ", str(bubble_sort), "\nTIME: " ,end_time1-start_time1)
print("COUNT SORT: ", str(count_sort), "\nTIME: " ,end_time2-start_time2)
print("MERGE SORT: ", str(merge_sort), "\nTIME: " ,end_time3-start_time3)
print("QUICK SORT: ", str(quick_sort), "\nTIME: " ,end_time4-start_time4)

# citit din fisier 
