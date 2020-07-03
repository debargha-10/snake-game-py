import pygame
import time
import random

pygame.init()
screenX=400
screenY=400
startX=screenX//2
startY=screenY//2
step=10

dis=pygame.display.set_mode((screenX,screenY))
gamerunning=True
gamepaused=False
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
snake=[]
snake.append([startX,startY])

clock = pygame.time.Clock()
score=0
def getfood():
    foodX=int(round(random.randrange(0, screenX-step)/10.0)*10.0)
    foodY=int(round(random.randrange(0, screenX-step)/10.0)*10.0)
    return [foodX,foodY,step,step]

def dispsnake():
    for i in snake:
        pygame.draw.rect(dis,black,[i[0],i[1],step,step])

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg, color,screenPos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, screenPos)
l=[]
l=getfood()
while gamerunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerunning=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake[0][0]=snake[0][0]-step
            elif event.key == pygame.K_RIGHT:
                snake[0][0]=snake[0][0]+step    
            elif event.key == pygame.K_UP:
                snake[0][1]=snake[0][1]-step
            elif event.key == pygame.K_DOWN:
                snake[0][1]=snake[0][1]+step
            elif event.key == pygame.K_ESCAPE:
                gamepaused=not(gamepaused)
            elif event.key == pygame.K_q and gamepaused:
                quit()
 
    if snake[0][0]>screenX-step:
        snake[0][0]=0
        
    elif snake[0][0]<0:
        snake[0][0]=snake[0][0]+screenX
    if snake[0][1]>screenY-step:
        snake[0][1]=0
    elif snake[0][1]<0:
        snake[0][1]=snake[0][1]+screenY
    if gamepaused==False:
        dis.fill(white)
        
        if snake[0][0]==l[0] and snake[0][1]==l[1]:
            score=score+10
            l=getfood()
            print(score)
        
        dispsnake()
        
        pygame.draw.rect(dis,blue,l)
    else:
        dis.fill(white)
        message("Game Paused", red,[screenX // 3, screenY // 3])
        message("Press ESC to resume",red,[screenX // 3-50, screenY // 3+25])
        message("Press Q to quit",red,[screenX // 3-20, screenY // 3+50])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
