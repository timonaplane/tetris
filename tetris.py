#!/usr/bin/python
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y


import pygame
import random

#Set up some colors
WHITE = 0xffffff
BLACK = 0x000000
RED = 0xff0000
GREEN = 0x00ff00
BLUE = 0x0000ff
YELLOW = 0xffff00
CYAN = 0x00ffff
PURPLE = 0x800080
ORANGE = 0xffa500

#Some size variables
WIDTH = 600
HEIGHT = 600
PIECE_SIZE = 25

#80 rows -> 400
#25 columns - > 125

#set up some pygame stuff
pygame.font.init()
font = pygame.font.Font(None, 36)

# define the piece rotations
z_rotations = [[Node(0,0) , Node(25, 0) , Node (25, 25), Node(50,25)],
[Node(25,0), Node(25,25), Node(50,0), Node(50,-25)]]
s_rotations = [[Node(0,0), Node(25,0), Node(25,-25), Node(50,-25)],
[Node(0,-25), Node(0,-50), Node(25,-25), Node(25,0)]]
i_rotations = [[Node(0,0), Node(25, 0), Node(50,0) , Node(75,0)],
[Node(25,-25), Node(25,0), Node(25,25), Node(25,50)]]
t_rotations = [[Node(0,0), Node(25, 0), Node(50,0), Node(25,25)],
[Node(0,0), Node(25,0), Node(25,-25), Node(25,25)],
[Node(25,-25), Node(0,0), Node(25,0), Node(50,0)],
[Node(50,0), Node(25,-25), Node(25,0), Node(25,25)]]
l_rotations = [[Node(0,0),Node(0,25),Node(25,0),Node(50,0)],
[Node(0,0),Node(25,0),Node(25,25),Node(25,50)],
[Node(0,50),Node(25,50),Node(50,25),Node(50,50)],
[Node(25,0),Node(25,25),Node(25,50),Node(50,50)]]
j_rotations = [[Node(0,0), Node(25,0), Node(50,0), Node(50,25)],
[Node(0,50), Node(25,0),Node(25,25),Node(25,50)],
[Node(0,25),Node(0,50),Node(25,50),Node(50,50)],
[Node(25,0),Node(25,25),Node(25,50),Node(50,0)]]



## NOTE: node 0,0 is always the bottom left most square in a piece
def generate_piece(piece_type):
    new_list = []
    if piece_type == 'z':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(25,25))
        new_list.append(Node(50,25))
        return new_list,RED
    elif piece_type == 's':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(25,-25))
        new_list.append(Node(50,-25))
        return new_list,GREEN
    elif piece_type == 'i':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(50,0))
        new_list.append(Node(75,0))
        return new_list,CYAN
    elif piece_type == 't':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(50,0))
        new_list.append(Node(25,25))
        return new_list,PURPLE
    elif piece_type == 'o':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(0,-25))
        new_list.append(Node(25,-25))
        return new_list,YELLOW
    elif piece_type == 'l':
        new_list.append(Node(0,0))
        new_list.append(Node(0,25))
        new_list.append(Node(25,0))
        new_list.append(Node(50,0))
        return new_list,BLUE
    elif piece_type =='j':
        new_list.append(Node(0,0))
        new_list.append(Node(25,0))
        new_list.append(Node(50,0))
        new_list.append(Node(50,-25))
        return new_list,ORANGE



#also need to check the game_matrix

