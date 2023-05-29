#decorator that returns the time of the function
from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function  executed in {(t2-t1)}s')
        return result
    return wrap_func

@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j
long_time(5)
#Game Tic tak toe
def board(self):
    print("")
    for i in range(0, 3):
        print("-------------")
        out = "| "
        for j in range(0, 3):
            if self.board[i, j] == 1:
                token = "X"
            if self.board[i, j] == -1:
                token = "0"
            if self.board[i, j] == 0:
                token = " "
            out += token + " | "
        print(out)
    print("-------------")





