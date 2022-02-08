#code.py
import random
import timeit
from lab4 import *
from sorts import *
import math
from openpyxl import Workbook

#reused code from last assignment
def sortFunctionTimeTest(function,listt):
    start = timeit.default_timer()
    listt = function(listt)
    end = timeit.default_timer()
    return end - start

#mergesort vs factor
#factor between 0 and 0.5

#column A is average case performance, coulmn B is worst case performance and column C is n
def worstCase():
    bestMergesort = mergesort #replace if another mergesort runs better than the standard
    
    num = 1
    workbook = Workbook()
    sheet = workbook.active
    factor = 0
    
    # headers
    sheet["A1"] = "Factor"
    sheet["B1"] = "Mergesort Runtime"
    
    factor = 0
    times = 2
    listLength = 100
    while factor <= 0.5:         
        spot = str("B" + str(times))
        runTime = sortFunctionTimeTest(bestMergesort,create_near_sorted_list(listLength, factor))
        sheet[spot] = runTime        

        spot = str("A" + str(times))   
        sheet[spot] = factor    
        factor += 0.1    
        times += 1
        
    workbook.save(filename="Lab 4 Worst Case.xlsx")  

# Test Test
worstCase()