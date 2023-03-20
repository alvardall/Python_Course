
'''
1. Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.
Can you help her?
Examples
"Matt" ➞ "Hello, Matt!"
"Helen" ➞ "Hello, Helen!"
"Mubashir" ➞ "Hello, my Love!"
'''

x = input('Enter your name:')

print(((x == "Mubashir") * "Hello,  my love!") + ((not (x == "Mubashir")) * ("Hello, " + x + "!")))
 
'''
 2.Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.
Examples
a,b = 9, 10 ➞ True
a,b = 9, 9 ➞ False
a,b = 1, 9 ➞ True
'''

a, b = 5, 5

x = ((a == 10 or b == 10) * 'True' + ((a + b) == 10) * 'True') 

print(x + (not (x)) * 'Folse') 

'''
3. Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
Examples
5 ➞ True
-55 ➞ True
37 ➞ False
'''

text_number = input('Enter number')
x = int(text_number) 
print(x % 5 == 0)


