import pygame
from pygame.locals import *
import pygame_textinput
import re
import wx
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab
from pygame.locals import *

class Point:
    def __init__(self,point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y
    def draw(self):
        fig = pylab.figure(figsize=[4, 4], dpi = 100)
        ax = fig.gca()
        ax.plot(self.point_x,self.point_y, marker='o', markersize=3, color="red")
        ax.grid(True)
        #ax.axis([-75,75,50,-50])
        ax.axis('on')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        window = pygame.display.set_mode((1020, 800), DOUBLEBUF)
        screen = pygame.display.get_surface()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (0,0))
        #
        # screen.blit(surf, (0,0))
        # pygame.display.flip()
        #
        #
        #

def wihtd(splited_command_input):
    run = True
    if splited_command_input[0] == "exit" or splited_command_input[0] == "Exit":
        run = False
    elif (splited_command_input[0] == "point" or splited_command_input[0] == "Point" and (len(splited_command_input)>=6)):
        point = draw_points(splited_command_input)
    else:
        print("That command doesn\'t exists, please type Help for more information")
        print(len(splited_command_input))
    return run

def draw_points(splited_command_input):
    point = Point(float(splited_command_input[2]),float(splited_command_input[3]))
    point.draw()

def main():
    pygame.init()

    logo = pygame.image.load('logo.png')
    #image = pygame.image.load('logo.png')
    #bgd_image = pygame.image.load("background.png")
    textinput = pygame_textinput.TextInput(initial_string = ">>>", font_family = "monospaced", font_size= 25, text_color = (255,255,255))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen_width = 800
    screen_height = 600
    display = (screen_width,screen_height)
    # screen = pygame.display.set_mode(display)
    clock = pygame.time.Clock()

    fig = pylab.figure(figsize=[4, 4], dpi = 50)
    ax = fig.gca()
    ax.plot([-20,20],[-20,-20],linewidth=2,color='r')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    window = pygame.display.set_mode((1020, 800), RESIZABLE|DOUBLEBUF)
    #window = pygame.display.set_mode(display)
    screen = pygame.display.get_surface()
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == pygame.QUIT:
                run = False
        if textinput.update(events):
            command_input = textinput.get_text()[3:]
            splited_command_input = re.split('[(,)\s]', command_input)
            print(splited_command_input)
            run = wihtd(splited_command_input)
            textinput.clear_text()
        pygame.draw.rect(screen,(0,0,255),(0,800-25,1020,25))
        screen.blit(textinput.get_surface(), (0,800-22))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__=="__main__":
    main()
