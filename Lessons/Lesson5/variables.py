
'''
1. For this challenge, you are supposed to find the sum of the digits of a two-digit number.
45 ➞ 9
38 ➞ 11
67 ➞ 13
'''

x = 38
y = x //10 + x % 10

print(y)



'''Need extra knowledge!!
2. 3.A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not.
44 ➞ True
45 ➞ False
-44 ➞ False
'''

x = 97
y = x // 10 == x % 10

print(y)


'''
3. Write a function that takes an integer minutes and converts it to seconds.
5 ➞ 300
2 ➞ 120
'''

x = 5
y = x * 60
print(y)


'''
4.Create a function that takes the age in years and returns the age in days.
65 ➞ 23725
0 ➞ 0
20 ➞ 7300
'''


x = 65
y = x * 365
print(y)



'''
5.Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200
'''


hours, minutes = 1, 3

seconds = (hours*60) * (60 + minutes)
print(seconds)


'''
6. Create a function that accepts a measurement value in inches and returns the equivalent of the measureme
'''
x =15
y = x * 12
print(y)


'''
7. Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers
'''

x = 5
y = x % 2 

print_text = (y == 0) * "zuyg"  + y * "kent" 
print(print_text)


x = 1960
y = (2023-x)//4

z = ((2023-x)* 365)+ y
print(z)

print(y)

x = 1940
y = 2023 - x

print((y>= 20 and y <= 30) * "vayelir" + (y>= 30 and y <= 40) * "ush e" + (y>= 40 and y <= 90) * "gna heto kgas")


