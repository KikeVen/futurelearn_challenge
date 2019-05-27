""" Dev Notes:
    Can you alter your code so that it will always return the leftmost
    item when there are multiple identical values? How about the rightmost?

Can you return the index of the closest value, when the actual
value is not found? So in the list [1,2,3,5,6,7], if I searched
for 3.5 then 2 would be returned, because at index 2 the value
is 3 which is closest to 3.5.
    Ref links:
    https://www.futurelearn.com/courses/programming-102-think-like-a-computer-scientist/2/steps/521031#fl-comments
"""
given_list = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]


def binary_search(sorted_list, value):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = int((left + right)/2)
        if sorted_list[mid] > value:
            right = mid - 1
        elif sorted_list[mid] < value:
            left = mid + 1
        else:
            return mid
    return False


print(binary_search(given_list, 4))
