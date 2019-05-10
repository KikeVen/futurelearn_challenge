#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description: Custom algorithm: "produce aisle"
        function takes a single type list, and returns a sorted list
        from min to max. with `list_float` it performs in 4.5 to 5 seconds
        compared to bubble algorithm which performs in 12 to 14 seconds
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""
import timeit

# ----------------------------- sample data ----------------------------- #

list_float = [3388.16, 3369.15, 3339.89, 3284.94, 3232.45, 3183.02, 3303.95,
              3389.11, 3401.45, 3298.21, 3528.76, 3753.34, 3594.35, 3805.21,
              3655.81, 3602.21, 3647.28, 5087.34, 5009.63, 5015.26, 5139.24,
              5262.07, 5350.22, 5494.85, 5129.30, 5814.15]
list_int = [4, 7, 9, 12, 2, 6, 1, 5, 8, 10, 0]
list_boo = [True, False]
list_str = ["bread", "cheese", "apple", "tomato", "biscuits"]
list_mix = ["cheese", False, 0, 5814.15]  # will give an error


# ----------------------------- sort function ----------------------------- #

def mm_sorter():  # ist_name
    """It takes a list, float, int or string and sorts them out from min to max
    Arguments:
        list_name {int, boo, float, string} -- list to be sorted
    Returns:
        int, boo, float, string -- a copy of the original list sorted from min to max
    """
    # list_copy = list_name[:]
    list_name = list_float
    sorted_list = []
    minc = 0
    maxc = -1
    list_range = len(list_name)

    for item in range(list_range):
        sorted_list.append('-')

    sort_range = int(list_range/2)
    if list_range % 2 != 0:
        sort_range += 1

    for item in range(sort_range):
        if not list_name:
            pass
        else:
            sorted_list[minc] = min(list_name)
            list_name.remove(min(list_name))
            minc += 1
        if not list_name:
            pass
        else:
            sorted_list[maxc] = max(list_name)
            list_name.remove(max(list_name))
            maxc += -1
    return sorted_list

# ----------------------------- function call ----------------------------- #


if __name__ == "__main__":

    print(mm_sorter())
    time_it = timeit.timeit(mm_sorter)
    print('Time it took to run: ', time_it)


# ----------------------------- Visual algorithm ----------------------------- #

""" Visual algorithm

master list:
          v   v
| 4 | 7 | 1 | 9 | 2 | 6 | 5 | 8 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
         min max

sorted list:
| 1 | - | - | - | - | - | - | 9 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
 min                         max

master list:
          v          v
| 4 | 7 | 2 | 6 | 5 | 8 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 6 |
         min         max

sorted list:
| 1 | 2 | - | - | - | - | 8 | 9 |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
     min                 max
"""
