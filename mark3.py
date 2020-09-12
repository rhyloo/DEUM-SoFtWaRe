from  libraries import *


Window_config.init()
photo = tk.PhotoImage(file = "C:/Users/jorge/Proyectos/DEUM-SoFtWaRe/logo.png")
Window_config.root.wm_title(Config.title)
Window_config.root.iconphoto(False, photo)
embed = tk.Frame(Window_config.root, width = Config.screen_width, height = Config.screen_constant_distance)
embed.grid(row = 2,columnspan=2)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
Window_config.root.update()

def _3d():
    fig2 = Figure(figsize=(5, 4), dpi=100)
    canvas2 = FigureCanvasTkAgg(fig2, master=Window_config.root)
    canvas2.draw()
    ax = fig2.add_subplot(111, projection="3d")
    t = np.arange(0, 3, .01)
    ax.plot(t, 2 * np.sin(2 * np.pi * t))
    canvas2.get_tk_widget().grid(row = 0, column = 0)
    toolbarFrame2 = tk.Frame(master=Window_config.root)
    toolbarFrame2.grid(row = 1, column = 0)
    toolbar2 = NavigationToolbar2Tk(canvas2, toolbarFrame2)

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
    [Point.coord_x,Point.coord_y] = [float(splited_command_input[2]), float(splited_command_input[3])]
    Point.draw_2D()
    # Point.draw_3D()

pygame.display.init()
screen = pygame.display.set_mode(Config.display)
pygame.init()
Config.init()
Point.init()
while Config.run:

    events = pygame.event.get()
    for event in events:
        print(event)
    if Config.textinput.update(events):
        command_input = Config.textinput.get_text()[3:]
        splited_command_input = re.split('[(,)\s]', command_input)
        print(splited_command_input)#Borrar al final
        Config.run = wihtd(splited_command_input)
        Config.textinput.clear_text()
    Window_config.root.update()
    pygame.draw.rect(screen,Config.BLUE_color,(0,0,Config.screen_width,25))
    screen.blit(Config.textinput.get_surface(), (0,0,Config.screen_width,25))
    pygame.display.flip()
    Config.clock.tick(120)
# tk.mainloop()
pygame.quit()
Window_config.root.destroy

# threading.Thread(target=five_seconds).start()
