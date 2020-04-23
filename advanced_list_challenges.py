# creates and returns a list from start to 100 including this, and jumps every three numbers
def every_three_nums(start):
    three_list = range(start, 101, 3)
    return list(three_list)


print(every_three_nums(3))


# remove every element between start and end
def remove_middle(lst, start, end):
    del lst[start:end+1]
    return lst


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# returns the item that appears more times in lst, if they appear the same amount of times, returns item1
def more_frequent_item(lst, item1, item2):
    if lst.count(item2) > lst.count(item1):
        return item2
    else:
        return item1


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# doubles element at index and returns modified list, if index is out of bounds, return original list
def double_index(lst, index):
    if index > len(lst)-1:
        return lst
    else:
        new_list = lst
        new_list[index] = lst[index] * 2
        return new_list


print(double_index([3, 8, -10, 12], 2))


# if list has an odd size, return middle element, otherwise return average of two middle elements
def middle_element(lst):
    if len(lst) % 2 != 0:
        return lst[len(lst)//2]
    else:
        sum = lst[len(lst)//2-1] + lst[len(lst)//2]
        return sum//2


print(middle_element([5, 2, -10, -4, 4, 5]))