from karel.stanfordkarel import *
#pikachu i choose you for this! 
def main():
    row_1()
    next_row_left()
    row_2()
    next_row_right()
    row_3()
    next_row_left()
    row_4()
    next_row_right()
    row_5()
    next_row_left()
    row_6()
    next_row_right()
    row_7()
    next_row_left()
    row_8()
    next_row_right()
    row_9()
    next_row_left()
    row_10()
    next_row_right()
    row_11()
    next_row_left()
    row_12()
    next_row_right()
    row_13()
    next_row_left()
    row_14()
    next_row_right()
    row_15()
    next_row_left()
    row_16()
    next_row_right()
    row_17()
    next_row_left()
    row_18()
    next_row_right()
    row_19()
    next_row_left()
    row_20()
    
#row 1
def row_1():
    for i in range(7):
        move()
    for i in range(3):
        paint_corner(BLACK)
        move()
    
    #row 2
def row_2():
    paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 3
def row_3():
    for i in range(2):
        paint_corner(BLACK)
        move()
    paint_corner(YELLOW)
    move()
    for i in range(3):
        paint_corner(BLACK)
        move()
    for i in range(4):
        move()
    
    #row 4
def row_4():
    for i in range(5):
        paint_corner(BLACK)
        move()
    for i in range(5):
        paint_corner(YELLOW)
        move()
    paint_corner(BLACK)
    move()
    
    #row 5
def row_5():
    paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 6
def row_6():
    move()
    paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 7
def row_7():
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(2):
        paint_corner(YELLOW)
        move()
    paint_corner(BLACK)
    move()
    for i in range(5):
        paint_corner(YELLOW)
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    
    #row 8
def row_8():
    paint_corner(BLACK)
    for i in range(11):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 9
def row_9():
    for i in range(3):
        paint_corner(BLACK)
        move()
    for i in range(3):
        paint_corner(YELLOW)
        move()
    paint_corner(RED)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()
    
    #row 10
def row_10():
    paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(RED)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    for i in range(3):
        move()
        paint_corner(BLACK)
    move()

#row 11
def row_11():
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(5):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()
    paint_corner(WHITE)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 12
def row_12():
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(9):
        paint_corner(YELLOW)
        move()
    paint_corner(BLACK)
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 13
def row_13():
    paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()
    move()
    paint_corner(BLACK)
    for i in range(9):
        move()
        paint_corner(YELLOW)
    move()
    move()
    paint_corner(BLACK)
    
    #row 14
def row_14():
    move()
    paint_corner(BLACK)
    for i in range(9):
        move()
        paint_corner(YELLOW)
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()
    
    #row 15
def row_15():
    paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    for i in range(2):
        for i in range(2):
            move()
            paint_corner(BLACK)
        for i in range(2):
            move()
            paint_corner(YELLOW)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 16
def row_16():
    move()
    paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    for i in range(2):
        move()
    for i in range(5):
        move()
        paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    move()

#row 17
def row_17():
    paint_corner(BLACK)
    for i in range(4):
        move()
        paint_corner(YELLOW)
    for i in range(3):
        move()
        paint_corner(BLACK)
    for i in range(5):
        move()
    paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 18
def row_18():
    move()
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    for i in range(8):
        move()
    paint_corner(BLACK)
    for i in range(3):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    
    #row 19
def row_19():
    move()
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(BLACK)
    for i in range(8):
        move()
    for i in range(3):
        move()
        paint_corner(BLACK)
    
    #row 20
def row_20():
    move()
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(9):
        move()
    paint_corner(BLACK)

def next_row_left():
    turn_left()
    move()
    turn_left()

def next_row_right():
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
