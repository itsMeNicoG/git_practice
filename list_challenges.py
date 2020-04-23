# takes list and appends the sum of the last two items three times
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))


# return last element of list with more elements or list1 if both have the same amount
def larger_list(lst1, lst2):
    if len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]


print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# check if an item appears more than n times in a list
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# appends size of list to it
def append_size(lst):
    lst.append(len(lst))
    return lst


print(append_size([1, 2, 3, 2]))


# zip two lists and sort result
def combine_sort(lst1, lst2):
    combined_list = list(zip(lst1, lst2))
    return sorted(combined_list)


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

