
class Board_class():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def display(self):
        print(("  "+ self.cells[1] + ' | ' +  self.cells[2] + " | " +  self.cells[3]))
        print("------------")
        print(("  " + self.cells[4] + ' | ' +  self.cells[5] + " | " +  self.cells[6]))
        print("------------")
        print("  " + self.cells[7] + ' | ' +  self.cells[8] + " | " +  self.cells[9])
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player


    def free_cell(self):
        free_cells = []
        for index, cell in enumerate(self.cells[1:10]):
            if cell == " ":
                free_cells.append(index+1)
        return free_cells
        
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    

        
if __name__== '__main__':            
    brd = Board_class() 
    brd.update_cell(9,'X')
    brd.display()
    brd.free_cell()
    brd.reset()





