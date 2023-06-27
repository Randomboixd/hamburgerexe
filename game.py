import pygame
import os
import random


pygame.init()
os.system("cls")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hamburger.exe")
spikeSprite = pygame.image.load("spike.png")
logo = pygame.image.load("burgir.png")
toiletSprite = pygame.image.load("toilet.png")
cheseburgerSprite = pygame.image.load("cheeseburger.png")
pygame.display.set_icon(logo)
del logo
GFont = pygame.font.SysFont("Comic Sans MS", 30)
GFont_smaller = pygame.font.SysFont("Comic Sans MS", 20)
GFont_large = pygame.font.SysFont("Comic Sans MS", 40)
fontcenter = (200 , 20)
fontbottom = (250, 500)
burgerstat = (100, 10)
colorcodes = [(102,17,0), (128,64,0), (102,102,0), (85,128,0), (42,128,0), (0,128,64), (0,128,128), (0,85,128), (42,0,128), (85,0,128), (128,0,106)]
backroundcolor = random.choice(colorcodes)

user = os.getlogin()


PlayerIcon = pygame.image.load("Player.png")
PlayerX,PlayerY = 400, 300
MovingConstantX = 0
MovingConstantY = 0

cheseburgerloc = (random.randint(200, 800), random.randint(100, 600))
cheseburgerstouched = 0

toiletSpeed = 0.3
toiletMeter = 0

moveSpeed = 1

StartupFrames = 0

toilettakechance = 960
ToiletX,ToiletY = 500,300
ToiletMovingConstantX = 0
ToiletMovingConstantY = 0

GameOver = False

reaction = GFont_smaller.render("Event: - nothing -", False, (255,255,255))

spikes = []

def renderPlayer(xcoord,ycoord):
    player = screen.blit(PlayerIcon, (xcoord,ycoord))
    return player

def renderCheseburger(xcoord,ycoord):
    ches = screen.blit(cheseburgerSprite, (xcoord,ycoord))
    return ches

def renderToilet(xcoord,ycoord):
    toilet = screen.blit(toiletSprite, (xcoord,ycoord))
    return toilet