#will fail to rotate piece if the rotation puts piece out of bounds
def rotate_piece(piece_list , piece_type, piece_status, PIECE_X, PIECE_Y, direction):
    temp_piece_list = []
    temp_piece_list.extend(piece_list)
    temp_piece_status = piece_status
    if(piece_type != 'o'):
        temp_piece_list.clear()
    if(direction =='right'):
        temp_piece_status += 1
    elif(direction =='left'):
        temp_piece_status -= 1

    if piece_type == 'z':
        if temp_piece_status == 2:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 1
        temp_piece_list.extend(z_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status
    elif piece_type == 's':
        if temp_piece_status == 2:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 1
        temp_piece_list.extend(s_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status
    elif piece_type =='i':
        if temp_piece_status == 2:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 1
        temp_piece_list.extend(i_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status
    elif piece_type =='t':
        if temp_piece_status == 4:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 3
        temp_piece_list.extend(t_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status
    elif piece_type =='l':
        if temp_piece_status == 4:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 3
        temp_piece_list.extend(l_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status
    elif piece_type =='j':
        if temp_piece_status == 4:
            temp_piece_status = 0
        elif temp_piece_status == -1:
            temp_piece_status = 3
        temp_piece_list.extend(j_rotations[temp_piece_status])
        #return piece_x, piece_y,  piece_status

    #check the temp_piece_list if in bounds
    for x in temp_piece_list:
        if x.x + PIECE_X < 0 or x.x + PIECE_X >= WIDTH or x.y + PIECE_Y >= HEIGHT:
            return PIECE_X, PIECE_Y, piece_status

    piece_list.clear()
    piece_list.extend(temp_piece_list)
    return PIECE_X, PIECE_Y, temp_piece_status

#also need to check the game_matrix
def can_move_horiz(curr_piece, PIECE_X, PIECE_Y, direction):
    if direction == 'left':
        for x in curr_piece:
            if(x.x + PIECE_X - 25 < 0):
                return False
    else:
        for x in curr_piece:
            if(x.x + PIECE_X + 25 >= WIDTH):
                return False
    return True
#also need to check the game_matrix

def can_move_down(curr_piece, PIECE_X, PIECE_Y):
    for x in curr_piece:
        if x.y + PIECE_Y + 25 >= HEIGHT:
            return False
    return True



def lock_piece(curr_piece, PIECE_X, PIECE_Y, GAME_MATRIX,piece_type):
    # [add x.x = + piece_x / piece_size][add x.y = + piece_y / piece_size] to game matrix
    print('called function')
    for x in curr_piece:
        GAME_MATRIX[(x.x + PIECE_X)//PIECE_SIZE][(x.y + PIECE_Y) //PIECE_SIZE] = piece_type

    return GAME_MATRIX

def main():
    #Set up the main stuff
    pygame.init()
    surface = pygame.display.set_mode((WIDTH,HEIGHT))
    GAME_MATRIX = [['p' for x in range(WIDTH//PIECE_SIZE)] for y in range(HEIGHT//PIECE_SIZE)]

    #Move down timer
    timer = 0
    PIECE_X = 200
    PIECE_Y = 0
    curr_piece = []
    piece_status = 0
    need_new_piece = False
    piece_type = 'l'
    pieces = ['i','o','t','s','z','j','l']
    color_maps = {'i':CYAN, 'o':YELLOW, 't':PURPLE, 's':GREEN,'z':RED,'j':ORANGE,'l':BLUE}
    piece_type = pieces[random.randint(0,6)]
    curr_piece,color = generate_piece(piece_type)
    can_move1 = True


    while True:

        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if(can_move_horiz(curr_piece,PIECE_X,PIECE_Y,'left')):
                        PIECE_X -= PIECE_SIZE
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if(can_move_horiz(curr_piece,PIECE_X,PIECE_Y,'right')):
                        PIECE_X += PIECE_SIZE
                elif event.key == pygame.K_z:

                    PIECE_X, PIECE_Y, piece_status = rotate_piece(curr_piece, piece_type, piece_status, PIECE_X, PIECE_Y, 'left')
                elif event.key == pygame.K_x:
                    PIECE_X, PIECE_Y, piece_status = rotate_piece(curr_piece, piece_type, piece_status, PIECE_X, PIECE_Y, 'right')
                elif event.key == pygame.K_DOWN:
                    if(can_move_down(curr_piece,PIECE_X,PIECE_Y)==True):
                        PIECE_Y += PIECE_SIZE
                    else:
                        #add to the array
                        need_new_piece = True
                        GAME_MATRIX = lock_piece(curr_piece,PIECE_X,PIECE_Y,GAME_MATRIX,piece_type)
                        timer = 0

        if(timer >= 1000):
            #can_move1 = can_move(curr_piece)
            if(can_move_down(curr_piece, PIECE_X, PIECE_Y) == True):
                PIECE_Y += PIECE_SIZE
                timer = 0
            else:
                GAME_MATRIX = lock_piece(curr_piece,PIECE_X,PIECE_Y,GAME_MATRIX,piece_type)
                timer = 0
                need_new_piece = True
        if(need_new_piece == True):
            piece_type = pieces[random.randint(0,6)]
            curr_piece,color = generate_piece(piece_type)
            need_new_piece = False
            PIECE_X = 200
            PIECE_Y = 0



        #check if the piece touches bottom of screen



        pygame.display.update()
        surface.fill(BLACK)
        #pygame.draw.rect(surface, RED, piece_rect)
        for x in curr_piece:
            pygame.draw.rect(surface, color, pygame.Rect(x.x + PIECE_X ,x.y + PIECE_Y, PIECE_SIZE, PIECE_SIZE))
        #display the locked boxes
        yes = 5
        for a in range(0, WIDTH//PIECE_SIZE):
            for b in range(0, HEIGHT//PIECE_SIZE):
                if(GAME_MATRIX[a][b] != 'p'):
                    pygame.draw.rect(surface, color_maps[GAME_MATRIX[a][b]], pygame.Rect(a*PIECE_SIZE,b*PIECE_SIZE,PIECE_SIZE, PIECE_SIZE))
        # for a in range(0,WIDTH//PIECE_SIZE):
        #     for b in range(0,HEIGHT//PIECE_SIZE):
        #         print('hello')
                 #if(GAME_MATRIX[a*PIECE_SIZE][b*PIECE_SIZE] != 'p'):
                    # pygame.draw.rect(surface, color_maps[GAME_MATRIX[a*PIECE_SIZE][b*PIECE_SIZE]], pygame.Rect(a**PIECE_SIZE,b**PIECE_SIZE,PIECE_SIZE,_PIECE_SIZE))




main()
input('Press ENTER to exit')
