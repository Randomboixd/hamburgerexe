"""
License:

Copyright © 2023 RandomboiXD

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import pygame
import os
import random
import base64
import json
import requests
import time


pygame.init()
os.system("cls")

licensetext = """
Copyright © 2023 RandomboiXD

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


def DownloadFiles(): # This function downloads assets from https://rndwebsite.ddns.net/ You can replace the url with your own, just make sure you return bytes.
    if os.path.exists("./HamburgerAssets/") and os.path.exists(f"./HamburgerAssets/burgir.png") and os.path.exists("./HamburgerAssets/cheeseburger.png") and os.path.exists("./HamburgerAssets/Player.png") and os.path.exists("./HamburgerAssets/spike.png") and os.path.exists("./HamburgerAssets/toilet.png") and os.path.exists("./HamburgerAssets/shop.png") and os.path.exists("./HamburgerAssets/coin.png") and os.path.exists("./HamburgerAssets/gear.png") and os.path.exists("./HamburgerAssets/backarrow.png"):
        print("Game assets are present, Starting game!")
    else:
        os.mkdir("./HamburgerAssets/")
        print("Connecting to https://rndwebsite.randomboixd.repl.co/ and downloading assets!")
        burgir = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/burgir")
        cheeseburger = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/cheeseburger")
        time.sleep(2)
        Player = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/Player")
        Spike = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/spike")
        toilet = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/toilet")
        Coin = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/coin")
        time.sleep(2)
        Shop = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/shop")
        gear = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/gear")
        backarrow = requests.get("https://rndwebsite.randomboixd.repl.co/cdn/hamburgerexe/backarrow")

        with open(f"./HamburgerAssets/burgir.png", "xb") as f:
            f.write(burgir.content)

        with open(f"./HamburgerAssets/cheeseburger.png", "xb") as f:
            f.write(cheeseburger.content)

        with open(f"./HamburgerAssets/Player.png", "xb") as f:
            f.write(Player.content)
        
        with open(f"./HamburgerAssets/spike.png", "xb") as f:
            f.write(Spike.content)
        
        with open(f"./HamburgerAssets/toilet.png", "xb") as f:
            f.write(toilet.content)

        with open(f"./HamburgerAssets/coin.png", "xb") as f:
            f.write(Coin.content)
        
        with open(f"./HamburgerAssets/shop.png", "xb") as f:
            f.write(Shop.content)
        
        with open(f"./HamburgerAssets/gear.png", "xb") as f:
            f.write(gear.content)

        with open(f"./HamburgerAssets/backarrow.png", "xb") as f:
            f.write(backarrow.content)

        print("Finished downloading (and writing) files! Starting game!")

DownloadFiles()
print(licensetext) # Print the MIT License

screen = pygame.display.set_mode((800, 600)) # Set the display to 800,600
# Import assets/sprites/whatever

antialias = False

pygame.display.set_caption("Hamburger.exe - Main Menu")
spikeSprite = pygame.image.load("./HamburgerAssets/spike.png")
logo = pygame.image.load("./HamburgerAssets/burgir.png")
toiletSprite = pygame.image.load("./HamburgerAssets/toilet.png")
cheseburgerSprite = pygame.image.load("./HamburgerAssets/cheeseburger.png")
PlayerIcon = pygame.image.load("./HamburgerAssets/Player.png")
CoinSprite = pygame.image.load("./HamburgerAssets/coin.png")
ShopSprite = pygame.image.load("./HamburgerAssets/shop.png")
OptionsSprite = pygame.image.load("./HamburgerAssets/gear.png")
BackArrowSprite = pygame.image.load("./HamburgerAssets/backarrow.png")
pygame.display.set_icon(logo)
del logo

# Add Fonts
GFont = pygame.font.SysFont("Cascadia Code SemiBold", 40)
GFont_smaller = pygame.font.SysFont("Cascadia Code", 30)
GFont_large = pygame.font.SysFont("Cascadia Mono SemiBold", 60)
fontcenter = (200 , 20)
fontbottom = (250, 500)
burgerstat = (1, 40)

# Add a random backround color every time the game starts up
colorcodes = [(102,17,0), (128,64,0), (102,102,0), (85,128,0), (42,128,0), (0,128,64), (0,128,128), (0,85,128), (42,0,128), (85,0,128), (128,0,106)]
backroundcolor = random.choice(colorcodes)

user = os.getlogin() # Get user for tutorial

