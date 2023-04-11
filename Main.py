import sys
import time
import pygame
import pickle
from pygame import mixer


# Random variables
pygame.init()
ID = -1
temp = 0
tempText = 0
loop1 = True
screen = [800, 400]
window = pygame.display.set_mode(screen, pygame.RESIZABLE)
speed = 0
jumpSpeed = 25
startTime = time.time()
fireTime = time.time() - 100


# Icon and the name of the game
pygame.display.set_caption("The Game")
icon = pygame.image.load("graphics/IJ.png")
pygame.display.set_icon(icon)

text_font = pygame.font.SysFont('Corbel', 35)


# The finish line
fin = pygame.transform.scale(pygame.image.load("graphics/fin.png"), (80, 400)).convert_alpha()


# Collectibles
jumpShoesC = pygame.transform.scale(pygame.image.load("graphics/shoes.png"), (70, 70)).convert_alpha()
gunC = pygame.transform.scale(pygame.image.load("graphics/gunC.png"), (70, 35)).convert_alpha()


# Graphics for the menu
unlocked = pygame.transform.scale(pygame.image.load("graphics/Unlocked.png"), (70, 70)).convert_alpha()
locked = pygame.transform.scale(pygame.image.load("graphics/Locked.png"), (70, 70)).convert_alpha()
setting = pygame.transform.scale(pygame.image.load("graphics/Settings.png"), (70, 70)).convert_alpha()
collectible = pygame.transform.scale(pygame.image.load("graphics/Collectibles.png"), (70, 70)).convert_alpha()
back = pygame.transform.scale(pygame.image.load("graphics/Back.png"), (70, 70)).convert_alpha()
secret = pygame.transform.scale(pygame.image.load("graphics/Secret.png"), (70, 70)).convert_alpha()


# Backgrounds and platforms
player = pygame.transform.scale(pygame.image.load("graphics/player.png"), (12 * 9, 12 * 14)).convert_alpha()
playerJump = pygame.transform.scale(pygame.image.load("graphics/playerJump.png"), (12 * 9, 12 * 14)).convert_alpha()
player_rect = player.get_rect(bottomleft=(50, 0))
platform = pygame.transform.scale(pygame.image.load("graphics/pI.png"), (160, 40)).convert_alpha()
platform_rect = platform.get_rect()
bg = pygame.transform.scale(pygame.image.load("graphics/bgI.png"), (800 * 12, 35 * 12)).convert_alpha()
bg_rect = bg.get_rect(topleft=(-50, 0))
platform1 = pygame.transform.scale(pygame.image.load("graphics/p1.png"), (160, 40)).convert_alpha()
bg1 = pygame.transform.scale(pygame.image.load("graphics/bg1.png"), (800 * 12, 35 * 12)).convert_alpha()
bg1sky = pygame.transform.scale(pygame.image.load("graphics/bg1sky.png"), (800, 400)).convert_alpha()
player1 = pygame.transform.scale(pygame.image.load("graphics/player1.png"), (12 * 9, 12 * 14)).convert_alpha()
player1Jump = pygame.transform.scale(pygame.image.load("graphics/player1jump.png"), (12 * 9, 12 * 14)).convert_alpha()
bullet = pygame.transform.scale(pygame.image.load("graphics/bullet.png"), (22, 6)).convert_alpha()
bullet_rect = bullet.get_rect()
equipped = pygame.transform.scale(pygame.image.load("graphics/equipped.png"), (75, 75)).convert_alpha()


# Music and sound
song = 0
mixer.init()
musicVolume = 100
mixer.music.load("sound/starbound.mp3")
mixer.music.set_volume(musicVolume)
mixer.music.play(-1)


# Button status
class Buttons:
    w = False
    a = False
    s = False
    d = False
    space = False
    mouse = False


# Shooting stuff
class Shoot:
    left = False
    right = False


def fire():
    global bullet
    Time = time.time()-fireTime
    if Shoot.left:
        window.blit(bullet, (bullet_rect.x-(Time*800), bullet_rect.y))
    if Shoot.right:
        window.blit(bullet, (bullet_rect.x+(Time*800), bullet_rect.y))


# Equipped gear
class Gear:
    def setvar(self, var):
        for key, value in var.items():
            try:
                setattr(self, key, value)
            except Exception as ex:
                print("(Not a real problem, 99% sure)")
    l1ce = False
    l2ce = False
    l3ce = False
    l4ce = False
    l5ce = False
    l6ce = False
    l7ce = False
    l8ce = False
    l9ce = False
    l10ce = False


def save_object(obj):
    try:
        with open("saves/data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Failure to save", ex)


