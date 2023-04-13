'''1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"
say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
say_hello_bye("jose", 0) ➞ "Bye Jose"'''

name, number = ("Tomi", 0)
if number == 1:
    print('Hello ' + name.capitalize())
else:
    number == 0
    print('Bye ' + name.capitalize())


'''2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.
Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False'''

lst = (["&&", "&", "&&&", "&&&&"])
print(all(x == lst[0] for x in lst))

# or
lst = (["&&", "&", "&&&", "&&&&"])
print(lst[:-1] == lst[1:])

'''3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
Examples
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False
Notes
Return True for the edge case of an empty array of hurdles. (Zero hurdles means that any jump height can clear them).'''
hurdle_heights, jump_height = ([1, 2, 1], 1)
if jump_height >= max(hurdle_heights):
    print(True)
else:
    print(False)

'''4. Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]
Notes
The input integer will be positive.
A factor is a number that evenly divides into another number without leaving a remainder. The second example is a factor of 12, because 12 / 2 = 6, with remainder 0.'''

x = 12
new_list = []
for i in range(1, x + 1):
    if x % i == 0:
        new_list.append(i)
print(new_list)

'''5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers.'''

start, end = (1, 10)
new_list = []
for num in list(range(start, end+1)):
    if str(num) == str(num)[::-1]:
        new_list.append(num)
print(len(new_list))

'''6. Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.
Define a separate is_vowel() function for easier to read code (recommendation).'''

x = ("abcde")
str1= ""
str2= ""
vowel = "aeiou"
for i in x:
    if i in vowel:
        str1 += i
    else:
        str2 += i
result = str1 + str2
print(result)


'''7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.
Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.'''

x = ("programming is fun")
print(x.replace('a', '4').replace("e", '3').replace(
    's', '5').replace('i', '1').replace('o', '0'))



'''8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.
Examples
return_end_of_number(553) ➞ "553-RD"
return_end_of_number(34) ➞ "34-TH"
return_end_of_number(1231) ➞ "1231-ST"
return_end_of_number(22) ➞ "22-ND"
return_end_of_number(412) ➞ "412-TH"'''
x = (10)
n = int(x)
if 11 <= (n % 100) <= 13:
    end_of_number = 'TH'
else:
    end_of_number = ['TH', 'ST', 'ND', 'RD', 'TH'][min(n % 10, 4)]
    print(str(n) + '-' + end_of_number)

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
You can assume all input seqeuences will be valid.
"AAA" "UUU"
"UUU" "AAA"
"GGG" "CCC"
"CCC" "GGG"'''

x = ("UCUCG")

converted_test = x.replace('A', 'E').replace('U', 'A').replace(
    'E', 'U').replace('C', 'E').replace('G', 'C').replace('E', 'G')
print((converted_test)[::-1])

