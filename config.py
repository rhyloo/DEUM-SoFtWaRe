import tkinter as tk
import os
import pygame
import pygame_textinput
import os.path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def px_inches(value):
    return (value*0.01)

class Point(object):
    coord_x = 0
    coord_y = 0

    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Point.coord_x
        Point.coord_y
    @classmethod
    def draw_2D(self):
        fig = plt.Figure(figsize=[px_inches(Config.screen_width)/2,px_inches(Config.screen_height)], dpi=100)
        fig.add_subplot().plot(Point.coord_x,Point.coord_y, marker='o', markersize=3, color="red")
        canvas = FigureCanvasTkAgg(fig, master=Window_config.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 0, column = 1)
        toolbarFrame = tk.Frame(master=Window_config.root)
        toolbarFrame.grid(row = 1, column = 1)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

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


class Config(object):
#pygame
    #Screen_Constants
    screen_width = 1000
    screen_height = 800
    screen_constant_distance = 25
    bottom_x_position = 0
    textinput = pygame_textinput.TextInput(initial_string = ">>>", font_family = "monospaced", font_size= 25, text_color = (250,0,0))
    display = (screen_width,screen_height)
    title = "DEUM SoFtWaRe"
    clock = pygame.time.Clock()
    run = True
    BLUE_color = (30,60,120)
    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Config.screen_width
        Config.screen_height
        Config.screen_constant_distance
        Config.bottom_x_position
        Config.textinput
        Config.display
        Config.clock
        Config.title
class Window_config(object):
    root = tk.Tk()
    root.geometry("900x600")
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    editmenu = tk.Menu(menubar, tearoff=0)
    helpmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Window_config.root
        Window_config.menubar
        Window_config.filemenu
        Window_config.editmenu
        Window_config.helpmenu
class Filemenu(object):

    Window_config.filemenu.add_command(label="Nuevo")
    Window_config.filemenu.add_command(label="Abrir")
    Window_config.filemenu.add_command(label="Guardar")
    Window_config.filemenu.add_command(label="Cerrar")
    Window_config.filemenu.add_separator()
    Window_config.filemenu.add_command(label="Salir", command=Window_config.root.destroy)

    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Filemenu.Window_config.filemenu.add_command(label="Nuevo")
        Filemenu.Window_config.filemenu.add_command(label="Abrir")
        Filemenu.Window_config.filemenu.add_command(label="Guardar")
        Filemenu.Window_config.filemenu.add_command(label="Cerrar")
        Filemenu.Window_config.filemenu.add_separator()
        Filemenu.Window_config.filemenu.add_command(label="Salir", command=Window_config.root.destroy)
class Editmenu(object):

    Window_config.editmenu.add_command(label="Cortar")
    Window_config.editmenu.add_command(label="Copiar")
    Window_config.editmenu.add_command(label="Pegar")

    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Editmenu.Window_config.editmenu.add_command(label="Cortar")
        Editmenu.Window_config.editmenu.add_command(label="Copiar")
        Editmenu.Window_config.editmenu.add_command(label="Pegar")
class Helpmenu(object):

    Window_config.helpmenu.add_command(label="Ayuda")
    Window_config.helpmenu.add_separator()
    Window_config.helpmenu.add_command(label="Acerca de...")

    def __Init__(self):
        pass
    @classmethod
    def init(self):
        Helpmenu.Window_config.helpmenu.add_command(label="Ayuda")
        Helpmenu.Window_config.helpmenu.add_separator()
        Helpmenu.Window_config.helpmenu.add_command(label="Acerca de...")
