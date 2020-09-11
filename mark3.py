import tkinter as tk
import os
import pygame
import re
import pygame_textinput
from pygame.locals import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


class Config(object):
    #Screen_Constants
    screen_width = 500
    screen_height = 25
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


def wihtd(splited_command_input):
    if splited_command_input[0] == "exit" or splited_command_input[0] == "Exit":
        Config.run = False
    elif (splited_command_input[0] == "point" or splited_command_input[0] == "Point" and (len(splited_command_input)>=6)):
        draw_points(splited_command_input)
    else:
        print("That command doesn\'t exists, please type Help for more information")
        print(len(splited_command_input)) #Borrar al final
    return Config.run
def hello():
    print ("hello!")

w, h = 500, 25

# Add a couple widgets. We're going to put pygame in `embed`.
root = tk.Tk()
menubar = tk.Menu(root)
root.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
filemenu.add_command(label="Nuevo",command=hello)
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

photo = tk.PhotoImage(file = "C:/Users/jorge/Proyectos/DEUM-SoFtWaRe/logo.png")
root.wm_title(Config.title)
root.iconphoto(False, photo)
embed = tk.Frame(root, width=w, height=h)
embed.grid(row = 2,columnspan=1)
#embed.pack()
# text = tk.Button(root, text='Blah.')
# text.pack()

# Tell pygame's SDL window which window ID to use
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

# The wxPython wiki says you might need the following line on Windows
# (http://wiki.wxpython.org/IntegratingPyGame).
os.environ['SDL_VIDEODRIVER'] = 'windib'

# Show the window so it's assigned an ID.
root.update()

# Usual pygame initialization
pos = 0
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig2 = Figure(figsize=(5, 4), dpi=100)
canvas2 = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
canvas2.draw()
ax = fig2.add_subplot(111, projection="3d")
t = np.arange(0, 3, .01)
ax.plot(t, 2 * np.sin(2 * np.pi * t))


canvas = FigureCanvasTkAgg(fig, master=root)
# canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas.draw()

canvas.get_tk_widget().grid(row = 0, column = 1)
# .pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
# canvas2.draw()
canvas2.get_tk_widget().grid(row = 0, column = 0)

toolbarFrame2 = tk.Frame(master=root)
toolbarFrame2.grid(row = 1, column = 0)
toolbar2 = NavigationToolbar2Tk(canvas2, toolbarFrame2)

toolbarFrame = tk.Frame(master=root)
toolbarFrame.grid(row = 1, column = 1)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)


pygame.display.init()
screen = pygame.display.set_mode(Config.display)
pygame.init()
Config.init()

while 1:


    # Do some pygame stuff
    events = pygame.event.get()
    if Config.textinput.update(events):
        command_input = Config.textinput.get_text()[3:]
        splited_command_input = re.split('[(,)\s]', command_input)
        print(splited_command_input)#Borrar al final
        Config.run = wihtd(splited_command_input)
        Config.textinput.clear_text()
    pygame.draw.rect(screen,Config.BLUE_color,(Config.bottom_x_position,Config.screen_height-Config.screen_constant_distance,Config.screen_width,Config.screen_constant_distance))
    screen.blit(Config.textinput.get_surface(), (Config.bottom_x_position,Config.screen_height-Config.screen_constant_distance))
    pygame.display.flip()
    Config.clock.tick(60)
    root.update()
    # Update the Tk display
tk.mainloop()
