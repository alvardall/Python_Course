

        #Edabit/Medium/Classes
#1
class Calculator:
	
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a // b
calculator = Calculator()

print(calculator.add(10, 5))

#2
class ones_threes_nines:
	
	def __init__(self, n):
		self.ones = n
		self.threes = n // 3
		self.nines = n // 9
n1 = ones_threes_nines(5)
print(n1.ones)  

#3
class Player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return (f'{self.name} is age {self.age}')

    def get_height(self):
        return (f'{self.name} is  {self.height} cm')

    def get_weight(self):
        return (f'{self.name} is  {self.weight} kg')

p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())

#4
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = (f'{firstname} {lastname}')
        self.email = (f'{firstname}.{lastname}@company.com').lower()
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
print(emp_2.email)

#5
class User:
    user_count = 0
    def __init__(self, u):
        self.username = u
        User.user_count += 1
u1 = User("johnsmith10")
u2 = User("marysue1989")
u3 = User("milan_rodrick")
print(User.user_count)

#6
class Name:
    def __init__(self, fname, lname):
        self.firsname = fname
        self.lastname = lname.title()
        self.fullname = fname +' ' + lname.title()
        self.initials = fname[0].capitalize() + '.' + lname[0].capitalize()
a1 = Name("john", "SMITH")
print(a1.initials) 
print(a1.lastname) 
print(a1.firsname)
print(a1.fullname)

#7
class Composer:
    count = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1
c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")

print(Composer.count)

#8
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return (f'Title: {self.title}')
    
    def get_autor(self):
        return (f'Author: {self.author}')
PP = Book('Pride and Prejudice',  'Jane Austen' )
H = Book('Hamlet',  'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy') 
print(H.title)
print(H.author)
print(H.get_title())
print(H.get_autor())

#9
class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
    def taste(self, food):
        if food in self.like:
            add = " and loves it"
        elif food in self.hate: 
            add = " and hates it"
        else: add= ""
        return self.name +  ' eats the ' + food + add + '!'
p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))

#10
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.density = self.population / self.area
        self.is_big = population > 250000000 or area > 3000000
    def compare_pd(self, other):
        result = ['smaller', 'larger'][self.density > other.density]
        return '{} has a {} population density than {}'.format(self.name, result, other.name)
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.is_big)
print(andorra.compare_pd(australia))

        