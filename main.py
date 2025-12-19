import pygame

pygame.init()

dis_width = 800 #Зададим размер игрового поля через две переменные.
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))  #Задаём размер игрового поля.
game_over = False #Переменная которая помогает контролировать - завершена игра или нет

pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Если нажата кнопка закрыть 
            game_over = True # То game_over принимает знаение True
        print(event) #Выводить в терминал все события
        
pygame.quit()
quit()