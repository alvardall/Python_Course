from Board import Board_class
from Player import Player
from Player import HumanPlayer
from Player import ComputerPlayer

class Game:
    def __init__(self):
        self.board = Board_class()
        self.human = HumanPlayer('X', self.board)
        self.computer = ComputerPlayer('O', self.board)
    
    def play(self):
        
        while True:
            self.human.move()
            self.board.display()
            if self.check_status(self.human):
                break
            self.computer.move()
            self.board.display()
            if self.check_status(self.computer):
                break
    
                
        
    def check_status(self, player:Player):
        cells = self.board.cells
        for i in range(3):
            if cells[i+1] == player.value and cells[i+4] == player.value and cells[i+7] == player.value: 
                print( "It's over! Player " + player.value + " wins!")
                return True
            elif cells[(i*3)+1] == player.value and cells[(i*3) + 2] == player.value and cells[(i*3) + 3] == player.value: 
                print( "It's over! Player " + player.value + " wins!")
                return True

            if cells[1] == player.value and cells[5] == player.value and cells[9] == player.value:
                print( "It's over! Player " + player.value + " wins!")
                return True
            elif cells[3] == player.value and cells[5] == player.value and cells[7] == player.value:
                print( "It's over! Player " + player.value + " wins!")
                return True
        
    
            
        if len(self.board.free_cell())==0:
            print("It's draw")
            return True
        return False



if __name__== '__main__':
    game = Game()
    game.play()
 
   
   

            
