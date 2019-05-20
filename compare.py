from timeit import timeit
from random import randint
import minmax_sort as mms
import bubble as bbs

##################################################################
# COPY AND PASTE YOUR bubble_sort AND merge_sort functions below #
##################################################################

# Generate a large (1000 items) random list
list_to_sort = [randint(0, 100000) for i in range(1000)]
my_float = mms.list_float

# Create anonymous functions to use with timeit,
# be sure to check these function names match your pasted ones


# def bs(): return bbs.sorter(list_to_sort)
# def ms(): return mms.mm_sorter(list_to_sort)

bs = lambda: bbs.sorter(list_to_sort)
ms = lambda: mms.mm_sorter(list_to_sort)
ts = lambda: sorted(list_to_sort)

# time the functions for 100 runs each
print("For a run of 1000 each\n")
print("My lamemo algo took:")
print(timeit(ms, number=1000))

print("Bubble took:")
print(timeit(bs, number=1000))

print("Timsort took:")
print(timeit(ts, number=1000))
