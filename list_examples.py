names = ['Nico', 'Snoop', 'Uncle Snoop']
ages = [21, 56, 57]
joined_list = zip(names, ages)
# If we don't add list inside the print, it will print it's memory location
print(list(joined_list))

names.append('Kathe')
ages.append(26)
names += ['Mateo']
ages += [10]

joined_list = zip(names, ages)
print(list(joined_list))

# show first 100 numbers divisible by the specified number
# range(x) will create list from 0 to x -1
# range(x,y) will create list from x to y-1
# range(x,y,z) will create list from x to y but adding z units each time


def show_divisible_by(number):
    multiple_list = range(number, (number*(100+1)), number)
    print(list(multiple_list))


show_divisible_by(3)
