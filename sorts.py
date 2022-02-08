from lab4 import *
import random

def mergesort_three(L): #Still needs thorough testing
    
    if len(L) <= 1:
        return 
    mid1 = len(L)//3
    mid2 = (2 * len(L))//3
    left, middle, right = L[:mid1], L[mid1:mid2], L[mid2:]

    #Mergesort core
    mergesort_three(left)
    mergesort_three(middle)
    mergesort_three(right)
    temp = merge_three(left, middle, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, middle, right):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right):
        #if left done
        if i >= len(left):
            if j >= len(middle):
                L.append(right[k])
                k += 1
            elif k >= len(right):
                L.append(middle[j])
                j += 1
            else:
                if middle[j] <= right[k]:
                    L.append(middle[j])
                    j += 1
                else:
                    L.append(right[k])
                    k += 1
        #if middle done
        if j >= len(middle):
            if i >= len(left):
                L.append(right[k])
                k += 1
            elif k >= len(right):
                L.append(left[i])
                i += 1
            else:
                if left[i] <= right[k]:
                    L.append(left[i])
                    i += 1
                else:
                    L.append(right[k])
                    k += 1
        #if right done
        if k >= len(right):
            if j >= len(middle):
                L.append(left[i])
                i += 1
            elif i >= len(left):
                L.append(middle[j])
                j += 1
            else:
                if middle[j] <= left[i]:
                    L.append(middle[j])
                    j += 1
                else:
                    L.append(right[i])
                    i += 1
        #if none done
        else: #sort
            if left[i] <= middle[j] and left[i] <= right[k]:
                L.append(left[i])
                i += 1
            elif middle[j] <= left[i] and middle[j] <= right[k]:
                L.append(middle[j])
                j += 1
            else:
                L.append(right[k])
                k += 1
    return L


def merge_bottom(L,start,mid,end):
    sOne = start
    sTwo = start
    mPlus = mid + 1
    temp = L.copy() #turns out you have to copy the list and can't just use it. This is the error that delayed pushing for so long!!!
    
    while sTwo <= mid and mPlus <= end:
        if L[sTwo] < L[mPlus]:
            temp[sOne] = L[sTwo]
            sTwo = sTwo + 1
        else:
            temp[sOne] = L[mPlus]
            mPlus = mPlus + 1

        sOne = sOne + 1

    while sTwo < len(L) and sTwo <= mid:
        temp[sOne] = L[sTwo]
        sOne = sOne + 1
        sTwo = sTwo + 1

    for i in range(start, end + 1):
        L[i] = temp[i]


def mergesort_bottom(L):
    l = 0
    h = len(L) - 1
    m = 1
    while m <= h - l:
        for i in range(l, h, 2*m):
            start = i
            mid = i + m - 1
            end = min(i + 2*m - 1, h)
            merge_bottom(L, start, mid, end)
        m = 2*m

# Main stuff tests

L = create_random_list(random.randint(3,10))
print("Unsorted:", L)
mergesort_bottom(L)
print("Sorted:", L)
