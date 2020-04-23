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
