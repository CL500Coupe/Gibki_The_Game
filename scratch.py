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
image_width12 = 200


game_background = pygame.image.load('game_background.png')
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

#zdjecia do sterowania
button_arrows = pygame.image.load("keyboard_arrows.png")
button_spacebar = pygame.image.load("space_bar.png")
button_poruszanie = pygame.image.load("poruszanie.png")
button_rzut = pygame.image.load("rzut.png")

#paski zycia
player_sila1 = pygame.image.load("sila1.png")
player_sila2 = pygame.image.load("sila2.png")
player_sila3 = pygame.image.load("sila3.png")

player_celnosc1 = pygame.image.load("celnosc1.png")
player_celnosc2 = pygame.image.load("celnosc2.png")
player_celnosc3 = pygame.image.load("celnosc3.png")

player_inteligencja1 = pygame.image.load("inteligencja1.png")
player_inteligencja2 = pygame.image.load("inteligencja2.png")
player_inteligencja3 = pygame.image.load("inteligencja3.png")




#zdjecia postaci
player_maciej = pygame.image.load("maciej.png")
player_jakub = pygame.image.load("jakub.png")
player_fabian = pygame.image.load("fabian.png")

bright_maciej = pygame.image.load("maciej_bright.png")
bright_jakub = pygame.image.load("jakub_bright.png")
bright_fabian = pygame.image.load("fabian_bright.png")




x_center1 = display_width / 2 - image_width1 / 2
x_center2 = display_width / 2 - image_width2 / 2
x_center3 = display_width / 2 - image_width3 / 2
x_center4 = display_width / 2 - image_width4 / 2
x_center5 = display_width / 2 - image_width6 / 2
x_center7 = display_width / 2 - image_width7 / 2

#jakub na srodku
x_center12 = display_width / 2 - image_width12 / 2

#pozycje zdjecia sterowanie
x_center8 = 150
x_center9 = 500
x_center10 = 135
x_center11 = 600
x_center20 = 100

y1= 50
y2 = 200
y3 = 350
y4 = 500
y5 = 300
y7 = 700
#pozycje zdjecia sterowanie
y8 = 350
y9 = 390
y10 = 550
y11 = 550
y20 = 100

pygame.init()
pygame.display.set_icon(game_icon)
display_surface = pygame.display.set_mode((display_width,display_height)) #width-height
pygame.display.set_caption('Gibki The Game')   #game title

#BLOKUJE MUZYKE MENU ZEBY NIE PRZESZKADZAŁO
 #muzyka tło
music = pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)




def game_loop_rudy():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    fabian = True

    while fabian:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_surface.blit(game_background, [0, 0])
        back_button()

        pygame.display.update()

def game_loop_fabian():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    fabian = True

    while fabian:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_surface.blit(game_background, [0, 0])
        back_button()




        pygame.display.update()


def game_loop_maciej():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    maciej = True

    while maciej:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_surface.blit(game_background, [0, 0])
        back_button()




        pygame.display.update()


def players():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    # KUBA
    display_surface.blit(player_sila2, (x_center12, 350))
    display_surface.blit(player_celnosc1, (x_center12, 450))
    display_surface.blit(player_inteligencja3, (x_center12, 550))
    if x_center12 + image_width12 > mouse[0] > x_center12 and 0 + 200 > mouse[1] > 0:

        jakub_sound = pygame.mixer.Sound('kuba_sound.wav')
        pygame.mixer.Sound.stop
        pygame.mixer.Sound.play(jakub_sound, 1)
        pygame.mixer.Sound.set_volume(jakub_sound, 0.1)
        display_surface.blit(bright_jakub, (x_center12, 0))
        if click[0] == 1:
            game_loop_rudy()
    else:
        display_surface.blit(player_jakub, (x_center12, 0))

    # FABIAN
    display_surface.blit(player_sila3, (700, 350))
    display_surface.blit(player_celnosc2, (700, 450))
    display_surface.blit(player_inteligencja1, (700, 550))
    if 700 + image_width12 > mouse[0] > 700 and 0 + 200 > mouse[1] > 0:

        fabian_sound = pygame.mixer.Sound('fabian_sound.wav')
        pygame.mixer.Sound.stop
        pygame.mixer.Sound.play(fabian_sound, 1)
        pygame.mixer.Sound.set_volume(fabian_sound, 0.1)
        display_surface.blit(bright_fabian, (700, 0))
        if click[0] == 1:
            game_loop_fabian()

    else:
        display_surface.blit(player_fabian, (700, 0))

    #Maciej
    display_surface.blit(player_sila1, (100, 350))
    display_surface.blit(player_celnosc3, (100, 450))
    display_surface.blit(player_inteligencja2, (100, 550))
    if x_center20 + image_width12 > mouse[0] > x_center20 and 0 + 200 > mouse[1] > 0:

        display_surface.blit(bright_maciej, (x_center20, 0))
        maciej_sound = pygame.mixer.Sound('zamknij_ryj.wav')
        pygame.mixer.Sound.stop
        pygame.mixer.Sound.play(maciej_sound, 1)
        pygame.mixer.Sound.set_volume(maciej_sound, 0.1)
        if click[0] == 1:
            game_loop_maciej()

    else:
        display_surface.blit(player_maciej, (x_center20, 0))


def choose_player():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    choose = True



    while choose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




        display_surface.blit(background, [0, 0])
        players()
        back_button()

        pygame.display.update()







def controls_screen():
    controls = True


    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_surface.blit(background, [0, 0])
        display_surface.blit(gibki_the_game, (x_center1, y1))

        display_surface.blit(button_arrows, (x_center8, y8))
        display_surface.blit(button_spacebar, (x_center9, y9))
        display_surface.blit(button_poruszanie, (x_center10, y10))
        display_surface.blit(button_rzut, (x_center11, y11))

        back_button()

        pygame.display.update()






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


def back_button(): #button POWROT
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if x_center7 + image_width4 > mouse[0] > x_center7 and y7 + 50 > mouse[1] > y7:

        display_surface.blit(button_powrot2, (x_center7, y7))
        if click[0] == 1:
            menu()
    else:
        display_surface.blit(button_powrot, (x_center7, y7))


def button():
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    # guzik play
    if x_center2 + image_width2 > mouse[0] > x_center2 and y2 + 50 > mouse[1] > y2:

        display_surface.blit(button_play2, (x_center2, y2))
        if click[0] == 1:
            choose_player()
    else:
        display_surface.blit(button_play, (x_center2, y2))

    # guzik sterowanie
    if x_center3 + image_width3 > mouse[0] > x_center3 and y3 + 50 > mouse[1] > y3:

        display_surface.blit(button_options2, (x_center3, y3))
        if click[0] == 1:
            controls_screen()

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
    Menu = True


    while Menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display_surface.blit(background,[0,0])
        display_surface.blit(gibki_the_game,(x_center1,y1))
        button()
        pygame.display.update()






while True: #main game loop


    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    menu()

    pygame.display.update()
    pygame.display.flip()




