#1. Imaginary Coding Interview
def interview(lst, tot):
    if len(lst) != 8:
        return "disqualified"
    elif sum(lst) + 20 > 120:
        return "disqualified"
    elif tot > 120:
        return "disqualified"
    else:
        return "qualified"


print(interview([5, 5, 5, 9, 13, 14, 21, 23], 120))


#2.Natural Emptiness 
def rep_set(n):
    if n == 0:
        return []
    if n == 1:
        return [[]]
    return [rep_set(i) for i in range(n)]


print(rep_set(4))


#3.Basic Arithmetic Operations on a String Number
def arithmetic_operation(n):

    first_num, operation, second_num = n.split()
    if operation == '+':
        return int(first_num) + int(second_num)
    if operation == '-':
        return int(first_num) - int(second_num)
    if operation == '*':
        return int(first_num) * int(second_num)
    if operation == '//' and second_num == '0':
        return -1
    return int(first_num) // int(second_num)


print(arithmetic_operation("12 - 12"))


#4.Encode Morse 
def encode_morse(message):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}
    y = ""
    for i in message:
        if i != " ":
            y += MORSE_CODE_DICT[i] + " "
        else:
            y += " "
    return y
print(encode_morse("EDABBIT CHALLENGE"))


#5.Mahjong Tiles 
def gen_tiles():

    ranks = ['yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
    suits = ['tong', 'tiao', 'wan']
    specials = {'yi tong': 'bing gan', 'er tong': 'yan jing', 'yi tiao': 'ji'}

    res = []
    for rank in ranks:
        for suit in suits:
            tile = rank + ' ' + suit
            if tile in specials:
                tile = specials[tile]
            res.extend([tile]*4)
    return res
print(gen_tiles())


#6.Combined Consecutive Sequence
def consecutive_combo(lst1, lst2):
    x = lst1 + lst2
    return sorted(x) == list(range(min(x), max(x)+1))
print(consecutive_combo([44, 46], [45]))

#7. Tallest Skyscraper
def tallest_skyscraper(lst):
	for i in range(len(lst)):
		if lst[i].count(1):
			return len(lst) - i
print(tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]))

#8.Sales by Match 
def sock_merchant(lst):
	return sum(lst.count(i) // 2 for i in set(lst))
print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))

#9.Remove The Word! 
def remove_letters(letters, word):
    for i in word:
        if i in letters:
            letters.remove(i)
    return letters            
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))


#10.Majority Vote 
def majority_vote(lst):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i
        return None
print(majority_vote(["A", "A", "A", "B", "C", "C"]))

#11 Pluralize!
def pluralize(lst):
    plural = set()
    for i in set(lst):
        if lst.count(i) > 1:
            plural.add(i + 's')
        else:
            plural.add(i)
    return plural
print(pluralize(["cow", "pig", "cow", "cow"]))

#or
def pluralize(lst):
	return set(i + "s" if lst.count(i)> 1 else i for i in lst) 
print(pluralize(["cow", "pig", "cow", "cow"]))

#12 Secret Function 4.0
def secret(txt):
    x = txt.split(".")
    y = ""
    for i in x:
        if i == 'p':
            y += "<p class='"
        if i != 'p':
            y += i + ' '
    return y.rstrip() + "'></p>"
print(secret("p.one.two.three"))

#13 Geometry 3: Perimeter of a Triangle
def perimeter(lst):
	result = 0
	for a,b in lst:
		for x,y in lst:
			result += ((x-a)**2 + (y-b)**2)**0.5
	return round(result/2,2)
print(perimeter([[15, 7], [5, 22], [11, 1]]))

#14 Count and Identify Data Types
def count_datatypes(*args):
    lst = [type(i) for i in args]
    list_order = [int, str, bool, list, tuple, dict]
    return [lst.count(i) for i in list_order]
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))


#15 How Many Unique Styles?
def unique_styles(albums):
    set1 = set()
    for i in albums:
        for j in i.split(','): 
            set1.add(j)
    return len(set1)
print(unique_styles([
    "Dub,Dancehall",
    "Industrial,Heavy Metal",
    "Techno,Dubstep",
    "Synth-pop,Euro-Disco",
    "Industrial,Techno,Minimal"
]))
        