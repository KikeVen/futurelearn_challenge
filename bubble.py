#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    description:
        Implemented bubble algorithm for comparison to
        custom algorithm, minmax_sort.py
    author: enrique bruzual
    website: https://enriquebruzual.netlify.com/
"""
import timeit

list_int = [4, 7, 9, 12, 2, 6, 1, 5, 8, 10, 0]
list_float = [3388.16, 3369.15, 3339.89, 3284.94, 3232.45, 3183.02, 3303.95,
                3389.11, 3401.45, 3298.21, 3528.76, 3753.34, 3594.35, 3805.21,
                3655.81, 3602.21, 3647.28, 5087.34, 5009.63, 5015.26, 5139.24,
                5262.07, 5350.22, 5494.85, 5129.30, 5814.15]

def sorter():
    """takes a list and sorts from min to max, using
    the 'bubble' algorithm
    """
    list_name = list_float
    changed = True
    while changed:
        changed = False
        for i in range(len(list_name) - 1):
            if list_name[i] > list_name[i+1]:
                list_name[i], list_name[i+1] = list_name[i+1], list_name[i]
                changed = True
    return list_name


if __name__ == "__main__":

    print(sorter())
    time_it = timeit.timeit(sorter)
    print('Time it took to run: ', time_it)
