'''1. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.'''

def arithmetic_operation(equation):
    first_num, operation, second_num = equation.split()
    if operation == '+':
        return int(first_num) + int(second_num)
    if operation == '-':
        return int(first_num) - int(second_num)
    if operation == '*':
        return int(first_num) * int(second_num)
    if operation == '//' and second_num == '0':
        return -1
    return int(first_num) // int(second_num)
print(arithmetic_operation("23 - 21"))


'''2  A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
Notes
    Position of the digit is 1-indexed.'''

def Disarium(num):
    number = num
    sum = 0
    while(num>0):
        l= len(str(num))
        no = num%10
        sum= sum + no**l   
        l-=1
        num = num//10
    return sum== number
print(Disarium(8))

#3 
'''def check_score(s):
    lst1 = []
    for x in s:
        for a in x:
            if "#" in a:
                lst1+= 5
            if "0" in a:
                lst1+=3
                return lst1
print(check_score([
  ["#", "!"],
  ["!!", "X"]
]))'''
 

'''4 Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.'''

def convert_to_hex(txt):
    return ' '.join(hex(ord(x))[2:] for x in txt)
print(convert_to_hex("Big Boi"))


'''5 Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.'''

def uncensor(txt, vowels):
    for i in range(txt.count('*')):
        txt = txt.replace('*',vowels[i],1)
    return txt
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))


'''6 Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how the text "Go to the challenges!" appears when hovering over the link.'''

def tidy_link(url, name, hover_text):
    return "[{}], ({}, {})".format( name, url, hover_text)
print(tidy_link("https://www.google.com", "Google", "Google Search"))


'''7 Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.'''   
import collections
def pluralize(lst):
    x = set()
    dict = collections.Counter(lst)
    for key in dict:
        if dict[key]>1:
           x.add(key + 's')
        if dict[key]==1:
           x.add(key)
    return x 
          
print(pluralize(["cow", "pig", "cow", "cow"]))

'''8 Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.'''

def censor_string(txt, lst, char):

    word_list = txt.split()
    for censor in lst:
        index = 0
        for word in word_list:
            if censor.lower() == word.lower():
                ch = len(censor) * char
                word_list[index] = ch
            elif censor.lower() == word[0:-1].lower():
                ch = len(censor) * char
                word_list[index] = ch+word[-1]
            index+=1

    return " ".join(word_list)
print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))

'''Generate a random float number'''

import random
def randfloat(start:float, end:float):
    return random.uniform(start, end)
start = 11.5
end = 83.5
print(randfloat(start, end))