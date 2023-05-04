'''1. Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.'''

def remove_letters(letters, word): 
    
    for i in word: 
        if i in letters: 
            letters.remove(i)
    return letters   
    
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))

'''2. Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.'''

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

'''3. Create a function based on the input and output. Look at the examples, there is a pattern.'''

def secret(txt):
    x = txt.split(".")
    y = ""
    for i in x:
        if i == 'p':
            y += "'<p class='"
        if i != 'p':
            y += i + " "
    return y[:-1] + "'></p>'"
print(secret("p.four.five"))


'''4. Create a function which takes in an encoded string and returns a dictionary according to the following example:'''

def parse_code(txt):
    n, s, i = [x for x in txt.split('0') if len(x)]
    return {'first_name': n, 'last_name': s, 'id': i}
print(parse_code("John000Doe000123"))


'''5. "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.
Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.'''

def loves_me(n):
    s= []
    if n==1:
        return 'LOVES ME'
    for i in range(n):
        if i%2==0:
            s.append('Loves me')
        else:
            s.append('Loves me not')
    
        a=', '.join(s)
    if s[-1]=='Loves me':
        return a + ', ' + 'LOVES ME NOT'
    else:
        return a+', '+'LOVES ME'
print(loves_me(3))