PlayerX,PlayerY = 400, 300
MovingConstantX = 0
MovingConstantY = 0
controlsInverted = False

cheseburgerloc = (random.randint(200, 800), random.randint(100, 600)) # Generates a random tuple location for the cheeseburger. misspell is intentional
cheseburgerstouched = 0 # How many cheeseburgers were clicked?

toiletSpeed = 0.3 # Speed of toilet. Events change this
toiletMeter = 0 # If this reaches 11 = Game over

moveSpeed = 1 # The Player's movespeed, events change this

StartupFrames = 0 # +1 every frame. Used by tutorial

toilettakechance = 960 # The chance for toiletMeter to go up by one
ToiletX,ToiletY = 500,300
ToiletMovingConstantX = 0
ToiletMovingConstantY = 0

TakesDamageFromSpikes = True

GameOver = False # Is game over?

hasbackround = True

Coins = 0



Randomtitles = ["Now with annoying flies!", "Welcome to the shoppin' channel!", "Are you H A M B U R G E R enough?"]

randomtitle = random.choice(Randomtitles)


reaction = GFont_smaller.render("Event: - nothing -", antialias, (255,255,255))

if os.path.exists("hamburger.records"): # If possible, load the records
    with open("hamburger.records", "r") as f:
        f = json.load(f)
    record = int(base64.b64decode(f["highscore"].encode()).decode()) # Records are encoded in B64
    del f
else:
    record = 0

Saved = False # Used by gameover to prevent it from saving the game EVERY FRAME

spikes = [] # Spike location tuples
coinslocs = []

def renderPlayer(xcoord,ycoord):
    player = screen.blit(PlayerIcon, (xcoord,ycoord))
    return player

def renderCheseburger(xcoord,ycoord):
    ches = screen.blit(cheseburgerSprite, (xcoord,ycoord))
    return ches

def renderToilet(xcoord,ycoord):
    toilet = screen.blit(toiletSprite, (xcoord,ycoord))
    return toilet

def renderShop():
    shop = screen.blit(ShopSprite, (0, 600-64))
    return shop

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

def GameOverScreen(Saved):
    
    if Saved != True: # Not saved? then save it!
        if os.path.exists("./hamburger.records"):
            
            with open("hamburger.records", "r") as f:
                f = json.load(f)

            highscore = int(base64.b64decode(f["highscore"].encode()).decode())

            if highscore < cheseburgerstouched:
                with open("hamburger.records", "w") as f:
                    record = base64.b64encode(str(cheseburgerstouched).encode()).decode()
                    json.dump({"highscore": record}, f)
            
        else:
            with open("hamburger.records", "x") as f:
                highscore = base64.b64encode(str(cheseburgerstouched).encode()).decode()
                json.dump({"highscore": highscore}, f)
        return True

    
            



def renderSpikes(): # Get spike locations and then render it
    s = []
    for spike in spikes:
        s.append(screen.blit(spikeSprite, spike))
    return s

def renderCoins():
    c = []
    locations = []
    iteration = 0
    for coin in coinslocs:
        c.append(screen.blit(CoinSprite, coin))
        locations.append(iteration)
        iteration += 1
    return [c, locations]


def ConfirmationMenu(message):
    confmenu = True
    global antialias
    while confmenu:
        screen.fill((0,179,119))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                QuitMenu()
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    QuitMenu()
                
                if events.key == pygame.K_RETURN:
                    confmenu = False

        confmsg = GFont_smaller.render(message, antialias, (255,255,255))
        successmsg = GFont.render("Success", antialias, (255,255,255))
        confirm = GFont_smaller.render("Hit enter to go back", antialias, (255,255,255))
        screen.blit(confmsg, (300, 200))
        screen.blit(successmsg, (330, 10))
        screen.blit(confirm, (300, 500))

        pygame.display.update()

    return

def QuitMenu():
    quitmenu = True
    global antialias
    while quitmenu:
        screen.fill((128,0,0))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            
            if events.type == pygame.KEYDOWN:

                if events.key == pygame.K_ESCAPE:
                    quitmenu = False

                if events.key == pygame.K_RETURN:
                    pygame.quit()
                    quit(0)
        
        leaving = GFont.render("Leaving hamburger.exe?", antialias, (255,255,255))
        leavingconfirm = GFont_smaller.render("Hit enter to quit, hit ESC to go back", antialias, (255,255,255))
        screen.blit(leaving, (230, 10))
        screen.blit(leavingconfirm, (240, 500))
        pygame.display.set_caption("Hamburger.exe - Quitting")
        pygame.display.update()
    return


