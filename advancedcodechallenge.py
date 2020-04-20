def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False


print("Number in Range Function")
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


print("Same Name Function")
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False


def always_false(num):
    if num > 5 and num < 5:
        return False
    return False


print("Always False Function")
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif 5 <= rating < 9:
        return "This one was fun."
    elif rating >= 9:
        return "Outstanding!"


print("Movie Review Function")
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."


def max_num(num1, num2, num3):
    if num1 > num2:
        if num1 == num3:
            return "It's a tie!"
        elif num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 == num3 or num2 == num1:
            return "It's a tie!"
        elif num2 > num3:
            return num2
        else:
            return num3


print("Find Max Number function")
print(max_num(5, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
