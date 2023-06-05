#1.  Write a map function that adds plus 5 to each item in the list.
lst1=[10, 20, 30, 40, 50, 60]
lst2= list(map(lambda item: item+5, lst1))
print(lst2)

#2.  Write a map function that adds "Hello, " in front of each item in the list.
lst1=["Alla", "Anna", "Lilia", "Mari"]
lst2 = list(map(lambda item: "Hello, " + item, lst1))
print(lst2)

#3.  Using filter() function filter the list so that only negative numbers are left.
lst1=[100, -1, -9, 15, -8, -0.5, 78, -0.2, -100]
lst2 = list(filter(lambda item: item<0, lst1))
print(lst2)

#4.  Using filter function, filter the even numbers so that only odd numbers are passed to the new list
lst1=[48, 96, 101, 29, 17, 9, 323, -8, -7]
lst2 = list(filter(lambda x: x%2 == 1, lst1))
print(lst2)

#5.  Using map() and filter() functions add 2000 to the values below 8000.
lst1=[50, 1000, 10000, 750, 70, 9500, 13000]
lst2 = list(map(lambda item: item+2000, filter(lambda item: item<8000, lst1)))
print(lst2)
#6.  Return product of integer lists
from functools import reduce
list1 = [5, 7, 3, 2]
result = reduce((lambda x, y: x * y), list1)
print(result)


def is_tie(cells):
        
        x = []
        for cell in cells:
        if cell == " ":

                x.append(cells.index(cell)+1)
        return  x
       
            
      
        
print(is_tie( [" ", "X", "m", " ", " ", "o", " ", " ", " ", " "]))