def OptionsMenu():
    optionsmenu = True
    while optionsmenu:
        global antialias
        global record
        screen.fill((26,153,0))
        optionstitle = GFont.render("Options", antialias, (255,255,255))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                QuitMenu()
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_q:
                    optionsmenu = False

                if events.key == pygame.K_ESCAPE:
                    QuitMenu()

                if events.key == pygame.K_a:
                    if antialias == True:
                        antialias = False
                    else:
                        antialias = True
                    ConfirmationMenu("Anti alias toggled!")

                if events.key == pygame.K_z:
                    if os.path.exists("./hamburger.records"):
                        os.remove("hamburger.records")
                        record = 0
                        ConfirmationMenu("Successfully deleted records!")

        if antialias == True:
            antialias_setting = GFont_smaller.render("[toggle with A] Text anti alias (Experimental): ON", antialias, (255,166,77))
        else:
            antialias_setting = GFont_smaller.render("[toggle with A] Text anti alias (Experimental): OFF", antialias, (255,166,77))

        record_delete = GFont_smaller.render("[delete with Z] Delete saved records (Warning: Permanent!)", antialias, (255,166,77))


        backarrowhint = GFont_smaller.render("Hit Q to go back", antialias, (255,255,255))

        screen.blit(optionstitle, (350, 10))
        screen.blit(antialias_setting, (100, 50))
        screen.blit(record_delete, (100, 80))
        screen.blit(BackArrowSprite, (30, 500))
        screen.blit(backarrowhint, (10, 560))

        pygame.display.set_caption("Hamburger.exe - Options")
        pygame.display.update()
    return

Menu = True
while Menu:
    screen.fill((102,25,255))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            QuitMenu()
        
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN:
                Menu = False
            
            if events.key == pygame.K_ESCAPE:
                QuitMenu()

            if events.key == pygame.K_q:
                OptionsMenu()

    ttl = GFont_large.render("Hamburger.exe", antialias, (230,115,0))
    randomtitletext = GFont_smaller.render(randomtitle, antialias, (230,230,0))
    hiscore = GFont_smaller.render(f"Your highscore is: {str(record)}", False,(26,153,0))
    hitentertocontinue = GFont_smaller.render("Hit enter to start game", False, (0,26,21))
    copyrighttext = GFont_smaller.render("hamburger.exe v0.3 - By RandomboiXD (2023)", False, (255, 0,0))
    copyrighttext2 = GFont_smaller.render("Licensed Under MIT, read console for license text", False, (255,0,0))
    optionshint = GFont_smaller.render("Hit Q for settings", False, (255, 255 ,255))
    screen.blit(ttl, (240, 150))
    screen.blit(randomtitletext, (245, 200))
    screen.blit(hiscore, (245, 250))
    screen.blit(hitentertocontinue, (280, 500))
    screen.blit(copyrighttext, (1,1))
    screen.blit(copyrighttext2, (1, 20))
    screen.blit(OptionsSprite, (700-32, 500))
    screen.blit(optionshint, (625, 560))
    pygame.display.set_caption("Hamburger.exe - Main Menu")
    pygame.display.update()

