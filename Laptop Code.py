import pygame
import time
import psutil
pygame.init()

#fps,width,height
clock = pygame.time.Clock()
width = round(1920/2)
height = round(1080*(2/5))

#attributes
pygame.display.set_caption("Car Controller Extreme")
icon = pygame.image.load("images\\unnamed.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width,height))


#images
background = pygame.image.load("images\\black.png")
enabled = pygame.image.load("images\\enable.png")
disabled = pygame.image.load("images\\disabled.png")
car = pygame.image.load("images\\Car.png") #166x216
oneWheel = pygame.image.load("images\\fwd.png") #79x76
fwd_arr = pygame.image.load("images\\arrow forward.png")
bwd_arr = pygame.image.load("images\\arrow backward.png")
depl = pygame.image.load("images\\depleted.png")
#text
logo = pygame.font.Font("images\\Platinum Sign Over.ttf",35)
reg = pygame.font.Font("images\\Platinum Sign Over.ttf",20)
reg1 = pygame.font.Font("images\\Platinum Sign Over.ttf",17)
health_scr = logo.render(str(" MECHATRONICS CHNL"), True, (0, 0, 0))
statsTXT = reg.render(str("STATS"), True, (255, 255, 255))
controlsTXT = reg.render(str("CONTROLS"), True, (255, 255, 255))
boostTXT = reg1.render(str("BOOST -"), True, (255, 255, 255))
cpuTXT = reg1.render(str("CPU     -"), True, (255, 255, 255))
batteryTXT = reg1.render(str("BTRY  -"), True, (255, 255, 255))
#starting variables
running = True
enable = False
boost = False
boost_cooldown = False
depleted = False
drive = 1    # 1 = 4wd , 2 = fwd , 3 = bwd
enx, eny = 20,120


def graphics(enable,drive):
    pygame.draw.rect(screen, (0, 0, 0), [0, 50, 510, 10])
    pygame.draw.rect(screen, (0, 0, 0), [0, 100, 510, 10])
    pygame.draw.line(screen, (0, 0, 0), (250, 50), (250, 500), 5)
    pygame.draw.line(screen, (0, 0, 0), (510, 50), (510, 500), 5)  # 2nd line
    pygame.draw.line(screen, (0, 0, 0), (505, 58), (550, 0), 10)  # sideways line
    screen.blit(health_scr, (0, 0))
    screen.blit(statsTXT, (265, 65))
    screen.blit(boostTXT, (265, 156))
    screen.blit(controlsTXT, (10, 65))
    screen.blit(cpuTXT, (265, 186))
    screen.blit(batteryTXT, (265, 216))
    if enable:
        screen.blit(enabled, (enx, eny))
    else:
        screen.blit(disabled, (enx, eny))
    if drive == 1:
        screen.blit(oneWheel, (650 + 166, (height / 2) - 108))
        screen.blit(oneWheel, (650 + 166, (height / 2) + 19))
    elif drive == 2:
        screen.blit(oneWheel, (650 + 166,(height/2)-108))
    elif drive == 3:
        screen.blit(oneWheel, (650 + 166, (height / 2)+19))
    screen.blit(fwd_arr, (650+67, (height / 2) - (108 + 83)))
    screen.blit(bwd_arr, (650 + 67, (height / 2) + 120))
def dis_cpu():
    raw = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    bar1 = (raw*1.25)
    if battery == "None":
        bar2 = (battery*1.25)
        pygame.draw.rect(screen, (0, 0, 0), [370, 220, 125, 15])
        pygame.draw.rect(screen, (255, 165, 0), [370, 220, bar2, 15])
    else:
        pygame.draw.rect(screen, (0, 0, 0), [370, 220, 125, 15])
    pygame.draw.rect(screen, (0, 0, 0), [370, 190, 125, 15])
    pygame.draw.rect(screen, (255, 165, 0), [370, 190, bar1, 15])

while running:
    clock.tick(15)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        if enable and (not keys[pygame.K_F1]):
            enable = False
            print("done")
        elif keys[pygame.K_F1] and (not enable):
            enable = True
            print("on")
            time.sleep(.3)
    if keys[pygame.K_LSHIFT] and not boost_cooldown and not boost:
        start_time = time.time()
        boost = True
    pygame.draw.rect(screen, (0, 255, 0), [370, 160, 125, 15])

    if boost:
        end_time = time.time()
        timer = end_time - start_time
        bar = round(timer * 12.5)

        pygame.draw.rect(screen, (255,165,0), [370, 160, bar, 15])
        if (timer >= 9.9):
            boost = False
            boost_cooldown = True
            start_time = time.time()
            print("done")

    if boost_cooldown:
        end_time = time.time()
        timer = end_time - start_time
        bar = round(timer*25)
        bar = 125 - bar
        pygame.draw.rect(screen, (0, 0, 0), [370, 160, bar, 15])

        if (timer >= 4.9):
            boost_cooldown = False
            print("done")


    dis_cpu()
    screen.blit(car, (650, (height/2)-108))
    graphics(enable,drive)


    pygame.display.update()