# Load saved object or create new ones
globals().update({"introC": False, "l1C": False, "l2C": False, "l3C": False, "l4C": False, "l5C": False, "l6C": False, "l7C": False, "l8C": False, "l9C": False, "l10C": False, "l1c": False, "l2c": False, "l3c": False, "l4c": False, "l5c": False, "l6c": False, "l7c": False, "l8c": False, "l9c": False, "l10c": False, "l1ce": False, "l2ce": False, "l3ce": False, "l4ce": False, "l5ce": False, "l6ce": False, "l7ce": False, "l8ce": False, "l9ce": False, "l10ce": False, "jump": False})
try:
    with open("saves/data.pickle", "rb") as f:
        savedObject = pickle.load(f)
    globals().update(savedObject)
    try:
        for key, value in savedObject.items():
            setattr(Gear, key, value)
    except Exception as ex:
        print(ex, "Hopefully not a problem")
except Exception as ex:
    print(ex, "(Not a real problem, 99% sure)")


# Post credit scene
def pcs():
    pass


# The screen to view collected items
def collectibles():
    global ID, locked, l1c, l2c, l3c, l4c, l5c, l6c, l7c, l8c, l9c, l10c, back, secret, gunC, equipped
    window.fill("Light Blue")
    back_rect = back.get_rect(center=(200, 50))
    secret_rect = secret.get_rect(center=(600, 50))
    C1 = gunC.get_rect(center=(200, 200))
    C2 = locked.get_rect(center=(300, 200))
    C3 = locked.get_rect(center=(400, 200))
    C4 = locked.get_rect(center=(500, 200))
    C5 = locked.get_rect(center=(600, 200))
    C6 = locked.get_rect(center=(200, 300))
    C7 = locked.get_rect(center=(300, 300))
    C8 = locked.get_rect(center=(400, 300))
    C9 = locked.get_rect(center=(500, 300))
    C10 = locked.get_rect(center=(600, 300))

    window.blit(back, back_rect)
    if Buttons.mouse and back_rect.collidepoint(pygame.mouse.get_pos()):
        ID = -1

    window.blit(secret, secret_rect)
    if Buttons.mouse and secret_rect.collidepoint(pygame.mouse.get_pos()):
        ID = -4

    if l1c:
        if Gear.l1ce:
            window.blit(equipped, equipped.get_rect(center=C1.center))
        elif Buttons.mouse and C1.collidepoint(pygame.mouse.get_pos()):
            Gear.l1ce = True
        window.blit(gunC, C1)
    else:
        window.blit(locked, locked.get_rect(center=C1.center))

    if l2c:
        if Gear.l2ce:
            window.blit(equipped, equipped.get_rect(center=C2.center))
        window.blit(gunC, C2)
    else:
        window.blit(locked, locked.get_rect(center=C2.center))

    if l3c:
        if Gear.l3ce:
            window.blit(equipped, equipped.get_rect(center=C3.center))
        window.blit(gunC, C3)
    else:
        window.blit(locked, locked.get_rect(center=C3.center))

    if l4c:
        if Gear.l4ce:
            window.blit(equipped, equipped.get_rect(center=C4.center))
        window.blit(gunC, C4)
    else:
        window.blit(locked, locked.get_rect(center=C4.center))

    if l5c:
        if Gear.l5ce:
            window.blit(equipped, equipped.get_rect(center=C5.center))
        window.blit(gunC, C5)
    else:
        window.blit(locked, locked.get_rect(center=C5.center))

    if l6c:
        if Gear.l6ce:
            window.blit(equipped, equipped.get_rect(center=C6.center))
        window.blit(gunC, C6)
    else:
        window.blit(locked, locked.get_rect(center=C6.center))

    if l7c:
        if Gear.l7ce:
            window.blit(equipped, equipped.get_rect(center=C7.center))
        window.blit(gunC, C7)
    else:
        window.blit(locked, locked.get_rect(center=C7.center))

    if l8c:
        if Gear.l8ce:
            window.blit(equipped, equipped.get_rect(center=C8.center))
        window.blit(gunC, C8)
    else:
        window.blit(locked, locked.get_rect(center=C8.center))

    if l9c:
        if Gear.l9ce:
            window.blit(equipped, equipped.get_rect(center=C9.center))
        window.blit(gunC, C9)
    else:
        window.blit(locked, locked.get_rect(center=C9.center))

    if l10c:
        if Gear.l10ce:
            window.blit(equipped, equipped.get_rect(center=C10.center))
        window.blit(gunC, C10)
    else:
        window.blit(locked, locked.get_rect(center=C10.center))


