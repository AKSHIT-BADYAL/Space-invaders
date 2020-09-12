import pygame# using pygame module
import os# using os(opersting system module)
import time #using time module
import random # using random module
# adding font
pygame.font.init()
# def.display window
width,height=600,600
main_window=pygame.display.set_mode((width,height))
# naming the title or caption of the game
pygame.display.set_caption("Space-Invaders")

# IMPORTING IMAGES FOR ENIMY SPACE SHIP
tomato_spaceship = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
olivs_spaceship = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
grass= pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
# MAIN SPACE SHIP OF PLAYER
mango_spaceship = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

# importing or including images for their wepons -laser
tomato_laser= pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
olive_laser= pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
grass_laser= pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
# main player wepon
mango_laser= pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

# importing background image
# using pygame.transform.scale(())-to scale the image to the size of main window
sky_background= pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(width,height))


# def. a function that determines the main workflow of the game -as - when to quit and in how much frame rate game should run and makesit constant on all devices
def main():
    run=True
    speed=70
    level=1
    lives=6
    main_font= pygame.font.SysFont("Chiller",40)# styling the font and declaring its size
    clock=pygame.time.Clock()
    # placing or redeawing the background
    def redraw_window():
        main_window.blit(sky_background,(0,0))
        #ADDING -------------- TEXT------------ TO THE MAIN WINDOW------------------------------------"start"
        # showing or drawing the --" livetext "--- on the main window
        lives_lable= main_font.render(f"Lives:{lives}",1,(255,255,255))
        # showing or drawing the---"level text"-- on the main window
        level_lable= main_font.render(f"Level:{level}",1,(255,255,255))
        main_window.blit(lives_lable,(10,10))
        main_window.blit(level_lable,(width-level_lable.get_width()-10,10))


    while run:
        clock.tick(speed)
        redraw_window()
        # event to make the main window run forever until we press quit button on the top right in windows and top left in mac
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
main()