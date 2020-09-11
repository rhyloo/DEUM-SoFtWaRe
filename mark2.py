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

class Config(object):
    #Screen_Constants
    screen_width = 1920
    screen_height = 1080
    screen_constant_distance = 25
    bottom_x_position = 0
    #Objects
    logo = pygame.image.load('C:/Users/jorge/Proyectos/DEUM-SoFtWaRe/logo.png')
    textinput = pygame_textinput.TextInput(initial_string = ">>>", font_family = "monospaced", font_size= 25,     text_color = (255,255,255))
    display = (screen_width,screen_height)
    clock = pygame.time.Clock()
    title = "DEUM SoFtWaRe"
    old_surface_2D = pygame.Surface((0, 0))
    old_surface_3D = pygame.Surface((0, 0))
    run = True
    BLUE_color = (0,0,255)

    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Config.screen_width
        Config.screen_height
        Config.screen_constant_distance
        Config.bottom_x_position
        Config.logo
        Config.textinput
        Config.display
        Config.clock
        Config.title
        Config.old_surface_2D
        Config.old_surface_3D

class Point:
    coord_x = 0
    coord_y = 0

    def __init__(self):
        pass
    @classmethod
    def draw_2D(self):
        fig = pylab.figure(figsize=[px_inches(Config.screen_width)/2,px_inches(Config.screen_height)], dpi = 100)
        ax = fig.gca()
        ax.plot(Point.coord_x,Point.coord_y, marker='o', markersize=3, color="red")
        ax.grid(True)
        #ax.axis([-75,75,50,-50])
        ax.axis('on')

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        screen = pygame.display.get_surface()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (0,0))
        Config.old_surface = surf #Almancenas el Surface iniciado en otra variable temporal.
    @classmethod
    def draw_3D(self):
        fig = pylab.figure(figsize=[px_inches(Config.screen_width)/2,px_inches(Config.screen_height)], dpi = 100)
        ax = plt.axes(projection='3d')
        ax.scatter3D(Point.coord_x, Point.coord_y, 0 ,cmap='Greens');
        ax.grid(True)
        #ax.axis([-75,75,50,-50])
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        screen = pygame.display.get_surface()
        size = canvas.get_width_height()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, ((Config.screen_width)/2,0))
        Config.old_surface = surf #Almancenas el Surface iniciado en otra variable temporal.

def px_inches(value):
    return (value*0.01)

def wihtd(splited_command_input):
    if splited_command_input[0] == "exit" or splited_command_input[0] == "Exit":
        Config.run = False
    elif (splited_command_input[0] == "point" or splited_command_input[0] == "Point" and (len(splited_command_input)>=6)):
        draw_points(splited_command_input)
    else:
        print("That command doesn\'t exists, please type Help for more information")
        print(len(splited_command_input)) #Borrar al final
    return Config.run

def draw_points(splited_command_input):
    [Point.coord_x, Point.coord_y] = [float(splited_command_input[2]), float(splited_command_input[3])]
    Point.draw_2D()
    Point.draw_3D()


def main():
    #Start Pygame
    pygame.init()
    Config.init()
    window = pygame.display.set_mode(Config.display, HWSURFACE|RESIZABLE|DOUBLEBUF)
    pygame.display.set_icon(Config.logo)
    pygame.display.set_caption(Config.title)

    while Config.run:

        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                Config.run = False
            elif event.type == pygame.VIDEORESIZE:
                Config.screen_width = event.w
                Config.screen_height = event.h
                window = pygame.display.set_mode((event.w, event.h), HWSURFACE|RESIZABLE|DOUBLEBUF)
                Point.draw_2D()
                Point.draw_3D()
                window.blit(Config.old_surface_2D, (0,0))
                window.blit(Config.old_surface_3D, ((Config.screen_width)/2,0))

        if Config.textinput.update(events):
            command_input = Config.textinput.get_text()[3:]
            splited_command_input = re.split('[(,)\s]', command_input)
            print(splited_command_input)#Borrar al final
            Config.run = wihtd(splited_command_input)
            Config.textinput.clear_text()
        pygame.draw.rect(window,Config.BLUE_color,(Config.bottom_x_position,Config.screen_height-Config.screen_constant_distance,Config.screen_width,Config.screen_constant_distance))
        window.blit(Config.textinput.get_surface(), (Config.bottom_x_position,Config.screen_height-Config.screen_constant_distance))
        pygame.display.update()
        Config.clock.tick(60)
    pygame.quit()
if __name__== "__main__":
    main()
