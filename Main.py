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
jumpSpeed = 20
startTime = time.time()
fireTime = time.time() - 100
timeChange = time.time()
destructPlatform = []
killPlatform = []
grass = 0


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
swordC = pygame.transform.scale(pygame.image.load("graphics/SwordC.png"), (77, 38)).convert_alpha()
eyeC = pygame.transform.scale(pygame.image.load("graphics/eyeC.png"), (77, 38)).convert_alpha()


# Graphics for the menu
unlocked = pygame.transform.scale(pygame.image.load("graphics/Unlocked.png"), (70, 70)).convert_alpha()
locked = pygame.transform.scale(pygame.image.load("graphics/Locked.png"), (70, 70)).convert_alpha()
setting = pygame.transform.scale(pygame.image.load("graphics/Settings.png"), (70, 70)).convert_alpha()
collectible = pygame.transform.scale(pygame.image.load("graphics/Collectibles.png"), (70, 70)).convert_alpha()
back = pygame.transform.scale(pygame.image.load("graphics/Back.png"), (70, 70)).convert_alpha()
box = pygame.transform.scale(pygame.image.load("graphics/Box.png"), (210, 70)).convert_alpha()
secret = pygame.transform.scale(pygame.image.load("graphics/Secret.png"), (70, 70)).convert_alpha()


# Backgrounds and platforms
player = pygame.transform.scale(pygame.image.load("graphics/player.png"), (12 * 9, 12 * 14)).convert_alpha()
playerJump = pygame.transform.scale(pygame.image.load("graphics/playerJump.png"), (12 * 9, 12 * 14)).convert_alpha()
player_rect = player.get_rect(bottomleft=(50, 0))
platform = pygame.transform.scale(pygame.image.load("graphics/pI.png"), (160, 40)).convert_alpha()
platform_rect = platform.get_rect()
platformD = pygame.transform.scale(pygame.image.load("graphics/pD.png"), (40, 160)).convert_alpha()
platformD_rect = platform.get_rect()
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
bg9 = pygame.transform.scale(pygame.image.load("graphics/bg9.png"), (800 * 12, 35 * 12)).convert_alpha()
bg9text = pygame.transform.scale(pygame.image.load("graphics/bg1.png"), (800 * 12, 35 * 12)).convert_alpha()
grass1 = pygame.transform.scale(pygame.image.load("graphics/bg1.png"), (16*8, 16*4)).convert_alpha()
grass2 = pygame.transform.scale(pygame.image.load("graphics/bg1.png"), (16*8, 16*4)).convert_alpha()
grass3 = pygame.transform.scale(pygame.image.load("graphics/bg1.png"), (16*8, 16*4)).convert_alpha()
bg2 = pygame.transform.scale(pygame.image.load("graphics/bg2.png"), (800 * 12, 35 * 12)).convert_alpha()
platform2 = pygame.transform.scale(pygame.image.load("graphics/p2.png"), (160, 40)).convert_alpha()
platform2cracked = pygame.transform.scale(pygame.image.load("graphics/p2c.png"), (160, 40)).convert_alpha()
player2 = pygame.transform.scale(pygame.image.load("graphics/player2.png"), (12 * 9, 12 * 14)).convert_alpha()
player2Jump = pygame.transform.scale(pygame.image.load("graphics/player2jump.png"), (12 * 9, 12 * 14)).convert_alpha()
sword = pygame.transform.scale(pygame.image.load("graphics/sword.png"), (120, 50)).convert_alpha()
swordInv = pygame.transform.scale(pygame.image.load("graphics/swordInv.png"), (120, 50)).convert_alpha()
bg3 = pygame.transform.scale(pygame.image.load("graphics/bg3.png"), (800 * 12, 35 * 12)).convert_alpha()
player3 = pygame.transform.scale(pygame.image.load("graphics/player3.png"), (12 * 9, 12 * 14)).convert_alpha()
player3Jump = pygame.transform.scale(pygame.image.load("graphics/player3jump.png"), (12 * 9, 12 * 14)).convert_alpha()
eye = pygame.transform.scale(pygame.image.load("graphics/eye.png"), (140, 50)).convert_alpha()
eyeInv = pygame.transform.scale(pygame.image.load("graphics/eyeInv.png"), (140, 50)).convert_alpha()


