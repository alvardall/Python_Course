from random import randint
def generate_number():
    randomNumber = randint(0,10)
    return randomNumber

def main():
    theNumber = generate_number()
    i = 1
    while True:
        print("Guess the number")
        number = int(input())
        if number == theNumber:
            print('Congratulation')
            print(f"The correct number is {str(number)}, you have tried {str(i)} times ")
            break
        elif number > theNumber:
            print('Go lower')
        elif number < theNumber:
            print('Go higer')
        print('=================')
        i += 1
main()



'''def solution(n): 
    
    while n:
        if n % 2:
            return False
    n //= 10   
    return True
print(solution(422))'''
