import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

dis = pygame.display.set_mode((800,600))  #Задаём размер игрового поля.
pygame.display.set_caption('Змейка')

dis_width = 800 #Зададим размер игрового поля через две переменные.
dis_height = 600


background = pygame.image.load('image/background.png')
game_over = False #Переменная которая помогает контролировать - завершена игра или нет
x1 = dis_width/2 # Начальное положение змейки относительно оси Х
y1 = dis_height/2 # Начальное положение змейки относительно оси Y
x1_change = 0 # Пременная которой будет присваиваться значение в зависимости от нажатой клавиши (управление змейкой)
y1_change = 0 # Пременная которой будет присваиваться значение в зависимости от нажатой клавиши (управление змейкой)
clock = pygame.time.Clock()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Если нажата кнопка закрыть 
            game_over = True # То game_over принимает знаение True
        if event.type == pygame.KEYDOWN: #Если нажата любая кнопка 
            if event.key == pygame.K_LEFT: # Если нажата кнопка влево - изменить положение змейка на 10 пикселей
                x1_change = -50
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 50
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -50
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 50
    x1 += x1_change #Записываем новое значение положения змейки по оси х.
    y1 += y1_change #Записываем новое значение положения змейки по оси y.
    dis.blit(background, (0,0))
    
    pygame.draw.rect(dis, black, [x1, y1, 50, 50])
    pygame.display.update()
    clock.tick(15)
        
pygame.quit()
quit()