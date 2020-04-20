def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


print("Large Power Function")
print(large_power(2, 13))
# should print True
print(large_power(2, 12))


# should print False


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False


print("Over Budget Function")
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))


# should print True


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


print("Twice as Large Function")
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))


# should print True


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print("Divisible by Ten Function")
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))


# should print False


def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False


print("Not Equal to Ten Function")
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5, 5))
# should print False
