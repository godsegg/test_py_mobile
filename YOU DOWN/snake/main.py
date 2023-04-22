import pygame, random

pygame.init()

WIN_WIDTH = 600
WIN_HIGTH = 400
WIN = 720
WIN1 = 1000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (50, 0 ,0)
GREEN = (0, 255, 0)
GREY = (127, 127, 127)
BLUE = (50, 153, 213)
WHITE_BLUE = (50, 255, 255)
YELLOW = (255, 255, 0)

fat = 15
fat_food = 10

'''display'''
screen = pygame.display.set_mode((WIN, WIN1))
pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()
FPS = 10
info = pygame.Surface((800, 30))

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

class Menu:
    def __init__(self, punkts=[400, 350, u'Punkt', (250, 250, 30), (250, 30, 250), (30, 250, 250)]):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0

        while done:
            menu_png = pygame.image.load('FON_MENU.jpg')
            info.fill((WHITE))
            screen.blit(menu_png, (-550, 50))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 500 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                        GAME = False
                        game_close = False
                    elif punkt == 1:
                        tutor()
                    elif punkt == 2:
                        exit()

            screen.blit(info, (0, 0))
            screen.blit(screen, (0, 30))
            pygame.display.flip()




def our_snake(fat, snake_list):
    for x in snake_list:
        pygame.draw.ellipse(screen, GREEN, [x[0], x[1], fat, fat]) #легендарный змей

def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [WIN1 / float(6), WIN / 11])

def message_tutor(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [WIN1 / float(6), WIN / 11])

def tutor():
    Tutor = True
    while Tutor:
        screen.fill(BLACK)
        menu1_png = pygame.image.load('pixil-frame-0 (1).png')
        screen.blit(menu1_png, (100, 120))
        done = False
        message_tutor('НАЖМИ НА МЕНЯ ЧТО БЫ ВЫЙТИ', WHITE_BLUE)
        pygame.display.flip()
        for event in pygame.event.get():
            #print('event.pos:', event.pos)
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] >= 160 and event.pos[1] <= 100 and event.pos[0] <= 560 and event.pos[1] >= 65:
                    Tutor = False
                    done = True

def Food():
    GAME = False
    game_close = False

    x1 = WIN_WIDTH / 2
    y1 = WIN_HIGTH / 2

    x1_change = 0
    y1_change = 0

    snake_List = [] #ДЛИНА ЗМЕЙКИ
    Length_of_snake = 1 #ИЗНАЧАЛЬНАЯ ДЛИНА ЗМЕЙКИ

    foodx = round(random.randrange(0, WIN_WIDTH - fat) / 10.0) * 10.0
    foody = round(random.randrange(0, WIN_WIDTH - fat) / 10.0) * 10.0

    punkts = [(270, 300, u'ИГРАТЬ', (11, 0, 77), (250, 250, 30), 0),
              (275, 350, u'ТУТОР', (11, 0, 77), (250, 250, 30), 1),
              (170, 400, u'КОНСИД С ПОЗОРОМ', (11, 0, 77), (250, 250, 30), 2)]

    Game = Menu(punkts)
    Game.menu()

    while not GAME:
        while game_close == True:
            screen.fill(DARK_RED) #ЦВЕТ ЭКРАНА ПРИ СМЕРТИ
            message("НАЖМИ НА МЕНЯ ЧТО БЫ ВЫЙТИ", WHITE_BLUE) #ЦВЕТ НАДПИСИ ПРИ СМЕРТИ
            #print('event.pos:', event.pos)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if event.pos[0] >= 160 and event.pos[1] <= 100 and event.pos[0] <= 560 and event.pos[1] >= 65:
                        Game.menu()
                        GAME = False
                        game_close = False
                        Food()
                        our_snake()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        Food()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -fat_food
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = fat_food
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -fat_food
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = fat_food
                    x1_change = 0
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] >= 499 and event.pos[1] <= 799 and event.pos[1] >= 199 and x1_change == 0: #ВПРАВО
                    x1_change = fat_food
                    y1_change = 0
                if event.pos[0] >= 0 and event.pos[1] >= 200 and event.pos[0] <= 230 and event.pos[1] <= 799 and x1_change == 0: #ВЛЕВО
                    x1_change = -fat_food
                    y1_change = 0
                if event.pos[0] >= 49 and event.pos[1] >= 800 and event.pos[0] <= 669 and event.pos[1] <= 999 and y1_change == 0:#ВНИЗ
                    y1_change = fat_food
                    x1_change = 0
                if event.pos[0] >= 49 and event.pos[1] <= 199 and event.pos[0] <= 669 and y1_change == 0: #ВВЕРХ
                    y1_change = -fat_food
                    x1_change = 0


        if x1 >= WIN or x1 < 0 or y1 >= WIN1 or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        chery_png = pygame.image.load('FON_GAME.png')
        screen.blit(chery_png, (-550,0))

        pygame.draw.rect(screen, WHITE_BLUE, [foodx, foody, fat_food, fat_food])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[0:-1]:
            if x == snake_Head and Length_of_snake >= 1:
                game_close = True

        our_snake(fat_food, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIN_WIDTH - fat) / 10.0) * 10.0
            foody = round(random.randrange(0, WIN_WIDTH - fat) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

Food()