# The settings for important things
def settings():
    pass


# The menu where you select levels, collectibles, or settings
def menu():
    global ID, locked, unlocked, introC, l1C, l2C, l3C, l4C, l5C, l6C, l7C, l8C, l9C, l10C, setting, collectible, song
    if song != 0:
        song = 0
        mixer.music.stop()
        mixer.music.load("sound/starbound.mp3")
        mixer.music.play(-1)
    window.fill("Light Blue")

    # Create rect for blit
    collectible_rect = setting.get_rect(center=(100, 50))
    setting_rect = setting.get_rect(center=(700, 50))
    Ui = unlocked.get_rect(center=(100, 150))
    U1 = unlocked.get_rect(center=(300, 150))
    U2 = unlocked.get_rect(center=(500, 150))
    U3 = unlocked.get_rect(center=(700, 150))
    U4 = unlocked.get_rect(center=(100, 250))
    U5 = unlocked.get_rect(center=(300, 250))
    U6 = unlocked.get_rect(center=(500, 250))
    U7 = unlocked.get_rect(center=(700, 250))
    U8 = unlocked.get_rect(center=(100, 350))
    U9 = unlocked.get_rect(center=(300, 350))
    U10 = unlocked.get_rect(center=(500, 350))
    Uec = unlocked.get_rect(center=(700, 350))

    window.blit(collectible, collectible_rect)
    if Buttons.mouse:
        if collectible_rect.collidepoint(pygame.mouse.get_pos()):
            ID = -3

    window.blit(setting, setting_rect)
    if Buttons.mouse:
        if setting_rect.collidepoint(pygame.mouse.get_pos()):
            ID = -2

    window.blit(unlocked, Ui)
    tempText = text_font.render("Intro", True, "Black")
    window.blit(tempText, tempText.get_rect(center=Ui.center))
    if Buttons.mouse:
        if Ui.collidepoint(pygame.mouse.get_pos()):
            ID = 0

    if introC:
        window.blit(unlocked, U1)
        tempText = text_font.render("lvl.1", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U1.center))
        if Buttons.mouse and U1.collidepoint(pygame.mouse.get_pos()):
            ID = 1
    else:
        window.blit(locked, U1)

    if l1C:
        window.blit(unlocked, U2)
        tempText = text_font.render("lvl.2", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U2.center))
        if Buttons.mouse and U2.collidepoint(pygame.mouse.get_pos()):
            ID = 2
    else:
        window.blit(locked, U2)

    if l2C:
        window.blit(unlocked, U3)
        tempText = text_font.render("lvl.3", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U3.center))
        if Buttons.mouse and U3.collidepoint(pygame.mouse.get_pos()):
            ID = 3
    else:
        window.blit(locked, U3)

    if l3C:
        window.blit(unlocked, U4)
        tempText = text_font.render("lvl.4", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U4.center))
        if Buttons.mouse and U4.collidepoint(pygame.mouse.get_pos()):
            ID = 4
    else:
        window.blit(locked, U4)

    if l4C:
        window.blit(unlocked, U5)
        tempText = text_font.render("lvl.5", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U5.center))
        if Buttons.mouse and U5.collidepoint(pygame.mouse.get_pos()):
            ID = 5
    else:
        window.blit(locked, U5)

    if l5C:
        window.blit(unlocked, U6)
        tempText = text_font.render("lvl.6", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U6.center))
        if Buttons.mouse and U6.collidepoint(pygame.mouse.get_pos()):
            ID = 6
    else:
        window.blit(locked, U6)

    if l6C:
        window.blit(unlocked, U7)
        tempText = text_font.render("lvl.7", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U7.center))
        if Buttons.mouse and U7.collidepoint(pygame.mouse.get_pos()):
            ID = 7
    else:
        window.blit(locked, U7)

    if l7C:
        window.blit(unlocked, U8)
        tempText = text_font.render("lvl.8", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U8.center))
        if Buttons.mouse and U8.collidepoint(pygame.mouse.get_pos()):
            ID = 8
    else:
        window.blit(locked, U8)

    if l8C:
        window.blit(unlocked, U9)
        tempText = text_font.render("lvl.9", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U9.center))
        if Buttons.mouse and U9.collidepoint(pygame.mouse.get_pos()):
            ID = 9
    else:
        window.blit(locked, U9)

    if l9C:
        window.blit(unlocked, U10)
        tempText = text_font.render("lvl.10", True, "Black")
        window.blit(tempText, tempText.get_rect(center=U10.center))
        if Buttons.mouse and U10.collidepoint(pygame.mouse.get_pos()):
            ID = 10
    else:
        window.blit(locked, U10)

    if l10C:
        window.blit(unlocked, Uec)
        tempText = text_font.render("End", True, "Black")
        window.blit(tempText, tempText.get_rect(center=Uec.center))
        if Buttons.mouse and Uec.collidepoint(pygame.mouse.get_pos()):
            ID = 11
    else:
        window.blit(locked, Uec)

    tempText = text_font.render("The Game", True, "Black")
    window.blit(tempText, tempText.get_rect(center=(400, 50)))


