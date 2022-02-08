def mergesort_three(L):
    
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
        #incomplete. needs to be fixed
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else: #sort. this part is complete
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