# Music and sound
song = 0
mixer.init()
musicVolume = 0.5
mixer.music.load("sound/starbound.mp3")
mixer.music.set_volume(musicVolume)
mixer.music.play(-1)
buttonVolume = 0.5
buttonPress = mixer.Sound("sound/buttonPress.mp3")
mixer.Sound.set_volume(buttonPress, buttonVolume)
sfxVolume = 0.5
revolverFire = mixer.Sound("sound/revolverFire.mp3")
revolverReload = mixer.Sound("sound/revolverReload.mp3")
shotgunFire = mixer.Sound("sound/shotgunFire.mp3")
swing = mixer.Sound("sound/swing.mp3")
laser = mixer.Sound("sound/laser.mp3")
sfx = [revolverFire, revolverReload, shotgunFire, swing, laser]


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
    global bullet, destructPlatform, killPlatform, temp
    Time = time.time()-fireTime
    bulletList = []
    melee_rect = sword.get_rect(center=(0, -1000))

    # Revolver
    if Gear.l1ce and temp == 0:
        if Time < 0.01:
            revolverFire.play()
            revolverReload.play()
        if Shoot.left:
            bulletList = [(bullet_rect.x-(Time*800), bullet_rect.y)]
        if Shoot.right:
            bulletList = [(bullet_rect.x+(Time*800), bullet_rect.y)]

    # Sword
    elif Gear.l2ce and temp == 0:
        if Shoot.left and Buttons.space and speed == 0:
            if Time < 0.01:
                swing.play()
            melee_rect = sword.get_rect(midright=(player_rect.left+40, player_rect.centery+15))
            window.blit(swordInv, melee_rect)
        if Shoot.right and Buttons.space and speed == 0:
            if Time < 0.01:
                swing.play()
            melee_rect = sword.get_rect(midleft=(player_rect.right-40, player_rect.centery+15))
            window.blit(sword, melee_rect)

    # Eye
    elif Gear.l3ce and temp == 0:
        if Shoot.left and Buttons.space and speed == 0:
            if Time < 0.01:
                laser.play()
            melee_rect = eyeInv.get_rect(midright=(player_rect.left+40, player_rect.centery+15))
            window.blit(eyeInv, melee_rect)
        if Shoot.right and Buttons.space and speed == 0:
            if Time < 0.01:
                laser.play()
            melee_rect = eye.get_rect(midleft=(player_rect.right-40, player_rect.centery+15))
            window.blit(eye, melee_rect)

    # Shotgun
    elif Gear.l4ce and temp == 0:
        if Time < 0.01:
            shotgunFire.play()
        if Shoot.left:
            bulletList = [(bullet_rect.x-(Time*800), bullet_rect.y+(Time*200)),
                          (bullet_rect.x-(Time*800), bullet_rect.y),
                          (bullet_rect.x-(Time*800), bullet_rect.y-(Time*200))]
        if Shoot.right:
            bulletList = [(bullet_rect.x+(Time*800), bullet_rect.y+(Time*200)),
                          (bullet_rect.x+(Time*800), bullet_rect.y),
                          (bullet_rect.x+(Time*800), bullet_rect.y-(Time*200))]

    # Check if bullet hits platform
    for j in bulletList:
        window.blit(bullet, j)
        for i in destructPlatform:
            if not platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).collidelist([bullet.get_rect(topleft=j)]):
                destructPlatform.remove(i)
        for i in killPlatform:
            if not platformD.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).collidelist([bullet.get_rect(topleft=j)]):
                killPlatform.remove(i)

    # Check if melee hits platform
    for i in destructPlatform:
        if platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).colliderect(melee_rect):
            destructPlatform.remove(i)
    for i in killPlatform:
        if platformD.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).colliderect(melee_rect):
            killPlatform.remove(i)


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
globals().update({"introC": False, "l1C": False, "l2C": False,
                  "l3C": False, "l4C": False, "l5C": False,
                  "l6C": False, "l7C": False, "l8C": False,
                  "l9C": False, "l10C": False, "l1c": False,
                  "l2c": False, "l3c": False, "l4c": False,
                  "l5c": False, "l6c": False, "l7c": False,
                  "l8c": False, "l9c": False, "l10c": False,
                  "jump": False})
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
mixer.music.set_volume(musicVolume)
mixer.Sound.set_volume(buttonPress, buttonVolume)
for z in sfx:
    mixer.Sound.set_volume(z, sfxVolume)


