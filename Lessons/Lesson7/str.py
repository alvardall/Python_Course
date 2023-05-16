# Week 4.1 strings

def str_to_int(s):
    return int(s)
print(str_to_int("1000"))

def bool_to_str(bool):
    return str(bool)
print(bool_to_str(False))

def joined(a):
    s = "something"
    return s + " " + a
print(joined("is better than nothing"))

def relation(name):
    dict1 = {"Darth Vader": 'father', 'Leia': 'sister', "Han": 'brother in law', "R2D2": 'droid'}
    return "Luke, I am your " + dict1[name]
print(relation("Darth Vader"))

def number_of_vowels(s):
    vowels = 'aeiou'
    lst1 = []
    for i in vowels:
        if i in s.lower():
            lst1.append(s.lower().count(i))
    return sum(lst1)
  
print(number_of_vowels("ArmtdftrEEEEsateee"))

def inequality(s):
    return eval(s)
print(inequality("1 < 2 < 6 < 9 > 3"))

def replace_s(s, charact):
    vowels = 'aeiou'
    for i in vowels:
        if i in s:
            s = s.replace(i, charact)
    return s
print(replace_s("shakespeare", "*"))

def card_number(s):
    return '*' * (len(s)-4) + s[-4:]

print(card_number("35123413355523"))

def swapped(name):
    return name.split(' ')[1] + ' ' + name.split(' ')[0]
print(swapped("Rosie O'Donnell"))

def isogram(s):
    for i in s:
        if s.lower().count(i) > 1:
            return False      
    return True
print(isogram("PasSword"))

# Week 3.2 

def my_love(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    return "Hello, " + name + "!"

print(my_love("Matt"))

def arguments(a, b):
    if a == 10:
        return True
    if b == 10:
        return True
    if a + b == 10:
        return True
    return False
print(arguments(0, 10))

def divisible(n):
    return n % 5 == 0
print(divisible(37))

def equal(a1, a2):
    return len(a1) == len(a2)
print(equal("hello", "edabit"))

def lenth(s):
    return len(s)% 2 == 0
print(lenth('dfddk'))

def repeated (txt, n):
    if type(txt) is not str:
        return "Not A String !!"
    return txt * n
print(repeated ('Mubashir', 2))

def volid(pin):
    if pin.isnumeric() and (len(pin) == 6 or len(pin) == 4):
        return True
   
      
    return False
print(volid('786 '))
        

