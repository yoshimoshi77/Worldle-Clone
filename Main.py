import pygame
import sys
from words import get_random_word
from words import get_possible_words_list
import time as t

pygame.init()
clock = pygame.time.Clock()
FPS = 999999999999
font = pygame.font.SysFont("bookmanoldstyle",50)

class game:
    def __init__(self):
        self.grid_y = 75
        self.screen_height = 650
        self.screen_width = 600  
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.word_list = []
        self.word_color_list = []
        self.background_color = (255,255,255)	
        self.title_font = pygame.font.SysFont("bookmanoldstyle",50)
        self.font = pygame.font.SysFont("bookmanoldstyle",14)
        self.grid_font = pygame.font.SysFont("arialblack",30)
        self.word = get_random_word()
        self.possible_words = get_possible_words_list()
        self.current_guess = ""
        self.letters = {
            "Q" : 0,
            "W" : 0,
            "E" : 0,
            "R" : 0,
            "T" : 0,
            "Y" : 0,
            "U" : 0,
            "I" : 0,
            "O" : 0,
            "P" : 0,
            "A" : 0,
            "S" : 0,
            "D" : 0,
            "F" : 0,
            "G" : 0,
            "H" : 0,
            "J" : 0,
            "K" : 0,
            "L" : 0,
            "Z" : 0,
            "X" : 0,
            "C" : 0,
            "V" : 0,
            "B" : 0,
            "N" : 0,
            "M" : 0,  
        }

        self.box_size = 50

    def write_title(self):
        title_text = self.title_font.render("WORDLE", True, (0,0,0))
        title_rect = title_text.get_rect(center = (self.screen_width/2 , 30))
        self.screen.blit(title_text,title_rect)

    def draw_grid(self):
        x_pos = 150
        y_pos = start_y = 75
        gray = (211,211,211)
        border = 3

        for row in range(1,6):
            for column in range(1,7):
                gray_rect = pygame.Rect(x_pos,y_pos,self.box_size,self.box_size)
                pygame.draw.rect(self.screen,gray,gray_rect)
                white_rect = pygame.Rect(x_pos + border,y_pos + border,self.box_size - border * 2,self.box_size - border * 2)
                pygame.draw.rect(self.screen,self.background_color,white_rect)
                y_pos += self.box_size + 10
            y_pos = start_y
            x_pos += self.box_size + 10

        x_pos = 175
        y_pos =  self.grid_y + 25

        for letter in self.current_guess:
            letter_img = self.grid_font.render(letter.upper(),True,(0,0,0))
            letter_rect = letter_img.get_rect(center = (x_pos,y_pos))
            self.screen.blit(letter_img,letter_rect)
            x_pos += 60

    def close_window(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw_keyboard(self):
        letter_count = 0
        x_pos = start_pos = 100
        y_pos = 450
        for letter in self.letters:
            if letter_count == 10 or letter_count == 19:
                start_pos += 30
                x_pos = start_pos
                y_pos += 50

            if self.letters[letter] == 0:
                color = (210,210,210)
            elif self.letters[letter] == -1:
                color = (128,128,128)
            elif self.letters[letter] == 1:
                color = (0,128,0)
            else:
                color  = (204,204,0)

            text_color = (0,0,0)

            letter_box = pygame.Rect(x_pos - 5,y_pos - 5, 35,45)
            letter_img = self.font.render(letter,True,text_color)
            letter_rect = letter_img.get_rect(topleft = (x_pos,y_pos))
            letter_rect.center = letter_box.center
            pygame.draw.rect(self.screen,color,letter_box,50,2)
            self.screen.blit(letter_img,letter_rect)
            x_pos += 40


            letter_count += 1

    def draw_screen(self):
        self.screen.fill(self.background_color)
        self.draw_grid()
        self.write_title()
        self.draw_keyboard() 

    def keyboard_input(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_a]:
                        self.current_guess = self.current_guess + "a"
                    elif keys[pygame.K_b]:
                        self.current_guess = self.current_guess + "b"
                    elif keys[pygame.K_c]:
                        self.current_guess = self.current_guess + "c"
                    elif keys[pygame.K_d]:
                        self.current_guess = self.current_guess + "d"
                    elif keys[pygame.K_e]:
                        self.current_guess = self.current_guess + "e"
                    elif keys[pygame.K_f]:
                        self.current_guess = self.current_guess + "f"
                    elif keys[pygame.K_g]:
                        self.current_guess = self.current_guess + "g"
                    elif keys[pygame.K_h]:
                        self.current_guess = self.current_guess + "h"
                    elif keys[pygame.K_i]:
                        self.current_guess = self.current_guess + "i"
                    elif keys[pygame.K_j]:
                        self.current_guess = self.current_guess + "j"
                    elif keys[pygame.K_k]:
                        self.current_guess = self.current_guess + "k"
                    elif keys[pygame.K_l]:
                        self.current_guess = self.current_guess + "l"
                    elif keys[pygame.K_m]:
                        self.current_guess = self.current_guess + "m"
                    elif keys[pygame.K_n]:
                        self.current_guess = self.current_guess + "n"
                    elif keys[pygame.K_o]:
                        self.current_guess = self.current_guess + "o"
                    elif keys[pygame.K_p]:
                        self.current_guess = self.current_guess + "p"
                    elif keys[pygame.K_q]:
                        self.current_guess = self.current_guess + "q"
                    elif keys[pygame.K_r]:
                        self.current_guess = self.current_guess + "r"
                    elif keys[pygame.K_s]:
                        self.current_guess = self.current_guess + "s"
                    elif keys[pygame.K_t]:
                        self.current_guess = self.current_guess + "t"
                    elif keys[pygame.K_u]:
                        self.current_guess = self.current_guess + "u"
                    elif keys[pygame.K_v]:
                        self.current_guess = self.current_guess + "v"
                    elif keys[pygame.K_w]:
                        self.current_guess = self.current_guess + "w"
                    elif keys[pygame.K_x]:
                        self.current_guess = self.current_guess + "x"
                    elif keys[pygame.K_y]:
                        self.current_guess = self.current_guess + "y"
                    elif keys[pygame.K_z]:
                        self.current_guess = self.current_guess + "z"    

                    if keys[pygame.K_BACKSPACE]:
                        new_str = ""
                        for i in range(len(self.current_guess) - 1):
                            new_str = new_str + self.current_guess[i]
                        self.current_guess = new_str

                    if keys[pygame.K_RETURN] and len(self.current_guess) == 5:
                        if self.current_guess in self.possible_words:       
                            self.word_list.append(self.current_guess)
                            self.analyse_word()
                            self.current_guess = ""

                    if len(self.current_guess) > 5:
                        new_str = ""
                        for i in range(5):
                            new_str = new_str + self.current_guess[i]
                        self.current_guess = new_str
            
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    

    def analyse_word(self):
        #analyse the word and then add the grid boxes
        guess = self.current_guess
        correct_word = self.word
        letter_index = 0
        x_pos = 150
        y_pos = self.grid_y
        self.grid_y += 60
        for letter in guess:
            gray = True
            letter = letter.upper()
            for correct_letter in correct_word:
                correct_letter = correct_letter.upper()
                if letter == correct_letter:
                    if guess[letter_index].upper() == correct_word[letter_index].upper():
                        self.letters[letter] = 1
                        grid_list.append(grid(x_pos,y_pos,50,(0,128,0),letter.upper(),self.grid_font))
                        gray = False
                        

                    else:
                        gray = False
                        if self.letters[letter] == 0:
                            self.letters[letter] = 0.5

                        grid_list.append(grid(x_pos,y_pos,50,(204,204,0),letter.upper(),self.grid_font))
            if gray:
                self.letters[letter] = -1
                grid_list.append(grid(x_pos,y_pos,50,(128,128,128),letter.upper(),self.grid_font))

            letter_index += 1
            x_pos += 60

    def end(self):
        img = self.font.render(self.word.upper(),True,(255,255,255))
        rect = pygame.Rect(self.screen_width/2 - img.get_width()/2 - 10, 100,img.get_width() + 20,img.get_height() + 20 )
        img_rect = img.get_rect(center = rect.center)
        pygame.draw.rect(self.screen,(0,0,0),rect,100,2)
        self.screen.blit(img,img_rect)
        pygame.display.update()
        t.sleep(5)
        pygame.quit()
        sys.exit()
        
class grid:
    def __init__(self,x,y,size,color,letter,font):
        self.rect = pygame.Rect(x,y,size,size)
        self.color = color
        self.x = x
        self.y = y
        self.letter_img = font.render(letter,True,(255,255,255))
        self.letter_rect = self.letter_img.get_rect(center = self.rect.center)
        
    def draw(self,screen):
        self.rect.x = self.x
        self.rect.y = self.y
        self.letter_rect.center = self.rect.center
        pygame.draw.rect(screen,self.color,self.rect)
        screen.blit(self.letter_img,self.letter_rect)


Wordle = game()

grid_list = []
while True:
    green = 0
    for letter in Wordle.letters:
        if Wordle.letters[letter] == 1:
            green += 1
    
    if green >= 5:
        Wordle.end()
    Wordle.draw_screen()
    Wordle.keyboard_input()
    for square in grid_list:
        square.draw(Wordle.screen)
    Wordle.close_window()
    if len(Wordle.word_list) > 5:
        Wordle.end()
    clock.tick(FPS)
    pygame.display.update()