# Post credit scene
def pcs():
    global back, ID

    window.fill("Light Blue")

    # Back to menu button
    back_rect = back.get_rect(center=(400, 50))
    window.blit(back, back_rect)
    if Buttons.mouse and back_rect.collidepoint(pygame.mouse.get_pos()):
        buttonPress.play()
        ID = -3


# The screen to view collected items
def collectibles():
    global ID, locked, l1c, l2c, l3c, l4c, l5c, l6c, l7c, l8c, l9c, l10c, back, secret, gunC, equipped, timeChange

    window.fill("Light Blue")

    C1 = gunC.get_rect(center=(200, 200))
    C2 = swordC.get_rect(center=(300, 200))
    C3 = eyeC.get_rect(center=(400, 200))
    C4 = locked.get_rect(center=(500, 200))
    C5 = locked.get_rect(center=(600, 200))
    C6 = locked.get_rect(center=(200, 300))
    C7 = locked.get_rect(center=(300, 300))
    C8 = locked.get_rect(center=(400, 300))
    C9 = locked.get_rect(center=(500, 300))
    C10 = locked.get_rect(center=(600, 300))

    # Back to menu button
    back_rect = back.get_rect(center=(200, 50))
    window.blit(back, back_rect)
    if Buttons.mouse and back_rect.collidepoint(pygame.mouse.get_pos()):
        ID = -1
        buttonPress.play()

    # Start a cutscene if you have all collectibles
    secret_rect = secret.get_rect(center=(600, 50))
    window.blit(secret, secret_rect)
    if Buttons.mouse and secret_rect.collidepoint(pygame.mouse.get_pos()):
        ID = -4
        buttonPress.play()

    if l1c:
        if Gear.l1ce:
            window.blit(equipped, equipped.get_rect(center=C1.center))
        if C1.collidepoint(pygame.mouse.get_pos()):
            if Buttons.mouse and time.time()-timeChange >= 0.5:
                buttonPress.play()
                if not Gear.l1ce:
                    Gear.l1ce = True
                else:
                    Gear.l1ce = False
                Gear.l2ce = False
                Gear.l3ce = False
                timeChange = time.time()
        window.blit(gunC, C1)
    else:
        window.blit(locked, locked.get_rect(center=C1.center))

    if l2c:
        if Gear.l2ce:
            window.blit(equipped, equipped.get_rect(center=C2.center))
        if C2.collidepoint(pygame.mouse.get_pos()):
            if Buttons.mouse and time.time()-timeChange >= 0.5:
                buttonPress.play()
                if not Gear.l2ce:
                    Gear.l2ce = True
                else:
                    Gear.l2ce = False
                Gear.l1ce = False
                Gear.l3ce = False
                timeChange = time.time()
        window.blit(swordC, C2)
    else:
        window.blit(locked, locked.get_rect(center=C2.center))

    if l3c:
        if Gear.l3ce:
            window.blit(equipped, equipped.get_rect(center=C3.center))
        window.blit(eyeC, C3)
        if C3.collidepoint(pygame.mouse.get_pos()):
            if Buttons.mouse and time.time()-timeChange >= 0.5:
                buttonPress.play()
                if not Gear.l3ce:
                    Gear.l3ce = True
                else:
                    Gear.l3ce = False
                Gear.l1ce = False
                Gear.l2ce = False
                timeChange = time.time()
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
        if C9.collidepoint(pygame.mouse.get_pos()):
            if Buttons.mouse and time.time()-timeChange >= 0.5:
                buttonPress.play()
                if not Gear.l9ce:
                    Gear.l9ce = True
                else:
                    Gear.l9ce = False
                timeChange = time.time()
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
    global buttonVolume, musicVolume, sfxVolume, ID

    window.fill("Light blue")
    sliders = [((100, 300), "Music", musicVolume),
               ((100, 200), "Button", buttonVolume),
               ((100, 100), "SFX", sfxVolume)]
    mouse = pygame.mouse.get_pos()

    j = 0
    for i, j, k in sliders:
        if Buttons.mouse and i[0]+10 <= mouse[0] <= i[0]+590 and i[1] <= mouse[1] <= i[1]+50:
            if k != round((mouse[0]-110)/580, 2):
                if j == "Music":
                    musicVolume = round((mouse[0]-110)/580, 2)
                    mixer.music.set_volume(musicVolume)
                elif j == "Button":
                    buttonVolume = round((mouse[0]-110)/580, 2)
                    mixer.Sound.set_volume(buttonPress, buttonVolume)
                elif j == "SFX":
                    sfxVolume = round((mouse[0]-110)/580, 2)
                    for z in sfx:
                        mixer.Sound.set_volume(z, sfxVolume)
                buttonPress.play()
        pygame.draw.rect(window, (200, 200, 200), pygame.Rect((i[0], i[1], 600, 50)))
        pygame.draw.rect(window, (100, 100, 100), pygame.Rect((k*580 + i[0], i[1], 20, 50)))

    textMusicVolume = text_font.render(("Music Volume: " + str(round(musicVolume * 100)) + "%"), True, (50, 50, 50))
    window.blit(textMusicVolume, (100, 310))
    textButtonVolume = text_font.render(("Button Volume: " + str(round(buttonVolume * 100)) + "%"), True, (50, 50, 50))
    window.blit(textButtonVolume, (100, 210))
    textSfxVolume = text_font.render(("SFX Volume: " + str(round(sfxVolume * 100)) + "%"), True, (50, 50, 50))
    window.blit(textSfxVolume, (100, 110))

    # Reset game
    box_rect = box.get_rect(midright=(600, 50))
    window.blit(box, box_rect)
    textReset = text_font.render(("Reset game"), True, (50, 50, 50))
    window.blit(textReset, textReset.get_rect(center=box_rect.center))
    if Buttons.mouse and box_rect.collidepoint(pygame.mouse.get_pos()):
        save_object("")
        sys.exit()

    # Back to menu button
    back_rect = back.get_rect(midleft=(200, 50))
    window.blit(back, back_rect)
    if Buttons.mouse and back_rect.collidepoint(pygame.mouse.get_pos()):
        buttonPress.play()
        ID = -1


