# importing the libraries
import pygame
from pygame import mixer
import random
# initialising the imported libraries
pygame.init()
mixer.init()
# Setting the screen size
screen_width = 600
screen_height = 650
# Loading the sprites
icon = pygame.image.load("icon.png")
background = pygame.image.load("paper_bg.jpg")
background = pygame.transform.scale(background, (600, 650))
X = pygame.image.load("X.png")
X = pygame.transform.scale(X, (200, 200))
O = pygame.image.load("O.png")
O = pygame.transform.scale(O, (200, 200))
Boxes = pygame.image.load("boxes.png")
Boxes = pygame.transform.scale(Boxes, (600, 600))
bge = pygame.image.load("winner bg.jpg")
bge = pygame.transform.scale(bge, (600, 650))

# Setting up the pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)
# Creating a Text
pygame.font.init()
font = pygame.font.SysFont('Corbel', 35, bold=True, italic=True)
text_invalid = font.render("Invalid Move", True, [128, 0, 0], [0, 0, 0])
text_invalid_rect = text_invalid.get_rect()
text_invalid_rect.center = (300, 625)
text_player1 = font.render("Player 1", True, [0, 0, 128], [128, 128, 128])
text_player1_rect = text_player1.get_rect()
text_player1_rect.center = (300, 625)
text_player2 = font.render("Player 2", True, [0, 0, 128], [128, 128, 128])
text_player2_rect = text_player1.get_rect()
text_player2_rect.center = (300, 625)
# Making a lookup table
lookup_table = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
# Splitting the places
B1 = pygame.Rect(0, 0, 200, 200)
B2 = pygame.Rect(200, 0, 200, 200)
B3 = pygame.Rect(400, 0, 200, 200)
B4 = pygame.Rect(0, 200, 200, 200)
B5 = pygame.Rect(200, 200, 200, 200)
B6 = pygame.Rect(400, 200, 200, 200)
B7 = pygame.Rect(0, 400, 200, 200)
B8 = pygame.Rect(200, 400, 200, 200)
B9 = pygame.Rect(400, 400, 200, 200)
# Making lists to store
B = [B1, B2, B3, B4, B5, B6, B7, B8, B9]
loc = [(0, 0), (200, 0), (400, 0), (0, 200), (200, 200), (400, 200), (0, 400), (200, 400), (400, 400)]


# creating a class for the X player
class player1(object):

    def __init__(self, turn, mouse):
        self.turn = turn
        self.mouse = mouse

    def draw(self, mouse):
        if self.turn == 1:
            for j in range(9):
                if pygame.Rect.collidepoint(B[j], mouse[0], mouse[1]):
                    if lookup_table[j] == 'E':
                        lookup_table[j] = 'X'
                        self.turn = 0
                        O_player.turn = 1


# creating class for O player
class player2(object):
    def __init__(self, turn, mouse):
        self.turn = turn
        self.mouse = mouse

    def draw(self, mouse):
        if self.turn == 1:
            for j in range(9):
                if pygame.Rect.collidepoint(B[j], mouse[0], mouse[1]):
                    if lookup_table[j] == 'E':
                        lookup_table[j] = 'O'
                        self.turn = 0
                        X_player.turn = 1


# storing the keys to find whether won or not
win = [0, 0, 0]


# creating a function for showing the image to screen
def redraw_game_window():
    screen.blit(background, (0, 0))
    screen.blit(Boxes, (0, 0))
    X_player.draw(mouse_pos)
    O_player.draw(mouse_pos)
    for k in range(9):
        if lookup_table[k] == 'X':
            screen.blit(X, loc[k])
        elif lookup_table[k] == 'O':
            screen.blit(O, loc[k])

    if X_player.turn == 1:
        screen.blit(text_player1, text_player1_rect)
    if O_player.turn == 1:
        screen.blit(text_player2, text_player2_rect)

    if win[0] == 1:
        screen.blit(text_winner1, text_winner1_rect)
    elif win[1] == 1:
        screen.blit(text_winner2, text_winner2_rect)

    pygame.display.update()


