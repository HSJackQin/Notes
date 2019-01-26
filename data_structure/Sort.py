
# Bubble Sort
def BubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for j in range(passnum):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
BubbleSort(alist)

# Short Bubble Sort
def ShortBubbleSort(alist):
    num = len(alist)-1
    stop = False
    while num > 0 and not stop:
        stop = True
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                stop = False
        num -= 1
    return alist

alist = [54,26,93,17,77,31,44,55,20]
ShortBubbleSort(alist)

# Select Sort
def SelectSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        maxlocate = 0
        for locate in range(1,passnum+1):
            if alist[maxlocate] < alist[locate]:
                maxlocate = locate
        alist[passnum], alist[maxlocate] = alist[maxlocate], alist[passnum]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
SelectSort(alist)
            
# Insert Sort
def InsertSort(alist):
    for position in range(1,len(alist)):
        currentvalue = alist[position]
        index = position
        while index > 0 and alist[index-1] > currentvalue:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = currentvalue
    return alist

alist = [54,26,93,17,77,31,44,55,20]
InsertSort(alist)

# Shell Sort
def ShellSort(alist):
    gap = len(alist)//2
    while gap > 1:
        for start in range(gap):
            Shell(alist, start, gap)
        gap = gap//2
    Shell(alist, 0, 1)
    return alist

def Shell(alist, start, gap):
    for n in range(start+gap,len(alist),gap):
        currentvalue = alist[n]
        index = n
        while index > 0 and alist[index-gap] > currentvalue:
            alist[index] = alist[index-gap]
            index -= gap
        alist[index] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
ShellSort(alist)

# Merge Sort(1)
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        leftpart = alist[:mid]
        rightpart = alist[mid:]

        mergeSort(leftpart)
        mergeSort(rightpart)
        # merge
        i = 0
        j = 0
        k = 0
        while i < len(leftpart) and j < len(rightpart):
            if leftpart[i] < rightpart[j]:
                alist[k] = leftpart[i]
                i += 1
            else:
                alist[k] = rightpart[j]
                j += 1
            k += 1
        while i < len(leftpart):
            alist[k] = leftpart[i]
            i += 1
            k += 1
        while j < len(rightpart):
            alist[k] = rightpart[j]
            j += 1
            k += 1
    
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

# Merge Sort(2)
def MergeSort(alist,first=0,last=8):
    if last - first > 0:
        mid = (last-first+1)//2
        leftstart = first
        leftend = mid - 1
        rightstart = mid
        rightend = last
        
        MergeSort(alist,leftstart,leftend)
        MergeSort(alist,rightstart,rightend)

        # 下一步该合并了
        
# Quick Sort
def QuickSort(alist):
    QuickSortHelper(alist,0,len(alist)-1)

def QuickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        QuickSortHelper(alist,first,splitpoint-1)
        QuickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
QuickSort(alist)
print(alist)