# The intro level
def intro():
    global temp, introC, ID,  speed, jumpSpeed, jump, gear
    platforms = [[30, 350], [190, 350], [700, 300], [400, 250]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline(player_rect.bottomleft, player_rect.bottomright):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w and jump:
                    speed = jumpSpeed

        # Graphics
        window.blit(bg, bg_rect)
        if not jump:
            window.blit(jumpShoesC, jumpShoesC.get_rect(topleft=(platform_rect.x+250, platform_rect.y+200)))
        if speed != 0:
            window.blit(playerJump, player_rect)
        else:
            window.blit(player, player_rect)
        for i in platforms:
            window.blit(platform, (platform_rect.x+i[0], platform_rect.y+i[1]))

        if jumpShoesC.get_rect(topleft=(platform_rect.x+250, platform_rect.y+200)).colliderect(player_rect):
            jump = True
        if jump:
            tempText = text_font.render("Collectible found, you can now jump!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))
        fire()

        # Win conditions
        window.blit(fin, (platform_rect.x+1000, platform_rect.y))
        if player_rect.x-platform_rect.x >= 1000:
            introC = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2

    # When the level is over, check if the player wants the next level or the menu
    elif temp == 1:
        if Buttons.mouse:
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
            else:
                ID = 1
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (-50, 0)
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Intro Complete!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Next Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))

    # Restart level or return to menu after loss
    else:
        if Buttons.mouse:
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
            else:
                ID = 0
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (0, 0)
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Level failed", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Restart Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))


def l1():
    global temp, l1C, l1c, ID, speed, jumpSpeed
    platforms = [[30, 350], [190, 350], [700, 300], [400, 250], [900, 350], [1100, 250]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform1.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline(player_rect.bottomleft, player_rect.bottomright):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w:
                    speed = jumpSpeed

        # Graphics
        window.blit(bg1sky, (0, 0))
        window.blit(bg1, bg_rect)
        if speed != 0:
            window.blit(player1Jump, player_rect)
        else:
            window.blit(player1, player_rect)
        for i in platforms:
            window.blit(platform1, (platform_rect.x+i[0], platform_rect.y+i[1]))
        fire()

        # Collectible
        if gunC.get_rect(topleft=(platform_rect.x+500, platform_rect.y+100)).colliderect(player_rect):
            l1c = True
            Gear.l1ce = True
        if not l1c:
            window.blit(gunC, (platform_rect.x+500, platform_rect.y+100))
        else:
            tempText = text_font.render("Collectible found!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))

        # Win conditions
        window.blit(fin, (platform_rect.x+1400, platform_rect.y))
        if player_rect.x-platform_rect.x >= 1400:
            l1C = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2

    # When the level is over, check if the player wants the next level or the menu
    elif temp == 1:
        if Buttons.mouse:
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
            else:
                ID = 2
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (-50, 0)
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Intro Complete!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Next Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))

    # Restart level or return to menu after loss
    else:
        if Buttons.mouse:
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
            else:
                ID = 1
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (0, 0)
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Level failed", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Restart Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))


def l2():
    global ID, l2C
    window.fill("Red")
    ID = -1
    l2C = True


def l3():
    global ID, l3C
    window.fill("Red")
    ID = -1
    l3C = True


def l4():
    global ID, l4C
    window.fill("Red")
    ID = -1
    l4C = True


def l5():
    global ID, l5C
    window.fill("Red")
    ID = -1
    l5C = True


def l6():
    global ID, l6C
    window.fill("Red")
    ID = -1
    l6C = True


def l7():
    global ID, l7C
    window.fill("Red")
    ID = -1
    l7C = True


def l8():
    global ID, l8C
    window.fill("Red")
    ID = -1
    l8C = True


def l9():
    global ID, l9C
    window.fill("Red")
    ID = -1
    l9C = True


def l10():
    global ID, l10C
    window.fill("Red")
    ID = -1
    l10C = True


