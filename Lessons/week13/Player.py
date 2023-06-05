
from Board import Board_class
import random

class Player:
    def __init__(self,value: str, board: Board_class):
        self.value = value
        self.board = board
   
    def move(self):
        pass

class HumanPlayer(Player):
    def move(self):
        while True:
            self.board.display()
            number = input("\nX) Please choose 1-9. > ")
            if number.isdigit():
                number = int(number)
            else:
                print("Type integer from 1-9")
                continue

            if number not in list(range(10)):
                print('Integer should be from 1 to 9 range')
                continue

            if number not in self.board.free_cell():
                print('Please choose another number')
                continue
            break
        print('X number = ', number)
        self.board.update_cell(number,self.value)

class ComputerPlayer(Player):
    def move(self):  
        number = random.choice(self.board.free_cell())          
        print('0 number = ', number)
        self.board.update_cell(number,self.value)

if __name__== '__main__':  
    board = Board_class()
    human= HumanPlayer('X', board)
    computer = ComputerPlayer('O', board)
    human.move()
    computer.move()
    board.display()


