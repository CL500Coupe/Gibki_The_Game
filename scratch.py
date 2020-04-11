import time
import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()

#variables
display_width = 1000
display_height =800

image_width1 = 729
image_width2 = 116
image_width3 = 361
image_width4 = 187
image_width5 = 47
image_width6 = 615
image_width7 = 184

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1000,800))
game_icon = pygame.image.load("icon.png")
gibki_the_game = pygame.image.load("Gibki-The-Game.png")
info = pygame.image.load("info.png")
button_play = pygame.image.load("Graj.png")
button_play2 = pygame.image.load("Graj_jasne.png")
button_options = pygame.image.load("Sterowanie.png")
button_options2 = pygame.image.load("Sterowanie_jasne.png")
button_quit = pygame.image.load("Wyjd.png")
button_quit2 = pygame.image.load("Wyjdz_jasne.png")
button_about = pygame.image.load("about.png")
button_about2 = pygame.image.load("about_jasne.png")
button_powrot = pygame.image.load("powrot.png")
button_powrot2 = pygame.image.load("powrot_jasne.png")

x_center1 = display_width / 2 - image_width1 / 2
x_center2 = display_width / 2 - image_width2 / 2
x_center3 = display_width / 2 - image_width3 / 2
x_center4 = display_width / 2 - image_width4 / 2
x_center5 = display_width / 2 - image_width6 / 2
x_center7 = display_width / 2 - image_width7 / 2

y1= 50
y2 = 200
y3 = 350
y4 = 500
y5 = 300
y7 = 650
pygame.init()
pygame.display.set_icon(game_icon)
display_surface = pygame.display.set_mode((display_width,display_height)) #width-height
pygame.display.set_caption('Gibki The Game')   #game title

#BLOKUJE MUZYKE MENU ZEBY NIE PRZESZKADZAŁO
# muzyka tło
music = pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

def about_screen():
    #petla dzieki ktorej wyswietla sie screen about
    about = True

    while about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        display_surface.blit(background, [0, 0])
        display_surface.blit(gibki_the_game, (x_center1, y1))
        display_surface.blit(info,(x_center5,y5))
        back_button()




        #update screena zawsze na koncu
        pygame.display.update()
        clock.tick(15)


def back_button(): #button POWROT
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if x_center7 + image_width4 > mouse[0] > x_center7 and y7 + 50 > mouse[1] > y7:

        display_surface.blit(button_powrot2, (x_center7, y7))
        if click[0] == 1:
            menu( )
    else:
        display_surface.blit(button_powrot, (x_center7, y7))


def button():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    # guzik play
    if x_center2 + image_width2 > mouse[0] > x_center2 and y2 + 50 > mouse[1] > y2:

        display_surface.blit(button_play2, (x_center2, y2))
    else:
        display_surface.blit(button_play, (x_center2, y2))

    # guzik sterowanie
    if x_center3 + image_width3 > mouse[0] > x_center3 and y3 + 50 > mouse[1] > y3:

        display_surface.blit(button_options2, (x_center3, y3))
    else:
        display_surface.blit(button_options, (x_center3, y3))

    # guzik wyjdz
    if x_center4 + image_width4 > mouse[0] > x_center4 and y4 + 50 > mouse[1] > y4:

        display_surface.blit(button_quit2, (x_center4, y4))
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        display_surface.blit(button_quit, (x_center4, y4))

    # guzik about
    if 900 + image_width5 > mouse[0] > 900 and 700 + 50 > mouse[1] > 700:

        display_surface.blit(button_about2, (900, 700))
        if click[0] == 1:
            about_screen()

    else:
        display_surface.blit(button_about, (900, 700))


def menu():  #main menu
    #petla dzieki ktorej dziala menu i cale to gowno sie trzyma
    about = True


    while about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display_surface.blit(background,[0,0])
        display_surface.blit(gibki_the_game,(x_center1,y1))
        button()
        pygame.display.update()
        clock.tick(15)





while True: #main game loop


    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    menu()
    clock.tick(60)
    pygame.display.update()
    pygame.display.flip()




