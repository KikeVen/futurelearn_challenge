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

bs = lambda: bbs.sorter(my_float)
ms = lambda: mms.mm_sorter(my_float)

# time the functions for 100 runs each
print("My took:")
print(timeit(ms, number=100))

print("Bubble took:")
print(timeit(bs, number=100))
