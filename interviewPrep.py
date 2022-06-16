def search(num, arr):
    index = 0
    for i in range(len(arr)):
        if (num==arr[i]):
            return True, index
        index+=1
    return False

def bSearch(num, arr):
    max = len(arr)-1
    min = 0
    while (min<=max):
        cur = (min+max)//2
        if (arr[cur]==num):
            return True,cur
        elif (arr[cur]>num):
            max=cur-1
        elif (arr[cur]<num):
            min=cur+1
    return False

def isSorted(arr):
    prev = arr[0]
    for i in range(1,len(arr)):
        if (prev>arr[i]):
            return False
        prev = arr[i]
    return True

def ssort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1,len(arr)):
            if (arr[j]<arr[min_i]):
                min_i = j
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp
        print(arr) # Only to visualize
    return(arr)

def isort(arr):
    for i in range(1,len(arr)):
        j = i
        while (j>0 and arr[j-1]>arr[j]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
            print(arr) # Only to visualize
    return(arr)

def fib(n):
    if (n<=1):
        return n
    return fib(n-1) + fib(n-2)

def fibFast(n):
    if (n<=1):
        return n
    fib = 1
    fibPrev = 1
    for i in range(2,n):
        temp = fib
        fib += fibPrev
        fibPrev = temp
    return fib

# for i in range(10000):
#     print(fibFast(i))

print("")
# arr = [5,3,9,4,1,6,10,2]
# print("Selection Sort!")
# print(arr)
# ssort(arr)
# print(arr)
# print("")
# arr = [5,3,9,4,1,6,10,2]
# print("Insertion Sort!")
# print(arr)
# isort(arr)
# print(arr)
print("")
