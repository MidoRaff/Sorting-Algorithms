import matplotlib.pyplot as plt
import numpy as np
import random

amt = int(input('Enter a random integer greater than 10: '))

if amt <= 10:
    amt = 15

sort = int(input('''Enter
\t 1 for Insertion Sort
\t 2 for Merge Sort
'''))


def InsertionSort(amt):
    lst = np.random.randint(0, 100, amt)
    x = np.arange(0, amt, 1)

    n=len(lst)
    # INSERTION SORT

    for k in range(1, n):
        key = lst[k]
        l = k-1
        while l>=0 and key < lst[l]:
            lst[l+1] = lst[l]
            l = l-1
            plt.bar(x,lst)
            plt.pause(0.001)
            plt.clf()
        else:
            lst[l+1] = key

    plt.show()


def MergeSort(amt):
    num =  [random.randint(0, 1000) for _ in range(amt)]

    def merge_sort(lst, left, right):

        if left >= right:
            return

        mid = (left + right)//2
    
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()

        merge_sort(lst, left, mid)
        merge_sort(lst, mid+1, right)
    
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()

        merge(lst, left, right, mid)
        plt.bar(list(range(amt)), lst)
        plt.pause(0.001)
        plt.clf()


    def merge(lst, left, right, mid):

        l_cy = lst[left:mid+1]
        r_cy = lst[mid+1:right+1]

        l_cou = r_cou = 0

        count = left
    
        while l_cou < (len(l_cy)) and r_cou < (len(r_cy)):
            if l_cy[l_cou] <= r_cy[r_cou]:
                lst[count] = l_cy[l_cou]
                l_cou += 1
            else:
                lst[count] = r_cy[r_cou]
                r_cou += 1

            count += 1

        while l_cou < (len(l_cy)):
            lst[count] = l_cy[l_cou]
            l_cou += 1
            count += 1
    
        while l_cou < (len(r_cy)):
            lst[count] = r_cy[r_cou]
            r_cou += 1
            count += 1



    merge_sort(num, 0, len(num)-1)
    plt.bar(list(range(amt)), num)
    plt.show()



if sort == 1:
    InsertionSort(amt)
elif sort == 2:
    MergeSort(amt)