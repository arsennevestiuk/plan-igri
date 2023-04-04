import pygame
import time
 
pygame.init()
 
clock = pygame.time.Clock()
n1 = ("1")
red = (255,0,0)
r = 0
coins = 0
w = 800
h = 600
white = (255, 255, 255)
black = (0, 0, 0)
bl = (173, 216, 230)
giga = (150,30,40)
fdmgoi = (0,0,0)
 
Display = pygame.display.set_mode((w,h))
pygame.display.set_caption("Клукер")
 
def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)
 
def autominer():
    global coins
    global r
    time.sleep(0.1)
    coins = coins + r
 
 
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    Display.blit(text, textRect)
 
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
 
 
def main_loop():
    global clock
    global r
    global ver
    global color1
    global color2
    global color3
    mong = 1
    cost = 50
    cost2 = 50
    global coins
    game = True
    while game:
        if game: 
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos >= (350, 0):
                    if mopos <= (450, 0):
                        coins += mong
 
                if mopos <= (800, 0):
                    if mopos >= (600, 0):
                        if coins >= cost:
                            coins = coins - cost
                            cost = cost * 1.5
                            mong = mong * 1.1
                            cost = round(cost, 0)
 
                if mopos >= (50, 0):
                    if mopos <= (245, 0):
                        if coins >= cost2:
                            coins = coins - cost2
                            cost2 = cost2 * 1.5
                            r = r + 0.5
                            cost2 = round(cost2, 0)
                   
                    


                if coins >= 1000000:
                    print("WIN")
                    game = False
 
  

        Display.fill(bl)
        DrawText("Клікер", black, bl, 400, 50, 50)
        DrawText("Твій рівень: " + str(n1), black, bl, 100,100,20)
        DrawText("Баланс: " + str(f'{coins:.2f}'), black, bl, 100, 200, 30)
        DrawText("улутшіті клукер " + str(cost), black,giga , 700, 300, 20)
        DrawText("авто клікер " + str(cost2), black,giga , 150, 350, 35)
        rectangle(Display, white, 50, 400, 200, 100)
        circle(Display,black , 400, 260, 40)
        rectangle(Display, white, 600, 320, 200, 100)
        pygame.display.update()
        clock.tick(60)
 
 
main_loop()
pygame.quit()
quit()