# creating a function for printing the image to screen in the winner screen
def redraw_emote_window():
    screen.blit(bge, (0, 0))
    if win[0] == 1:
        screen.blit(text_winner1, text_winner1_rect)
    elif win[1] == 1:
        screen.blit(text_winner2, text_winner2_rect)
    elif win[2] == 1:
        screen.blit(text_tied, text_tied_rect)
    pygame.display.update()


# creating the texts
text_winner1 = font.render("!Winner : Player 1!", True, [0, 128, 0], [0, 0, 100])
text_winner1_rect = text_winner1.get_rect()
text_winner1_rect.center = (screen_width//2, screen_height//2)
text_winner2 = font.render("!Winner : Player 2!", True, [0, 128, 0], [0, 0, 200])
text_winner2_rect = text_winner1.get_rect()
text_winner2_rect.center = (screen_width//2, screen_height//2)
text_tied = font.render("!Tied!", True, [255, 255, 0], [0, 0, 100])
text_tied_rect = text_tied.get_rect()
text_tied_rect.center = (screen_width//2, screen_height//2)


# creating a function to find the match is completed or not
def check_win(lookup, w):
    if lookup[0] == lookup[1] and lookup[1] == lookup[2]:
        if lookup[0] == 'X':
            w[0] = 1
            w[1] = 0
            print('1')
        elif lookup[0] == 'O':
            w[0] = 0
            w[1] = 1
            print('2')
    elif lookup[3] == lookup[4] and lookup[4] == lookup[5]:
        if lookup[4] == 'X':
            w[0] = 1
            w[1] = 0
            print('3')
        elif lookup[4] == 'O':
            w[0] = 0
            w[1] = 1
            print('4')
    elif lookup[6] == lookup[7] and lookup[7] == lookup[8]:
        if lookup[7] == 'X':
            w[0] = 1
            w[1] = 0
            print('5')
        elif lookup[7] == 'O':
            w[0] = 0
            w[1] = 1
            print('6')
    elif lookup[0] == lookup[3] and lookup[3] == lookup[6]:
        if lookup[0] == 'X':
            w[0] = 1
            w[1] = 0
            print('7')
        elif lookup[0] == 'O':
            w[0] = 0
            w[1] = 1
            print('8')
    elif lookup[1] == lookup[4] and lookup[4] == lookup[7]:
        if lookup[4] == 'X':
            w[0] = 1
            w[1] = 0
            print('9')
        elif lookup[4] == 'O':
            w[0] = 0
            w[1] = 1
            print('10')
    elif lookup[2] == lookup[8] and lookup[8] == lookup[5]:
        if lookup[2] == 'X':
            w[0] = 1
            w[1] = 0
            print('11')
        elif lookup[2] == 'O':
            w[0] = 0
            w[1] = 1
            print('12')
    elif lookup[0] == lookup[4] and lookup[4] == lookup[8]:
        if lookup[4] == 'X':
            w[0] = 1
            w[1] = 0
            print('13')
        elif lookup[4] == 'O':
            w[0] = 0
            w[1] = 1
            print('14')
    elif lookup[2] == lookup[4] and lookup[4] == lookup[6]:
        if lookup[4] == 'X':
            w[0] = 1
            w[1] = 0
            print('15')
        elif lookup[4] == 'O':
            w[0] = 0
            w[1] = 1
            print('16')
    else:
        flag = 0
        for t in range(9):
            if lookup[t] != 'E':
                flag += 1
        if flag == 9:
            w[2] = 1

# creating and initialising the variables
mouse_pos = (100, 750)
running = True
running_emote = False
clock = pygame.time.Clock()
X_player = player1(1, mouse_pos)
O_player = player2(0, mouse_pos)

# main loop
while running:
    clock.tick(9)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
    check_win(lookup_table, win)
    if win[0] == 1 or win[1] == 1 or win[2] == 1:
        running = False
        running_emote = True

    redraw_game_window()


# loop for the showing the winner
while running_emote:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_emote = False
            

    redraw_emote_window()

pygame.quit()

