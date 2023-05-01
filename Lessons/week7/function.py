'''1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"
say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
say_hello_bye("jose", 0) ➞ "Bye Jose"'''

def say_hello_bye(a, b ):
    if b == 1:
        return f'Hello {a.capitalize()}'
    elif b == 0:
        return f'Bye {a.capitalize()}'
    else:
        return 'Frong number'
print(say_hello_bye("alon", 1))
print(say_hello_bye("Tomi", 1)) 
print(say_hello_bye("Jose", 0))

'''2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.
Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False'''

def all_same(elements):
     return (elements[:-1] == elements[1:])

test_jackpot = (["SS", "SS", "SS", "Ss"])
print(all_same(test_jackpot))

'''3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them).'''

def hj(arr, h):
  for i in arr:
    if i <= h:
        return  True
    else:
        i > h
        return False 
    
print(hj([5, 5, 3, 4, 5], 3))

'''4. Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. The second example is a factor of 12, because 12 / 2 = 6, with remainder 0.'''

def factorize(n):   
    new_list =[];
    for i in range(1, n + 1):
        if n % i == 0:
            new_list.append(i) 
    return new_list
print (factorize(12))


'''5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers.'''

def count_palindromes(start, end):
    new_list = []
    for num in (range(start, end)):
        if str(num) == str(num)[::-1]:
           new_list.append(num)
        return (new_list)

print(count_palindromes(1, 10))

'''6. Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).'''

def split(string):
    vowels = ['a','e','i','o','u']
    str1= ""
    str2 = ""
    for letter in string:
        if letter.lower()  in vowels:
            str1 += letter
        else:
            str2 += letter
    return (str1 +str2)

print(split("abcde"))
'''7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.'''
'''def hacker_speak(txt):
	dict = {"a":4, "e":3, "i":1, "o":0,"s":5}
	str1 = ""
	for i in list(txt):
        if 
		    str1 += str(dict[i])
        else:
       
		    str1 += i
	return str1
print(hacker_speak("javascript is cool"))'''

'''8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.'''

def ordinal(num):
  
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
    
        suffix = end_of_number.get(num % 10, 'th')
    return str(num) + "-"+ suffix
end_of_number = {1: 'st', 2: 'nd', 3: 'rd'}
print(ordinal(553))

'''9. Create a function that converts Celsius to Fahrenheit and vice versa.
Examples
convert("35*C") ➞ "95*F"
convert("19*F") ➞ "-7*C"
convert("33") ➞ "Error"
Notes
Round to the nearest integer.
If the input is incorrect, return "Error".
For the formulae to convert back and forth, check the Resources tab.'''
temp = "33C"
degree = int(temp[:-1])
convention = temp[-1]

if convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convention = "F"
elif convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  convention = "C"
else:
  print("Error")
  quit()
print(result, convention )

'''10. Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
Original    Complement
"AAA" "UUU"
"UUU" "AAA"
"GGG" "CCC"
"CCC" "GGG"
Your function should find the complement on the right AND also reverse the resulting string.
Examples
reverse_complement("GUGU") ➞ "ACAC"
reverse_complement("UCUCG") ➞ "CGAGA"
reverse_complement("CAGGU") ➞ "ACCUG"
Notes
You can assume all input seqeuences will be valid.'''

def reverse_complement(RNA):
    pair = {"A":"U", "G":"C", "C":"G", "U":"A"}
    new_pair = ""
    for i in range(len(RNA) - 1, -1, -1):
        new_pair += pair[RNA[i]]
    return new_pair
print(reverse_complement("UCUCG"))

'''Imagine you have three numbers: a, b and c. c is equal to either a or b, but you dont know which one. Your task is to create a function that returns whatever number c is not out of a and b. So, if c is equal to a return b and if c is equal to b, return a.'''

a, b, c = (27, 31, 31)
print((c == b) * a + (c == a) * b)





