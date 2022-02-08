from lab4 import *
import random

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