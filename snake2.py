# Importing Libraries
import pygame
import time
import random

# Colors
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)

# Initial Conditions and Dimensions
pygame.init()
screenX=400
screenY=400
startX=screenX//2
startY=screenY//2
step=10
dis=pygame.display.set_mode((screenX,screenY))
gamerunning=True
gamepaused=False
gameover=False

snake=[]
snake.append([startX,startY])
score=0
flag=0
clock = pygame.time.Clock()

pygame.mixer.music.load('Music.mp3')

# Utility Functions
def getfood():
    foodX=int(round(random.randrange(0, screenX-step)/10.0)*10.0)
    foodY=int(round(random.randrange(0, screenX-step)/10.0)*10.0)
    return [foodX,foodY,step,step]

def dispsnake():
    for i in snake:
        pygame.draw.rect(dis,black,[i[0],i[1],step,step])

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)

def message(msg, color,screenPos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, screenPos)
    
def addbody():
    length=len(snake)
    l=snake[length-1]
    snake.append(l)
    
def movesnake(headX,headY):
    length=len(snake)
    temp=snake[0]
    temp2=[]
    for i in range(1,length):
        temp2=snake[i]
        snake[i]=temp
        temp=temp2
                
    snake[0]=[headX,headY]
    
def collision():
    global gameover
    if snake[0] in snake[1:len(snake)] and len(snake)>=4:
        gameover=True
        

        

def snscore():
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
    
# Game Loop
l=[]
l=getfood()
head=snake[0]
pygame.mixer.music.play(0)
while gamerunning:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gamerunning=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and gameover==False:
                head[0]=head[0]-step
                movesnake(head[0],head[1])
            elif event.key == pygame.K_RIGHT and gameover==False:
                head[0]=head[0]+step    
                movesnake(head[0],head[1])
            elif event.key == pygame.K_UP and gameover==False:
                head[1]=head[1]-step
                movesnake(head[0],head[1])
            elif event.key == pygame.K_DOWN and gameover==False:
                head[1]=head[1]+step
                movesnake(head[0],head[1])
            elif event.key == pygame.K_ESCAPE and gameover==False:
                gamepaused=not(gamepaused)
            if event.key == pygame.K_q and (gamepaused or gameover):
                gamerunning=False
            if event.key == pygame.K_r and gameover:
                gameover=False
                snake=[[startX,startY]]
                score=0
                clock = pygame.time.Clock()
                l=getfood()
                head=snake[0]
                pygame.mixer.music.play(-1)
 
    if head[0]>screenX-step:
        head[0]=0
    elif head[0]<0:
        head[0]=head[0]+screenX
    if head[1]>screenY-step:
        head[1]=0
    elif head[1]<0:
        head[1]=head[1]+screenY
    
    
    if gamepaused==False or gameover== False:
        dis.fill(white)
        
        if snake[0][0]==l[0] and snake[0][1]==l[1]:
            score=score+10
            l=getfood()
            addbody()
        else:
            
            dispsnake()
            snscore()
            pygame.draw.rect(dis,blue,l)
        
    if gamepaused:
        pygame.mixer.music.stop()
        dis.fill(white)
        message("Game Paused", red,[screenX // 3, screenY // 3])
        message("Press ESC to resume",red,[screenX // 3-50, screenY // 3+25])
        message("Press Q to quit",red,[screenX // 3-20, screenY // 3+50])
    collision()
    if gameover:
        pygame.mixer.music.stop()
        dis.fill(white)
        message("Game Over", red,[screenX // 3, screenY // 3])
        message("Press R to restart",red,[screenX // 3-50, screenY // 3+25])
        message("Press Q to quit",red,[screenX // 3-20, screenY // 3+50])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