def end_credits():
    global ID, platform_rect, song
    stop = 1700
    if song != 1:
        song = 1
        mixer.music.stop()
        mixer.music.load("sound/End Credit Song.mp3")
        mixer.music.play(-1)
    window.fill("Black")
    tempText = text_font.render("The Game", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+400)))
    tempText = text_font.render("Lead Team", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+500)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+550)))
    tempText = text_font.render("Lead Developer", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+650)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+700)))
    tempText = text_font.render("Lead Coder", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+800)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+850)))
    tempText = text_font.render("Lead Designer", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+950)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1000)))
    tempText = text_font.render("PR Department", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1100)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1150)))
    tempText = text_font.render("Funds Department", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1250)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1300)))
    if platform_rect.y >= -(stop-200):
        platform_rect.y -= 1
    if Buttons.space:
        ID = -1
        platform_rect.topleft = (0, 0)
    tempText = text_font.render("Press space to return to menu", True, "Pink")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y+stop)))


# The main play function,take cares of which levels or menus are open
def play():
    global loop1, ID, temp, speed, jumpSpeed, fireTime

    # Button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Buttons.d = True
            if event.key == pygame.K_a:
                Buttons.a = True
            if event.key == pygame.K_s:
                Buttons.s = True
            if event.key == pygame.K_w:
                Buttons.w = True
            if event.key == pygame.K_SPACE:
                Buttons.space = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Buttons.d = False
            if event.key == pygame.K_a:
                Buttons.a = False
            if event.key == pygame.K_s:
                Buttons.s = False
            if event.key == pygame.K_w:
                Buttons.w = False
            if event.key == pygame.K_SPACE:
                Buttons.space = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Buttons.mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            Buttons.mouse = False

    # Movement and alike
    if ID in range(0, 10) and temp == 0:
        if Buttons.d:
            if player_rect.x <= 400:
                player_rect.x += 3
                platform_rect.x -= 3
                bg_rect.x -= 2
                bullet_rect.x -= 3
            else:
                platform_rect.x -= 6
                bg_rect.x -= 3
                bullet_rect.x -= 6
        if Buttons.a and platform_rect.x < 0:
            if player_rect.x >= 50:
                player_rect.x -= 3
                platform_rect.x += 3
                bg_rect.x += 2
                bullet_rect.x += 3
            else:
                platform_rect.x += 6
                bg_rect.x += 3
                bullet_rect.x += 6
        player_rect.y -= speed
        if speed != 0:
            speed -= 1

        print(time.time()-fireTime)
        if Buttons.space:
            if time.time()-fireTime > 1 and Gear.l1ce:
                if pygame.mouse.get_pos()[0] <= player_rect.x:
                    Shoot.left = True
                    Shoot.right = False
                    bullet_rect.midright = player_rect.midleft
                else:
                    Shoot.left = False
                    Shoot.right = True
                    bullet_rect.midleft = player_rect.midright
                fireTime = time.time()

    # Check what level to play
    if ID == -4:
        pcs()
    if ID == -3:
        collectibles()
    if ID == -2:
        settings()
    if ID == -1:
        menu()
    elif ID == 0:
        intro()
    elif ID == 1:
        l1()
    elif ID == 2:
        l2()
    elif ID == 3:
        l3()
    elif ID == 4:
        l4()
    elif ID == 5:
        l5()
    elif ID == 6:
        l6()
    elif ID == 7:
        l7()
    elif ID == 8:
        l8()
    elif ID == 9:
        l9()
    elif ID == 10:
        l10()
    elif ID == 11:
        end_credits()


# Start the mayhem
while loop1:
    play()
    pygame.display.flip()
    pygame.time.Clock().tick(60)


# Save things
print(Gear.l1ce)
toBeSaved = {"introC": introC, "l1C": l1C, "l2C": l2C,
             "l3C": l3C, "l4C": l4C, "l5C": l5C, "l6C": l6C,
             "l7C": l7C, "l8C": l8C, "l9C": l9C, "l10C": l10C,
             "l1c": l1c, "l2c": l2c, "l3c": l3c, "l4c": l4c,
             "l5c": l5c, "l6c": l6c, "l7c": l7c, "l8c": l8c,
             "l9c": l9c, "l10c": l10c, "jump": jump, "l1ce": Gear.l1ce,
             "l2ce": Gear.l2ce, "l3ce": Gear.l3ce, "l4ce": Gear.l4ce,
             "l5ce": Gear.l5ce, "l6ce": Gear.l6ce, "l7ce": Gear.l7ce,
             "l8ce": Gear.l8ce, "l9ce": Gear.l9ce, "l10ce": Gear.l10ce}
print(toBeSaved)
save_object(toBeSaved)
sys.exit()
