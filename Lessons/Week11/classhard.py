
#1 Magic Function
class Magic:
    
    def trim(self,a):
        return  a.strip()
    def replace(self,a,b,c):
        return a.replace(b,c)
    def str_length(self,a):
        return len(a)
    def list_slice(self,a,b):
        return  a[b[0]-1:b[1]] if len(a)> 0 else -1
magic = Magic()
print(magic.replace("AzErty-QwErty", "E", "e")) 
print(magic.str_length("hello world"))
print(magic.trim("      python is awesome      "))
print(magic.list_slice([], (2, 4)))

#2 Ones, Threes and Nines (Version #2)
class ones_threes_nines:
    def __init__(self, n):
        self.nines = n// 9
        n -= self.nines * 9
        self.threes = n//3
        n -= self.threes * 3
        self.ones = n
        self.answer = (f"nines:{self.nines}, threes:{self.threes}, ones:{self.ones}")
x1 = ones_threes_nines(10)
x2 = ones_threes_nines(15)
x3 = ones_threes_nines(22)
print(x1.answer)
print(x2.answer)
print(x3.answer)

#3

class Menu:
	
	def __init__(self,lst):
		self.lst = lst
		self.index = 0
	
	def to_the_right(self):
		index = self.index
		self.index = self.index + 1 if index < len(self.lst) - 1 else 0	
	
	def display(self):
		self.copy = self.lst.copy()
		self.copy[self.index] = [self.copy[self.index]]
		return str(self.copy)
menu = Menu([1, 2, 3])
print(menu.display())
menu.to_the_right()
print(menu.display())
menu.to_the_right()
print(menu.display())
menu.to_the_right()
print(menu.display())

#4
class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary 
    def from_string(s):
        firstname, lastname, salary = s.split('-')
        return Employee(firstname, lastname, int(salary))

emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.salary)

#5 People Sort
class Person:
    def __repr__(self):
            return '({})'.format(self.lastname)

def people_sort(lst, attr):
	if attr == 'firstname':
		result = sorted(lst, key=lambda x: x.firstname)
	elif attr == 'lastname':
		result = sorted(lst, key=lambda x: x.lastname)
	else:
		result = sorted(lst, key=lambda x: x.age)
	return result
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

print(people_sort([p1, p2, p3], "firstname"))


#6
class Memories:
    def __init__(self):
        self.baza = dict()
    def add(self, **kwargs):
        self.baza.update(kwargs)
    def remember(self, reqall):
        if reqall in self.baza:
            return self.baza[reqall]
        return False
memories = Memories()
memories.add(name="Shane", gender="M", catch_phrase="bazinga")
memories.add(work="None", love_life=0)
memories.add(adress="car")

print(memories.remember("catch_phrase"))
print(memories.remember("gender"))
print(memories.remember("adress"))


#7 Shiritori Game
class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False
    def play(self,new):
        if self.words==[] or (new[0]==self.words[-1][-1] and new not in self.words):
            self.words.append(new)
            return self.words
        self.game_over = True
        return "game over"
    def restart(self):
        self.__init__()
        return "game restarted"
    
my_shiritori = Shiritori()
print(my_shiritori.play("apple"))
print(my_shiritori.play("ear"))
print(my_shiritori.play("rhino"))
print(my_shiritori.play("corn"))
print(my_shiritori.words)
print(my_shiritori.restart())
print(my_shiritori.words)

#8
class Employee:
    
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name, self.lastname = full_name.split()
        self.__dict__.update(kwargs)
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(john.name)
print(mary.lastname)
print(richard.height)
print(giancarlo.nationality)
    