import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.update()
gamerun = True
gameover = False
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 255, 150)
resu = "0"
urchce = "0"
mnh = ["Ножницы", "Камень", "Бумага"]

while gamerun:
    pygame.draw.rect(screen, color1, (50, 100, 300, 400))
    pygame.draw.rect(screen, color2, (450, 100, 300, 400))
    pygame.draw.rect(screen, color3, (850, 100, 300, 400))
    pygame.draw.rect(screen, color4, (500, 550, 200, 100))
    pygame.display.update()
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            gamerun = False
            pygame.quit()
        elif event1.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 50 < x < 350 and 100 < y < 500:
                color1 = (150, 150, 150)
                color2 = (0, 255, 0)
                color3 = (0, 0, 255)
                urchce = "Ножницы"
                cmchce = random.choice(mnh)
                if cmchce == "Ножницы":
                    resu = "Ничья"
                elif cmchce == "Бумага":
                    resu = "Выиграли"
                else:
                    resu = "Проиграли"
            if 450 < x < 750 and 100 < y < 500:
                color1 = (255, 0, 0)
                color2 = (150, 150, 150)
                color3 = (0, 0, 255)
                urchce = "Камень"
                cmchce = random.choice(mnh)
                if cmchce == "Камень":
                    resu = "Ничья"
                elif cmchce == "Ножницы":
                    resu = "Выиграли"
                else:
                    resu = "Проиграли"
            if 850 < x < 1150 and 100 < y < 500:
                color1 = (255, 0, 0)
                color2 = (0, 255, 0)
                color3 = (150, 150, 150)
                urchce = "Бумага"
                cmchce = random.choice(mnh)
                if cmchce == "Бумага":
                    resu = "Ничья"
                elif cmchce == "Камень":
                    resu = "Выиграли"
                else:
                    resu = "Проиграли"
            if 500 < x < 700 and 550 < y < 650:
                if urchce == "0":
                    print("Вы еще не выбрали")
                else:
                    if resu == "0":
                        pass
                    else:
                        print("ВЫ ВЫБРАЛИ: " + urchce)
                        print("ПК ВЫБРАЛ: " + cmchce)
                        print(resu)
                        color1 = (255, 0, 0)
                        color2 = (0, 255, 0)
                        color3 = (0, 0, 255)
                        color4 = (255, 255, 150)
                        resu = "0"
                        urchce = "0"