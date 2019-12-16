#!python3
# Dec 12, 2019
# -*- coding: utf-8 -*-

import simpleguitk as simplegui
import random
# open the image from this website
#address = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576970052&di=3314b7ee3a4151fddf15ff0c0cacb32a&imgtype=jpg&er=1&src=http%3A%2F%2Fimg.sj33.cn%2Fuploads%2Fallimg%2F201404%2F7-140419131052964.jpg'
byamax = simplegui.load_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576970052&di=3314b7ee3a4151fddf15ff0c0cacb32a&imgtype=jpg&er=1&src=http%3A%2F%2Fimg.sj33.cn%2Fuploads%2Fallimg%2F201404%2F7-140419131052964.jpg')
# set the screen size
WIDTH = 600
HEIGHT = WIDTH + 100
# set the size of the each piece of puzzle
IMAGE_SIZE = WIDTH/3

# set the coordinates of the pieces
all_coordinates = [[IMAGE_SIZE*0.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*0.5],
                        [IMAGE_SIZE*2.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*0.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*1.5, IMAGE_SIZE*1.5], [IMAGE_SIZE*2.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*0.5, IMAGE_SIZE*2.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*2.5], None]

# set the screen to a 3x3 board
ROWS = 3
COLS = 3

steps = 0

# set the format as a constant 
board = [[None,None,None],[None,None,None],[None,None,None]]

# create a collection of the puzzle pieces
class Square:
    def __init__(self, coordinage):
        self.center = coordinage

    def draw(self, canvas, board_pos):

        canvas.draw_image(byamax,self.center,[IMAGE_SIZE,IMAGE_SIZE],
                          [(board_pos[1]+0.5)*IMAGE_SIZE,(board_pos[0]+0.5)*IMAGE_SIZE],[IMAGE_SIZE,IMAGE_SIZE])

# apply the small pieces of pictures into the squares
def init_board(): 

    # disorganize the pictures
    random.shuffle(all_coordinates)

    # replace and joint the squares
    for i in range(ROWS):
        for j in range(COLS):

            idx = i * ROWS + j
            square_center = all_coordinates[idx]

            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


def play_game():

    #reset the game 
    global steps
    steps = 0
    init_board()

# create a discription box
def draw(canvas):

    # location
    canvas.draw_image(byamax,[WIDTH/2,WIDTH/2],[WIDTH,WIDTH],[50,WIDTH+50],[98,98])

    # show the steps the player has done
    canvas.draw_text('Steps：'+str(steps),[400,680],22,'White')

    # show them on the screen
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(canvas,[i,j])

# the movement of the squares
def mouseclick(pos):

    global steps

    # r = roll, c = column
    r = int(pos[1]//IMAGE_SIZE)
    c = int(pos[0]//IMAGE_SIZE)

    # if click the blank square the movement of the squares pause
    if r<3 and c<3:
        if board[r][c] is None:
            return

        # check the squares around the square that the player clicks
        else:
            current_square = board[r][c]
            if r - 1 >= 0 and board[r - 1][c] is None:  # check the above square
                board[r][c] = None
                board[r - 1][c] = current_square
                steps += 1
            elif c + 1 <= 2 and board[r][c + 1] is None:  # chech the square on the right
                board[r][c] = None
                board[r][c + 1] = current_square
                steps += 1
            elif r + 1 <= 2 and board[r + 1][c] is None:  # check the square below
                board[r][c] = None
                board[r + 1][c] = current_square
                steps += 1
            elif c - 1 >= 0 and board[r][c - 1] is None:  # check the square on the left
                board[r][c] = None
                board[r][c - 1] = current_square
                steps += 1


frame = simplegui.create_frame('Puzzle',WIDTH,HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.add_button('Restart',play_game,60)

frame.set_mouseclick_handler(mouseclick)

play_game()

frame.start()
