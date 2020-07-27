from copy import deepcopy
import time
from os import system
import random


class Cell:
    
    def __init__(self, phase=None):

        if phase:
            self.phase = phase
        else:
            self.phase = random.choice([True, False])

    def status(self, group):

        if group < 2:
            self.phase = False
        elif self.phase == True and 2 <= group <= 3:
            self.phase = True
        elif self.phase == False and group == 3:
            self.phase = True
        else:
            self.phase = False

    def __str__(self):
        if self.phase:
            return '[O]'
        else:
            return '[ ]'

class Glive:

    def __init__(self, rows=20, columns=20):

        self.rows = rows
        self.columns = columns
        self.board = []
        self.steps = 100
        self.time = 0.3
        
        for row in range(rows):
            columna = []
            for column in range(columns):
                columna.append(Cell())
            self.board.append(columna)
        
    def start(self):
        self.show('Initial')
        for n in reversed(range(self.steps)):
            nextboar = deepcopy(self.board)
            for row in range(self.rows):
                columna = []
                for column in range(self.columns):
                    neig = self.neighbor(row, column)
                    nextboar[row][column].status(neig)

            self.board = deepcopy(nextboar)
            self.show(n)
            

    def probe_state(self, patron=None):
        if patron:

            for cellx in range(len(patron)):
                for celly in range(len(patron[0])):
                               self.board[cellx][celly].phase=patron[cellx][celly]
        else:
            #slice
            self.board[1][1].phase = True
            self.board[2][2].phase = True
            self.board[0][3].phase = True
            self.board[1][3].phase = True
            self.board[2][3].phase = True



    def neighbor(self, x, y):
 
        offset = [-1,0,1]
        neigh = 0

        for posx in offset:
            for posy in offset:
                if 0 <= y + posy <= self.columns -1 and 0 <= x + posx <= self.rows -1:
                    if self.board[x + posx][y + posy].phase == True and not posx == 0 == posy:
                        neigh += 1
        return neigh


    def show(self, step):


        system('clear')
        print(f'Glive step {step}')
        print('-' * 12)
        
        row = ''
        for celly in range(self.columns):
            for cellx in range(self.rows):
                row += f'{self.board[cellx][celly]}'
            row += '\n'
        print(row)
        
        time.sleep(self.time)
        
        
if __name__ == '__main__':


    miboard = Glive()
    miboard.start()