runs = True
while runs:
    if hasbackround == True:
        screen.fill(backroundcolor)
    shop = renderShop()
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            QuitMenu()
        
        if events.type == pygame.KEYDOWN:
            
            if events.key == pygame.K_w or events.key == pygame.K_UP:
                if controlsInverted:
                    MovingConstantY += moveSpeed
                else:
                    MovingConstantY -= moveSpeed
            
            if events.key == pygame.K_s or events.key == pygame.K_DOWN:
                if controlsInverted:
                    MovingConstantY -= moveSpeed
                else:
                    MovingConstantY += moveSpeed

            if events.key == pygame.K_d or events.key == pygame.K_RIGHT:
                if controlsInverted:
                    MovingConstantX -= moveSpeed
                else:
                    MovingConstantX += moveSpeed

            if events.key == pygame.K_a or events.key == pygame.K_LEFT:
                if controlsInverted:
                    MovingConstantX += moveSpeed
                else:
                    MovingConstantX -= moveSpeed

            if events.key == pygame.K_x and Coins > 3:
                Coins -= 3
                moveSpeed -= 1

            if events.key == pygame.K_c and Coins > 3:
                Coins -= 3
                moveSpeed += 1

            if events.key == pygame.K_b and Coins > 20:
                Coins -= 20
                TakesDamageFromSpikes = False

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w or events.key == pygame.K_s or events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                MovingConstantY = 0

            if events.key == pygame.K_a or events.key == pygame.K_d or events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                MovingConstantX = 0

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                QuitMenu()

            if events.key == pygame.K_LALT:
                print("--- Start Variable Dump ---")
                print(f"PlayerX/Y: {str((PlayerX, PlayerY))}\nToiletX/Y: {str((ToiletX,ToiletY))}\nGameSaved: {str(Saved)}\nStartupFrames: {str(StartupFrames)}\nSpikes: {str(spikes)}\nGameOver: {str(GameOver)}\ntoilettakechance: {str(toilettakechance)}\nCheseburgerLoc: {str(cheseburgerloc)}\nCheseburgerstouched: {str(cheseburgerstouched)}\nMovingConstantX/Y: {str((MovingConstantX, MovingConstantY))}\nToiletMovingConstantX/Y: {str((ToiletMovingConstantX,ToiletMovingConstantY))}\nMovespeed: {str(moveSpeed)}\nCoins: {str(Coins)}\nCoinslocs: {str(coinslocs)}")
                print("--- End Variable Dump ---")

            if events.key == pygame.K_f:
                if pygame.display.is_fullscreen() == False:
                    pygame.display.toggle_fullscreen()
                    print("Goin' fullscreen!")
                else:
                    pygame.display.toggle_fullscreen()
                    print("No more fullscreen :(")
            
            if events.key == pygame.K_g:
                hasbackround = True


        if events.type == pygame.KEYDOWN and events.key == pygame.K_e and ches.colliderect(player) and GameOver != True:
            cheseburgerloc = (random.randint(200, 500), random.randint(100, 500))
            cheseburgerstouched += 1

        if events.type == pygame.KEYDOWN and events.key == pygame.K_e and toilet.colliderect(player) and toiletMeter > 8 and GameOver != True:
            toiletMeter = 0


    PlayerY += MovingConstantY
    PlayerX += MovingConstantX
    
    if GameOver != True: # This code allows the game to check if player is out of bounds. Thanks ChatGPT for helping me in math... my brain is no longer braining
        if PlayerY > 600 - 64:
            PlayerY = 600 - 64
        elif PlayerY < 0:
            PlayerY = 0

        if PlayerX > 800 - 64:
            PlayerX = 800 - 64
        elif PlayerX < 0:
            PlayerX = 0

    if GameOver != True: # Yeet the player off screen if game over
        player = renderPlayer(PlayerX,PlayerY)
    else:
        player = renderPlayer(99999999,9999999)

    tutorialscreen()
    CoinSign = GFont_smaller.render(f"You have {str(Coins)} coins!", antialias, (255,255,255))
    screen.blit(CoinSign, (620, 580))
    spikelocs = renderSpikes()
    if spikelocs == []:
        pass
    else:
        for x in spikelocs:
            if x.colliderect(player) and TakesDamageFromSpikes == True:
                GameOver = True
                Saved = GameOverScreen(Saved)
    
    coinslocations = renderCoins()
    if coinslocations == []:
        pass
    else:
        for x,y in zip(coinslocations[0], coinslocations[1]):
            if x.colliderect(player):
                Coins += 1
                try:
                    del coinslocs[y]
                except:
                    print(f"An error occured when trying to delete key {str(y)} of coins")
                del x

    ches = renderCheseburger(cheseburgerloc[0], cheseburgerloc[1])

    toiletmovetype = random.choice(["onward", "left", "right", "backward","onward", "left", "right", "backward","onward", "left", "right", "backward","onward", "left", "right", "backward"])
    movelength = [0, 0.5, 0.6, 0.7]
    # Making the toilet move randomly
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
        sup = GFont_smaller.render("Press E to pick up cheseburger!", antialias, (255,255,255))
        screen.blit(sup, fontbottom)

    if toilet.colliderect(player) and toiletMeter > 8:
        sup = GFont_smaller.render("Press E to take a dump", antialias, (255,255,255))
        screen.blit(sup, fontbottom)

    stat = GFont_smaller.render(f"Hamburgers eaten: {str(cheseburgerstouched)}", antialias, (255,255,255))
    screen.blit(stat, burgerstat)
    pygame.display.set_caption(f"Hamburger.exe - {str(cheseburgerstouched)} chesburgers eaten")

    if toiletMeter > 8:
        toiletstat = GFont_smaller.render(f"GO TO THE TOILET!", antialias, (255,255,255))
    else:
        toiletstat = GFont_smaller.render(f"Your toilet meter: {str(toiletMeter)}/10", antialias, (255,255,255))
    toiletwarning = GFont_smaller.render("Going over 10 is a game over!", antialias, (255,0,0))
    if GameOver != True:
        screen.blit(toiletstat, (300, 530))
        screen.blit(toiletwarning, (300, 550))
    
    if GameOver == True:
        gameoverscreentitle = GFont_large.render("Game over.", antialias, (255,0,0))
        screen.blit(gameoverscreentitle, (30, 300))

    if toiletMeter > 10:
        GameOver = True
        Saved = GameOverScreen(Saved)

    if random.randint(0, 999) == 69:

        event = random.choice(["spikes", "rnggod", "rnggodfail", "speedup", "speeddown", "invert", "nobackround", "randombackround", "jackpot"])
        if event == "spikes":
            spikes.append((random.randint(0, 800-64), random.randint(0, 600-64)))
            reaction = GFont_smaller.render(f"Event: Spike planted!", antialias, (255,255,255))
        elif event == "rnggod":
            ups = random.randint(0, 200)
            toilettakechance += ups
            reaction = GFont_smaller.render(f"Event: RNG Gods like you", antialias, (255,255,255))
        elif event == "rnggodfail":
            downs = random.randint(0, 200)
            toilettakechance -= downs
            reaction = GFont_smaller.render(f"Event: The RNG Gods hate you", antialias, (255,255,255))
        elif event == "speedup":
            by = [0.1,0.2,0.3,0.4,0.5,0.6]
            moveSpeed += random.choice(by)
            reaction = GFont_smaller.render(f"Event: Im sanic! Sanic the hedgehog!", antialias, (255,255,255))
        elif event == "speeddown":
            by = [0.1,0.2]
            moveSpeed -= random.choice(by)
            reaction = GFont_smaller.render(f"Event: Snail moment", antialias, (255,255,255))
        elif event == "invert":
            if controlsInverted:
                reaction = GFont_smaller.render("Event: No more weird controls!", antialias, (255,255,255))
                controlsInverted = False
            else:
                reaction = GFont_smaller.render("Event: You know what? *inverts your controls*", antialias, (255,255,255))
                controlsInverted = True
        elif event == "nobackround":
            if hasbackround:
                hasbackround = False
                reaction = GFont_smaller.render("Event: Eh who needs a backround?", antialias, (255,255,255))
                print("Backround was disabled! Hit G to fix!")
            else:
                hasbackround = True
                reaction = GFont_smaller.render("Event: yo we need that backround", antialias, (255,255,255))
        elif event == "randombackround":
            backroundcolor = random.choice(colorcodes)
            reaction = GFont_smaller.render("Event: New color time!", antialias, (255,255,255))
        elif event == "jackpot":
            howmuch = random.randint(1, 100)
            for x in range(howmuch):
                coinslocs.append((random.randint(100, 700), random.randint(100, 500)))
            reaction = GFont_smaller.render("Event: WOOOOO Jackpot!", antialias, (255,255,255))
        
    screen.blit(reaction, (400, 10))
    version = GFont_smaller.render(f"Build V0.3, RandomboiXD", antialias, (255,0,0))
    records = GFont_smaller.render(f"High score: {str(record)}", antialias, (0,255,0))
    screen.blit(records, (1,20))
    screen.blit(version, (1,1))
    if shop.colliderect(player):
        HintDisplay = GFont_smaller.render("Welcome to the shop!", antialias, (255,255,255))
        HintDisplay2 = GFont_smaller.render("X = -1 Speed,C = + 1 speed, 3 coins each!", antialias, (255,255,255))
        HintDisplay3 = GFont_smaller.render("B = No damage from spikes (20 coins)", antialias, (255,255,255))
        screen.blit(HintDisplay, (PlayerX, PlayerY-30))
        screen.blit(HintDisplay2, (PlayerX, PlayerY-50))
        screen.blit(HintDisplay3, (PlayerX, PlayerY-70))
    pygame.display.update()
    dice = random.randint(0, toilettakechance)
    if dice == 69: 
        toiletMeter += 1

    if dice == 2:
        coinslocs.append((random.randint(100, 700), random.randint(100, 500)))
    


    StartupFrames += 1
    
