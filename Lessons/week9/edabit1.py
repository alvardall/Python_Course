
# 1 string medium



def int_to_str(i):
    return str(i)


print(int_to_str(29348))


def str_to_int(s):
    return int(s)


print(str_to_int('4'))

# 2


def string_int(txt):
    return int(txt)


print(string_int("1000"))
# 3


def how_many_seconds(hours):
    seconds = hours * 3600
    return seconds


print(how_many_seconds(24))

# 4 string medium


def next_edge(side1, side2):
    edge = (side1 + side2) - 1
    return edge


print(next_edge(8, 10))

# 1 string hard


def arithmetic_operation(equation):
    first_num, operation, second_num = equation.split()
    if operation == '+':
        return str(first_num) + str(second_num)
    if operation == '-':
        return int(first_num) - int(second_num)
    if operation == '*':
        return str(first_num) * str(second_num)
    if operation == '//' and second_num == '0':
        return -1
    return str(first_num) // str(second_num)

print(arithmetic_operation("23 - 21"))

#2 string medium
def find_it(items, name):
    if name in items:
        return name.capitalize() + ' is gone...'
         
    return name.capitalize() + ' is here!'
print(find_it({
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
}, "timmy"))

#3 string medium
'''Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"
area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"
area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"
Notes
    The total world's landmass is 148,940,000 [Km^2]
    Round the result to two decimal places.
    If you get stuck on a challenge, find help in the Resources tab.'''

def area_of_country(name, area):
   
    return name + " is " + str((area * 100 // 148940000 )) +'%' + " of the total world's landmass"

print(area_of_country("Russia", 17098242))