# The menu where you select levels, collectibles, or settings
def menu(natural):
    global ID, locked, unlocked, introC, l1C, l2C, l3C, l4C, l5C, l6C, l7C, l8C, l9C, l10C, setting, collectible, song, destructPlatform, killPlatform
    if song != 0:
        song = 0
        mixer.music.stop()
        mixer.music.load("sound/starbound.mp3")
        mixer.music.play(-1)
    window.fill("Light Blue")

    if natural:

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
        window.blit(setting, setting_rect)
        window.blit(unlocked, Ui)
        tempText = text_font.render("Intro", True, "Black")
        window.blit(tempText, tempText.get_rect(center=Ui.center))

        level_data = [
            (U1, "lvl.1", 1, introC),
            (U2, "lvl.2", 2, l1C),
            (U3, "lvl.3", 3, l2C),
            (U4, "lvl.4", 4, l3C),
            (U5, "lvl.5", 5, l4C),
            (U6, "lvl.6", 6, l5C),
            (U7, "lvl.7", 7, l6C),
            (U8, "lvl.8", 8, l7C),
            (U9, "lvl.9", 9, l8C),
            (U10, "lvl.10", 10, l9C),
            (Uec, "End", 11, l10C)]

        for rect, text, level_id, completed in level_data:
            if not completed:
                window.blit(locked, rect)
            else:
                window.blit(unlocked, rect)
                tempText = text_font.render(text, True, "Black")
                window.blit(tempText, tempText.get_rect(center=rect.center))
                if Buttons.mouse and rect.collidepoint(pygame.mouse.get_pos()):
                    buttonPress.play()
                    ID = level_id

        if Buttons.mouse:
            if collectible_rect.collidepoint(pygame.mouse.get_pos()):
                buttonPress.play()
                ID = -3
            if setting_rect.collidepoint(pygame.mouse.get_pos()):
                buttonPress.play()
                ID = -2
            if Ui.collidepoint(pygame.mouse.get_pos()):
                buttonPress.play()
                ID = 0

        window.blit(text_font.render("The Game", True, "Black"), text_font.render("The Game", True, "Black").get_rect(center=(400, 50)))

    # Create special platforms
    if ID == 1:
        killPlatform = [[700, 200], [600, 100]]
    if ID == 2:
        killPlatform = [[860, -50]]
        destructPlatform = [[600, 80]]


