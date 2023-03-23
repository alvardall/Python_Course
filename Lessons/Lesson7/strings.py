

'''
1. Create a function that takes a string and returns it as an integer.
Examples
"6" ➞ 6
"1000" ➞ 1000
Notes
All numbers will be whole.
All numbers will be positive
'''

x = '1000'
y = x.isnumeric
print((x != float and int(x)>0) * int(x))

'''
2. Create a function that takes a boolean variable flag and returns it as a string.
Examples
True ➞ "True"
False ➞ "False"
'''

x = bool(True)
print(str(x))

'''
3. Write a function that returns the string "something" joined with a space " " and the given argument a.
Examples
"is better than nothing" ➞ "something is better than nothing"
"Bob Jane" ➞ "something Bob Jane"
"something" ➞ "something something"
'''

a = "Bob Jane" 
b = "something "
print(b + a)

'''
4. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid
Examples
"Darth Vader" ➞ "Luke, I am your father."
"Leia" ➞ "Luke, I am your sister."
"Han" ➞ "Luke, I am your brother in law."
'''

input_name = input("Enter name:")   
name = str(input_name)
x =(name == 'Darth Vader')* 'father'
y = (name == "Leia") * "sister"
z = (name == "Han") * "brother in law"
g = (name == "R2D2") * 'droid'
print("Luke, I am your " + x +y + z + g)

'''
5. Create a function that takes a string and returns the number (count) of vowels contained within it.
Examples
"Celebration" ➞ 5
"Palm" ➞ 1
"Prediction" ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
'''

data = str(input("Enter a sentence: "))
vowels = "aeiou"
for v in vowels:
    print(data.lower().count(v))

'''
7. Create a function that replaces all the vowels in a string with a specified character.
Examples
"the aardvark", "#" ➞ "th# ##rdv#rk"
"minnie mouse", "?" ➞ "m?nn?? m??s?"
"shakespeare", "*" ➞ "sh*k*sp**r*"
'''

x, y = "minnie mouse", "?"
vowels = 'aeiou'

print(x.replace('a', y ).replace('e', y ).replace('i',y ).replace('o', y ).replace('u', y ))
'''
8. Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.
Examples
"1234123456785678" ➞ "************5678"
"8754456321113213" ➞ "************3213"
"35123413355523" ➞ "**********5523"
'''
def last_four_characters(s):
    return (len(s) - len(s[-4::])) * '*' + s[-4::]

print(last_four_characters("1234123456785678"))


'''
9. Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.
Examples
"Donald Trump" ➞ "Trump Donald"
"Rosie O'Donnell" ➞ "O'Donnell Rosie"
"Seymour Butts" ➞ "Butts Seymour"
'''

name = input('Entr name_surname:') 
name = name.split()                           
print(name[1]+''+name[0])

'''
10. An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples
"Algorism" ➞ True
"PasSword" ➞ False
# Not case sensitive.
"Consecutive" ➞ False
'''

def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)
print(is_isogram("PasSword"))