def tutorialscreen():
    if StartupFrames < 600:
        a = GFont.render(f"Welcome to hamburger.exe {user}!", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 900:
        a = GFont.render("Don't ask why im here.", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 1800:
        a = GFont.render("You must consume the hamburgers!", False, (255,255,255))
        screen.blit(a, fontcenter)
    elif StartupFrames < 2900:
        a = GFont_smaller.render("Or death will be your only choice! now GO!", False, (255,255,255))
        screen.blit(a, fontcenter)

def GameOverScreen():
    gameoverscreentitle = GFont_large.render("Game over.", False, (255,0,0))
    screen.blit(gameoverscreentitle, (30, 300))

def renderSpikes():
    s = []
    for spike in spikes:
        s.append(screen.blit(spikeSprite, spike))
    return s

runs = True
while runs:
    screen.fill(backroundcolor)
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

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w or events.key == pygame.K_s or events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                MovingConstantY = 0

            if events.key == pygame.K_a or events.key == pygame.K_d or events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                MovingConstantX = 0

        if events.type == pygame.KEYDOWN:
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

        

        

        if events.type == pygame.KEYDOWN and events.key == pygame.K_e and ches.colliderect(player) and GameOver != True:
            cheseburgerloc = (random.randint(200, 500), random.randint(100, 500))
            cheseburgerstouched += 1
        if events.type == pygame.KEYDOWN and events.key == pygame.K_e and toilet.colliderect(player) and toiletMeter > 8 and GameOver != True:
            toiletMeter = 0


    PlayerY += MovingConstantY
    PlayerX += MovingConstantX
    
    if GameOver != True:
        if PlayerY > 600 - 64:
            PlayerY = 600 - 64
        elif PlayerY < 0:
            PlayerY = 0

        if PlayerX > 800 - 64:
            PlayerX = 800 - 64
        elif PlayerX < 0:
            PlayerX = 0

    if GameOver != True:
        player = renderPlayer(PlayerX,PlayerY)
    else:
        player = renderPlayer(99999999,9999999)
    tutorialscreen()
    spikelocs = renderSpikes()
    if spikelocs == []:
        pass
    else:
        for x in spikelocs:
            if x.colliderect(player):
                GameOver = True
                GameOverScreen()

    ches = renderCheseburger(cheseburgerloc[0], cheseburgerloc[1])

    toiletmovetype = random.choice(["onward", "left", "right", "backward","onward", "left", "right", "backward","onward", "left", "right", "backward","onward", "left", "right", "backward"])
    movelength = [0, 0.5, 0.6, 0.7]
    if toiletmovetype == "onward":
        howmuch = random.choice(movelength)
        ToiletMovingConstantY += howmuch
    elif toiletmovetype == "left":
        howmuch = random.choice(movelength)
        ToiletMovingConstantX -= howmuch
    elif toiletmovetype == "right":
        howmuch = random.choice(movelength)
        ToiletMovingConstantX += howmuch
    elif toiletmovetype == "backward":
        howmuch = random.choice(movelength)
        ToiletMovingConstantY -= howmuch

    ToiletY += ToiletMovingConstantY
    ToiletX += ToiletMovingConstantX
    

    if ToiletY > 600 - 64:
        ToiletY = 600 - 64
    elif ToiletY < 0:
        ToiletY = 0

    if ToiletX > 800 - 64:
        ToiletX = 800 - 64
    elif ToiletX < 0:
        ToiletX = 0

    toilet = renderToilet(ToiletX, ToiletY)
    if ches.colliderect(player):
        sup = GFont_smaller.render("Press E to pick up cheseburger!", False, (255,255,255))
        screen.blit(sup, fontbottom)

    if toilet.colliderect(player) and toiletMeter > 8:
        sup = GFont_smaller.render("Press E to take a dump", False, (255,255,255))
        screen.blit(sup, fontbottom)

    stat = GFont_smaller.render(f"Hamburgers eaten: {str(cheseburgerstouched)}", False, (255,255,255))
    screen.blit(stat, burgerstat)
    pygame.display.set_caption(f"Hamburger.exe - {str(cheseburgerstouched)} chesburgers eaten")

    toiletstat = GFont_smaller.render(f"Your toilet meter: {str(toiletMeter)}/10", False, (255,255,255))
    toiletwarning = GFont_smaller.render("Going over 10 is a game over!", False, (255,0,0))
    if GameOver != True:
        screen.blit(toiletstat, (300, 530))
        screen.blit(toiletwarning, (300, 550))

    if toiletMeter > 10:
        GameOver = True
        GameOverScreen()

    if random.randint(0, 999) == 69:

        event = random.choice(["spikes", "rnggod", "rnggodfail", "speedup", "speeddown"])
        if event == "spikes":
            spikes.append((random.randint(0, 800-64), random.randint(0, 600-64)))
            reaction = GFont_smaller.render(f"Event: Spike planted!", False, (255,255,255))
        elif event == "rnggod":
            ups = random.randint(0, 200)
            toilettakechance += ups
            reaction = GFont_smaller.render(f"Event: You made a deal with the RNG Gods!", False, (255,255,255))
        elif event == "rnggodfail":
            downs = random.randint(0, 200)
            toilettakechance -= downs
            reaction = GFont_smaller.render(f"Event: The RNG Gods hate you", False, (255,255,255))
        elif event == "speedup":
            by = [0.1,0.2,0.3,0.4,0.5,0.6]
            moveSpeed += random.choice(by)
            reaction = GFont_smaller.render(f"Event: Im sanic! Sanic the hedgehog!", False, (255,255,255))
        elif event == "speeddown":
            by = [0.1,0.2]
            moveSpeed -= random.choice(by)
            reaction = GFont_smaller.render(f"Event: Snail moment", False, (255,255,255))
        
    screen.blit(reaction, (400, 10))
    version = GFont_smaller.render(f"Build V0.1, RandomboiXD", False, (255,0,0))
    screen.blit(version, (1,1))
    pygame.display.update()
    dice = random.randint(0, toilettakechance)
    if dice == 69:
        toiletMeter += 1

    


    StartupFrames += 1
    