# The intro level
def intro():
    global temp, introC, ID,  speed, jumpSpeed, jump, Gear, destructPlatform, killPlatform
    platforms = [[30, 350], [190, 350], [700, 300], [400, 250]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline((player_rect.bottomleft[0]+24, player_rect.bottomleft[1]), (player_rect.bottomright[0]-24, player_rect.bottomright[1])):
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

        # Shoes for jumping
        if not jump:
            if jumpShoesC.get_rect(topleft=(platform_rect.x+250, platform_rect.y+200)).colliderect(player_rect):
                jump = True
        else:
            tempText = text_font.render("Collectible found, you can now jump!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))

        # Win conditions
        window.blit(fin, (platform_rect.x+1000, platform_rect.y))
        if player_rect.x-platform_rect.x >= 1000:
            introC = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2
        for i in killPlatform:
            if platformD.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).colliderect(player_rect):
                temp = 2


def l1():
    global temp, l1C, l1c, ID, speed, jumpSpeed
    platforms = [[30, 350], [190, 350], [700, 300], [400, 250], [900, 350], [1100, 250]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform1.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline((player_rect.bottomleft[0]+24, player_rect.bottomleft[1]), (player_rect.bottomright[0]-24, player_rect.bottomright[1])):
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
            if 0 <= grass < 1:
                window.blit(grass1, grass1.get_rect(midbottom=(platform_rect.x+i[0]+80, platform_rect.y+i[1])))
            elif 1 <= grass < 2:
                window.blit(grass2, grass2.get_rect(midbottom=(platform_rect.x+i[0]+80, platform_rect.y+i[1])))
            else:
                window.blit(grass3, grass3.get_rect(midbottom=(platform_rect.x+i[0]+80, platform_rect.y+i[1])))

        # Collectible
        if not l1c:
            if gunC.get_rect(topleft=(platform_rect.x+500, platform_rect.y+100)).colliderect(player_rect):
                l1c = True
                Gear.l1ce = True
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
        for i in killPlatform:
            if platformD.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).colliderect(player_rect):
                temp = 2


def l2():
    global temp, l2C, l2c, ID, speed, jumpSpeed
    platforms = [[30, 350], [190, 350], [450, 350], [610, 370], [850, 370], [1050, 270], [830, 170], [830, 30], [1050, 50], [1250, 130]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform2.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline((player_rect.bottomleft[0]+24, player_rect.bottomleft[1]), (player_rect.bottomright[0]-24, player_rect.bottomright[1])):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w:
                    speed = jumpSpeed

        # Graphics
        window.blit(bg2, bg_rect)
        if speed != 0:
            window.blit(player2Jump, player_rect)
        else:
            window.blit(player2, player_rect)
        for i in platforms:
            window.blit(platform2, (platform_rect.x+i[0], platform_rect.y+i[1]))

        # Collectible
        if not l2c:
            if swordC.get_rect(topleft=(platform_rect.x+450, platform_rect.y+50)).colliderect(player_rect):
                l2c = True
                Gear.l2ce = True
                Gear.l1ce = False
            window.blit(swordC, (platform_rect.x+500, platform_rect.y+100))
        else:
            tempText = text_font.render("Collectible found!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))

        # Win conditions
        window.blit(fin, (platform_rect.x+1600, platform_rect.y))
        if player_rect.x-platform_rect.x >= 1600:
            l2C = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2
        for i in killPlatform:
            if platformD.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).colliderect(player_rect):
                temp = 2


def l3():
    global temp, l3C, l3c, ID, speed, jumpSpeed
    platforms = [[30, 375], [330, 375], [630, 375], [930, 375], [1230, 375], [1530, 375], [1830, 375], [2130, 375], [2430, 375], [2730, 375], [3030, 375], [3330, 375], [3630, 375], [3930, 375], [4230, 375], [4530, 375], [4830, 375], [5130, 375], [5430, 375], [5730, 375], [6030, 375], [6330, 375]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform2.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline((player_rect.bottomleft[0]+24, player_rect.bottomleft[1]), (player_rect.bottomright[0]-24, player_rect.bottomright[1])):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w:
                    speed = jumpSpeed

        # Graphics
        window.blit(bg3, bg_rect)
        if speed != 0:
            window.blit(player3Jump, player_rect)
        else:
            window.blit(player3, player_rect)
        for i in platforms:
            window.blit(platform2, (platform_rect.x+i[0], platform_rect.y+i[1]))

        # Collectible
        if not l3c:
            if swordC.get_rect(topleft=(platform_rect.x+450, platform_rect.y+50)).colliderect(player_rect):
                l3c = True
                Gear.l3ce = True
                Gear.l2ce = False
                Gear.l1ce = False
            window.blit(eyeC, (platform_rect.x+500, platform_rect.y+100))
        else:
            tempText = text_font.render("Collectible found!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))

        # Win conditions
        window.blit(fin, (platform_rect.x+6500, platform_rect.y))
        if player_rect.x-platform_rect.x >= 6500:
            l3C = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2


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
    global temp, l9C, l9c, ID, speed, jumpSpeed
    platforms = [[30, 375], [330, 375], [630, 375], [930, 375], [1230, 375], [1530, 375], [1830, 375], [2130, 375], [2430, 375], [2730, 375], [3030, 375], [3330, 375], [3630, 375], [3930, 375]]
    if temp == 0:
        if player_rect.bottom < 400:
            player_rect.bottom += 8

        # Collisions with platforms
        for i in platforms:
            if platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline(player_rect.bottomleft, player_rect.bottomright):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w:
                    speed = jumpSpeed

        # Graphics
        window.blit(bg9, bg_rect)
        window.blit(bg9text, (bg_rect[0]*2, 0))
        if speed != 0:
            window.blit(player1Jump, player_rect)
        else:
            window.blit(player1, player_rect)
        for i in platforms:
            window.blit(platform, (platform_rect.x+i[0], platform_rect.y+i[1]))


        # Collectible
        if not l9c:
            if gunC.get_rect(topleft=(platform_rect.x+900, platform_rect.y+100)).colliderect(player_rect):
                l9c = True
                Gear.l9ce = True
            window.blit(gunC, (platform_rect.x+900, platform_rect.y+100))
        else:
            tempText = text_font.render("Collectible found!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 50)))

        # Win conditions
        window.blit(fin, (platform_rect.x+4000, platform_rect.y))
        if player_rect.x-platform_rect.x >= 4000:
            l9C = True
            temp = 1

        # Loss conditions
        if player_rect.bottom >= 400:
            temp = 2


def l10():
    global ID, l10C
    window.fill("Red")
    ID = -1
    l10C = True


def end_credits():
    global ID, platform_rect, song
    stop = 2750
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
    tempText = text_font.render("HR Department", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1400)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1450)))
    tempText = text_font.render("Risk Management Department", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1550)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1600)))
    tempText = text_font.render("Lead Rizz Management", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1700)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1750)))
    tempText = text_font.render("The Rizzler", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1850)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+1900)))
    tempText = text_font.render("Special thanks to:", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2000)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2050)))
    tempText = text_font.render("Thanks for motivating me <3!", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2150)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2200)))
    tempText = text_font.render("People we unfortunately lost during the way", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2300)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2350)))
    tempText = text_font.render("PR Department", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2450)))
    tempText = text_font.render("Viktor Lennartsson", True, "White")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+2500)))
    if platform_rect.y >= -(stop-200)*2:
        platform_rect.y -= 1
    if Buttons.space:
        ID = -1
        platform_rect.topleft = (0, 0)
        buttonPress.play()
    tempText = text_font.render("Thank you for playing", True, "Pink")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+stop+25)))
    tempText = text_font.render("Press space to return to menu", True, "Pink")
    window.blit(tempText, tempText.get_rect(midtop=(400, platform_rect.y/2+stop-25)))


