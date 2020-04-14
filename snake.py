import pygame, random

class Snake():
    def __init__(self,sc):
        self.parts = [[25,25]]
        self.sc = sc
    def move(self,motion):
        global INGAME
        new_parts = []
        for i in range(len(self.parts)):
            new_parts.append([1,1])
            
        if motion == LEFT:
            new_parts[0][0] = self.parts[0][0] - 1
            new_parts[0][1] = self.parts[0][1]
            if new_parts[0][0] < 0:
                INGAME = False
        if motion == RIGHT:
            new_parts[0][0] = self.parts[0][0] + 1
            new_parts[0][1] = self.parts[0][1]
            if new_parts[0][0] > 49:
                INGAME = False
        if motion == DOWN:
            new_parts[0][1] = self.parts[0][1] + 1
            new_parts[0][0] = self.parts[0][0]
            if new_parts[0][1] > 49:
                INGAME = False
        if motion == UP:
            new_parts[0][1] = self.parts[0][1] - 1
            new_parts[0][0] = self.parts[0][0]
            if new_parts[0][1] < 0:
                INGAME = False
        for i in range(1, len(self.parts)):
            new_parts[i] = self.parts[i-1] 
        self.parts = new_parts
    def draw(self):
        for  i in range(len(self.parts)):
            pygame.draw.rect(self.sc, BLACK, (self.parts[i][0]*10, self.parts[i][1]*10, 10, 10))
    def add(self):
        self.parts.append(self.parts[-1])
            
 
FPS = 30
W = 500  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
GREEN = (127, 255, 0)
BLACK = (0,0,0)
RIGHT = "right"
LEFT = "left"
STOP = "stop"
UP = "up"
DOWN = "down"
INGAME = True
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
snake = Snake(sc)


f1 = pygame.font.Font(None, 36)
text1 = f1.render('YOU LOSE', 1, (180, 0, 0))
 
f2 = pygame.font.SysFont('serif', 48)
text2 = f2.render("Press any key to restart", 0, (0, 180, 0))

f3 = pygame.font.Font(None, 10)
text3 = f1.render('0', 1, (180, 0, 0))

motion = STOP

FOOD = [random.randint(1, 48),random.randint(1, 48)]
while True:
    sc.fill(WHITE)
 
 

 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and motion != RIGHT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT and motion != LEFT:
                motion = RIGHT
            elif i.key == pygame.K_UP and motion != DOWN:
                motion = UP
            elif i.key == pygame.K_DOWN and motion != UP:
                motion = DOWN
            
    snake.draw()
    sc.blit(text3, (10, 10))
    pygame.draw.rect(sc, GREEN, (FOOD[0]*10, FOOD[1]*10, 10, 10))
    pygame.display.update()

 
    if motion == LEFT:
        snake.move(LEFT)
    elif motion == RIGHT:
        snake.move(RIGHT)
    elif motion == UP:
        snake.move(UP)
    elif motion == DOWN:
        snake.move(DOWN)
    for i in range(1,len(snake.parts)):
        if snake.parts[i] == snake.parts[0]:
            INGAME = False
    text3 = f1.render(str(len(snake.parts)), 1, (180, 0, 0))
    if FOOD == snake.parts[0]:
        snake.add()
        FOOD = [random.randint(1, 50),random.randint(1, 50)]
    while INGAME == False:
        sc.blit(text1, (10, 50))
        sc.blit(text2, (10, 100))
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif i.type == pygame.KEYDOWN:
                snake = Snake(sc)
                INGAME = True
                motion = STOP
        clock.tick(100)
    clock.tick(FPS)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()