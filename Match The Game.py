import pygame
pygame.init()
WIDTH=800
HEIGHT=800
TITLE="Match The Game"
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

candycrush=pygame.image.load("candycrush.jpg")
ludo=pygame.image.load("Ludo.png")
subwaysufers=pygame.image.load("subwaysurfers.png")
tempilrun=pygame.image.load("tempilrun.png")


class Game(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=pygame.transform.scale(image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
cc=Game(2002,800,candycrush)
l=Game(200,600,ludo)
ss=Game(200,400,subwaysufers)
tr=Game(200,200,tempilrun)
sprites=pygame.sprite.Group()
sprites.add(cc)
sprites.add(l)
sprites.add(ss)
sprites.add(tr)



screen.fill("White")
run=True    
while run==True:
    screen.blit(candycrush,(200,0))
    screen.blit(ludo,(200,200))
    screen.blit(subwaysufers,(200,600))
    screen.blit(tempilrun,(200,400))
    font=pygame.font.SysFont("Arial",50)
    text=font.render("candycrush",True,"black")
    screen.blit(text,(500,400))

    font=pygame.font.SysFont("Arial",50)
    text=font.render("templerun",True,"black")
    screen.blit(text,(500,600))

    font=pygame.font.SysFont("Arial",50)
    text=font.render("ludo",True,"black")
    screen.blit(text,(500,0))

    font=pygame.font.SysFont("Arial",50)
    text=font.render("subwaysurfers",True,"black")
    screen.blit(text,(500,200))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            

        if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,"black",pos,pos2,10)

        

       

        







    pygame.display.update()