# The main play function,take cares of which levels or menus are open
def play():
    global loop1, ID, temp, speed, jumpSpeed, fireTime, destructPlatform, grass, killPlatform

    # Grass
    if grass > 3:
        grass = 0
    grass += 0.01

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
            if ID in [3]:
                speed -= 0.25
            else:
                speed -= 1
        if Buttons.w and Gear.l9ce:
            speed = jumpSpeed/2

        # Use weapons
        if Buttons.space:
            if time.time()-fireTime > 3:
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
        menu(True)
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

    # When the level is over, check if the player wants the next level or the menu
    if temp == 1:
        if Buttons.mouse:
            buttonPress.play()
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
            else:
                ID += 1
                destructPlatform = []
                killPlatform = []
                menu(False)
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (-50, 0)
        # Graphics
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Level "+str(ID)+" Complete!", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Next Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))

    # Restart level or return to menu after loss
    elif temp == 2:
        if Buttons.mouse:
            buttonPress.play()
            if pygame.mouse.get_pos()[0] <= screen[0]/2:
                ID = -1
                destructPlatform = []
                killPlatform = []
            # Spawn destructible platforms
            menu(False)
            temp = 0
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (0, 0)
        # Graphics
        else:
            window.fill("Light Blue")
            tempText = text_font.render("Level failed", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(400, 80)))
            tempText = text_font.render("Main menu", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(200, 200)))
            tempText = text_font.render("Restart Level", True, "Black")
            window.blit(tempText, tempText.get_rect(center=(600, 200)))

    elif ID in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and temp == 0:
        # Back to menu button
        back_rect = back.get_rect(center=(200, 50))
        window.blit(back, back_rect)
        if Buttons.mouse and back_rect.collidepoint(pygame.mouse.get_pos()):
            buttonPress.play()
            ID = -1
            destructPlatform = []
            killPlatform = []
            player_rect.bottomleft = (50, 0)
            platform_rect.topleft = (0, 0)
            bg_rect.topleft = (0, 0)

        # Firing and destructible platforms
        fire()
        for i in killPlatform:
            window.blit(platformD, (platform_rect.x+i[0], platform_rect.y+i[1]))
        for i in destructPlatform:
            if ID == 2:
                window.blit(platform2cracked, (platform_rect.x+i[0], platform_rect.y+i[1]+8))
        for i in destructPlatform:
            if platform.get_rect(topleft=(platform_rect.x+i[0], platform_rect.y+i[1])).clipline((player_rect.bottomleft[0]+24, player_rect.bottomleft[1]), (player_rect.bottomright[0]-24, player_rect.bottomright[1])):
                player_rect.bottom = platform_rect.y+i[1]
                if Buttons.w and jump:
                    speed = jumpSpeed


# Start the mayhem
while loop1:
    play()
    pygame.display.flip()
    pygame.time.Clock().tick(60)


# Save things
toBeSaved = {"introC": introC, "l1C": l1C, "l2C": l2C,
             "l3C": l3C, "l4C": l4C, "l5C": l5C, "l6C": l6C,
             "l7C": l7C, "l8C": l8C, "l9C": l9C, "l10C": l10C,
             "l1c": l1c, "l2c": l2c, "l3c": l3c, "l4c": l4c,
             "l5c": l5c, "l6c": l6c, "l7c": l7c, "l8c": l8c,
             "l9c": l9c, "l10c": l10c, "jump": jump, "l1ce": Gear.l1ce,
             "l2ce": Gear.l2ce, "l3ce": Gear.l3ce, "l4ce": Gear.l4ce,
             "l5ce": Gear.l5ce, "l6ce": Gear.l6ce, "l7ce": Gear.l7ce,
             "l8ce": Gear.l8ce, "l9ce": Gear.l9ce, "l10ce": Gear.l10ce,
             "musicVolume": musicVolume, "sfxVolume": sfxVolume, "buttonVolume": buttonVolume}
print(toBeSaved)
save_object(toBeSaved)
sys.exit()
