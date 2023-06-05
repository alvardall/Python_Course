import os
os.system('clear')

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def display(self):
        print(("  "+ self.cells[1] + ' | ' +  self.cells[2] + " | " +  self.cells[3]))
        print("------------")
        print(("  " + self.cells[4] + ' | ' +  self.cells[5] + " | " +  self.cells[6]))
        print("------------")
        print("  " + self.cells[7] + ' | ' +  self.cells[8] + " | " +  self.cells[9])
    def update_cell(self, number, player):
        if self.cells[number] == " ":
            self.cells[number] = player

    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        return False
    
    def is_tie(self):
        used_cells = 0
      
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False


    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()
def print_header():
    print("Welcome to Tic-Tac-Toe\n")
def refresh_screen():
    os.system('clear')

    print_header()
    board.display()

while True:
    refresh_screen()
    x_number = int(input("\nX) Please choose 1-9. > "))
    board.update_cell(x_number, "X")
    refresh_screen()

    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
        

    O_number = int(input("\n0) Please choose 1-9. > "))
    board.update_cell(O_number, "0")
    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break



