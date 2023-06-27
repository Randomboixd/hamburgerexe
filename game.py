import pygame
import os


pygame.init()
os.system("cls")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hamburger.exe")
logo = pygame.image.load("burgir.png")
pygame.display.set_icon(logo)
del logo
GFont = pygame.font.SysFont("Comic Sans MS", 30)
GFont_smaller = pygame.font.SysFont("Comic Sans MS", 20)
fontcenter = (200 , 20)

user = os.getlogin()


PlayerIcon = pygame.image.load("Player.png")
PlayerX,PlayerY = 400, 300
MovingConstantX = 0
MovingConstantY = 0


moveSpeed = 1

StartupFrames = 0

def renderPlayer(xcoord,ycoord):
    screen.blit(PlayerIcon, (xcoord,ycoord))

def tutorialscreen():
    if StartupFrames < 600:
        a = GFont.render(f"Welcome to the game {user}!", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 900:
        a = GFont.render("Don't ask why im here.", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 1500:
        a = GFont.render("You must consume the hamburgers!", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 2000:
        a = GFont_smaller.render("Or death will be your only choice! now GO!", False, (255,255,255))
        screen.blit(a, fontcenter)
    #if StartupFrames => 

runs = True
while runs:
    screen.fill((0,0,0))
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            runs = False
            print("Exiting")
            break
        
        if events.type == pygame.KEYDOWN:
            
            if events.key == pygame.K_w or events.key == pygame.K_UP:
                MovingConstantY -= moveSpeed
            
            if events.key == pygame.K_s or events.key == pygame.K_DOWN:
                MovingConstantY += moveSpeed

            if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
                MovingConstantX += moveSpeed

            if events.key == pygame.K_a or events.key == pygame.K_LEFT:
                MovingConstantX -= moveSpeed

            if events.key == pygame.K_ESCAPE:
                runs = False
                print("Exiting")
                break

            if events.key == pygame.K_f:
                if pygame.display.is_fullscreen() == False:
                    pygame.display.toggle_fullscreen()
                    print("Goin' fullscreen!")
                else:
                    pygame.display.toggle_fullscreen()
                    print("No more fullscreen :(")
        
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w or events.key == pygame.K_s or events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                MovingConstantY = 0

            if events.key == pygame.K_a or events.key == pygame.K_d or events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                MovingConstantX = 0


    PlayerY += MovingConstantY
    PlayerX += MovingConstantX
    
    if PlayerY > 600 - 64:
        PlayerY = 600 - 64
    elif PlayerY < 0:
        PlayerY = 0

    if PlayerX > 800 - 64:
        PlayerX = 800 - 64
    elif PlayerX < 0:
        PlayerX = 0

    renderPlayer(PlayerX,PlayerY)
    tutorialscreen()
    pygame.display.update()
    StartupFrames += 1