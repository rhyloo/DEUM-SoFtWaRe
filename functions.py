
def wihtd(splited_command_input):
    if splited_command_input[0] == "exit" or splited_command_input[0] == "Exit":
        Config.run = False
    elif (splited_command_input[0] == "point" or splited_command_input[0] == "Point" and (len(splited_command_input)>=6)):
        draw_points(splited_command_input)
    else:
        print("That command doesn\'t exists, please type Help for more information")
        print(len(splited_command_input)) #Borrar al final
    return Config.run

def px_inches(value):
    return (value*0.01)

def draw_points(splited_command_input):
    [Point.coord_x,Point.coord_y] = [float(splited_command_input[2]), float(splited_command_input[3])]
    point.draw_2D()
    # Point.draw_3D()
