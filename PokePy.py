import pygame

########### INITIATE ###########

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('PokePy')


########### ANTI REPETITION ###########

def img(name):
    return pygame.image.load(name)


def scale(name, resolution):
    return pygame.transform.scale(name, resolution)


########### BUTTONS ###########

fight_b = (425, 468)
pokemon_b = (425, 528)
bag_b = (611, 468)
run_b = (611, 528)
upper_b = 468
bottom_b = 528
left_b = 425
right_b = 611


attak1_b = (45, 450)
attak2_b = (281, 450)
attak3_b = (45, 510 )
attak4_b = (281, 510)
left_a_b = 15
right_a_b = 251
upper_a_b = 450
bottom_a_b = 510


########### TEXT MESSAGES ###########





########### BACKGROUND ELEMENTS ###########

battle = img('./InterfaceSprites/fgt_background.png')
txt_bar = img('./InterfaceSprites/text_bar.png')
fgt_options = img('./InterfaceSprites/fgt_options.png')
arrow = img('./InterfaceSprites/arrow.png')
atk_bar = img('./InterfaceSprites/pp_bar.png')

########### SCALE ADJUSTMENTS ###########

battle = scale(battle, (800, 420))
txt_bar = scale(txt_bar, (800, 180))
fgt_options = scale(fgt_options, (400, 180))
arrow = scale(arrow, (20, 38))
atk_bar = scale(atk_bar, (800, 180))

########### DRAW ###########


def write_text(ttf, size, text, x, y, color):

    pygame.font.init()
    font = pygame.font.Font(ttf, size)
    text_object = font.render(text, True, (color))
    textRect = text_object.get_rect()
    textRect.topleft = (x, y)
    win.blit(text_object, textRect)

########### WINDOW ###########

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def returnWinSize(self):
        return (self.width, self.height)


w = Window(800, 600)
win = pygame.display.set_mode(w.returnWinSize())

bs = True


########### ARROW ###########

class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        win.blit(arrow, (self.x, self.y))

    def moveBO(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.x == left_b:
            self.x += 186
        if pressed[pygame.K_LEFT] and self.x == right_b:
            self.x -= 186
        if pressed[pygame.K_UP] and self.y == bottom_b:
            self.y -= 60
        if pressed[pygame.K_DOWN] and self.y == upper_b:
            self.y += 60

    def moveAO(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and self.x == left_a_b:
            self.x += 236
        if pressed[pygame.K_LEFT] and self.x == right_a_b:
            self.x -= 236
        if pressed[pygame.K_UP] and self.y == bottom_a_b:
            self.y -= 60
        if pressed[pygame.K_DOWN] and self.y == upper_a_b:
            self.y += 60

def select():

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RETURN] and (battle_arrow.x, battle_arrow.y) == fight_b:
        while True:
            fight()
            if fight() == False:
                break


battle_arrow = Arrow(left_b, upper_b)
attak_arrow = Arrow(15, 450)

def battleScreen():

    win.blit(battle, (0, 0))
    win.blit(txt_bar, (0, 420))
    win.blit(fgt_options, (400, 420))

    battle_arrow.draw()
    battle_arrow.moveBO()
    select()
    pygame.display.update()


def fight():

    win.blit(battle, (0, 0))
    win.blit(atk_bar, (0, 420))

    write_text('./Font/joystix monospace.ttf', 20, 'passa zap', 45, 450, (0,0,0))
    write_text('./Font/joystix monospace.ttf', 20, 'quick attack', 281, 450, (0,0,0))
    write_text('./Font/joystix monospace.ttf', 20, 'thunder wave', 45, 510, (0,0,0))
    write_text('./Font/joystix monospace.ttf', 20, 'bite', 281, 510, (0,0,0))

    print(attak_arrow.x)
    print(attak_arrow.y)

    attak_arrow.draw()
    attak_arrow.moveAO()

    pygame.display.update()


run = True

while run:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    battleScreen()


