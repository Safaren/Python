import PySimpleGUI as sg
import math
import time
import sys
from midiutil import MIDIFile
import pygame
import os


global easy
easy = True
track = 0
channel = 9
sound_time = 0
duration = 1
tempo = 120
volume = 200

midi = MIDIFile(1)
midi.addTempo(track, sound_time, tempo)
midi.addTrackName(track, sound_time, "button")

notes = [(81,4)]

button_size = (7, 3)

player = 'X'
computer = 'O'
current_player = player



screen_width, screen_height = sg.Window.get_screen_size()

suma = 0
suma_co = 3
players = ['O','X']
table = [['' for _ in range(3)] for _ in range(3)]


FILE_TIMES = "Puntuaciones.txt"

time_ini = time.time()

def calculate_time(time_ini,time_current):
    time_end = time_current - time_ini
    seconds = time_end
    hours = int(time_end / 60 / 60)
    seconds -= hours * 60 * 60
    minutes = int(time_end / 60)
    seconds -= minutes *60 
    return  f"{hours:02d}:{minutes:02d}:{int(seconds):02d}"

def main_screen():
    
    style_button = {'button_color':('#630b57','GREEN'), \
                'size': (7, 3), 'font': ('Helvetica', 20 , 'bold' )}

    style_text = {'size':20,'text_color':'#630b57', \
                'justification': 'center', 'font':'bold', \
                'background_color': '#E4F1CD', 'expand_x': True}

    layout =[
            [sg.Text("Hola", key='-Estado-', **style_text)],
            
            [[sg.Button("", key=f"-{i*3+n+1}-", **style_button) \
                for n in range(3)]for i in range(3)],
            [sg.Button("Salir", key="-OK-", **style_button),\
            sg.Button("Restart", key="-RS-", **style_button)]]
    window_home = sg.Window("Tres en raya", layout , margins=(10, 10) )

    return window_home

def start_screen():
    global player_name,easy
    layout_start = [
        [sg.Text("Elige O o X, las X empiezan.")],
        [sg.Radio("X", "Ficha",key ="X", default=True),\
        sg.Radio("O", "Ficha",key ="O", default=False)],
        [sg.Checkbox("Facil", key="-dif-", default=False)],
        [sg.Button("Aceptar", key="-OK-"),\
         sg.Button("Cancelar",    key="-CANCEL-")],
         [sg.Text("Jugador:"),sg.Input(key="-name-"),\
          sg.Button("Puntaciones", key="-Pun-")]
    ]
    window_start = sg.Window("Elige dificultad", layout_start)

    while True:
        event, values = window_start.read()  # Leemos los eventos y valores de la ventana
        opcion = ''
        if event == sg.WIN_CLOSED or event == "-CANCEL-":  # Si se cierra la ventana, salimos del bucle
            sys.exit(0)
        elif event == "-Pun-":
            window_start.close() 
            screen_time()
        elif event == "-OK-":
           
            if values["O"] == True:
                opcion = "O"
            else:
                opcion = "X"
            if values["-name-"] == "":
                player_name = "Player: " + opcion
            else:
                player_name =(values["-name-"])
            easy = values["-dif-"]
            print(easy)
            window_start.close() 
            return opcion 
    

def reset(screen):
    global table, current_player, computer, player
    if screen:
        for n in range(1,10):
                window.Element(f"-{n}-").Update(text="")
    pygame.mixer.music.unload()
    pygame.mixer.music.stop
    load_sound()
    table = [['' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'
    current_player = player
    

def load_times(file):
    if os.path.exists(file):
        f = open(file,"a+",  encoding='utf-8')
        f.seek(0,os.SEEK_END)
    else: 
        f = open(FILE_TIMES,"w+", encoding='utf-8')
    return f

def show_times():
    if os.path.exists(FILE_TIMES):
        with open(FILE_TIMES,"r") as f:
            showtext = f.read()
            print(showtext)
    else: 
        f = open(FILE_TIMES,"a+",  encoding='utf-8')
        showtext = ''
    f.close()
    return showtext

def save_times(score):
    file = load_times(FILE_TIMES)
    file.write(score + '\n')


    file.close()

def delete_times(file):
    os.remove(file)

def terminate_check():
    for y in range(0,3):
        for x in range(0,3):
            if table[y][x] == "":
                return False
    return True
def winner_check():
    for y in range(0,3):
        table_line = [table[x][y] for x in range(0,3)]
        if winner_check_line(table_line) == True:
            return True
        table_line = [table[y][x] for x in range(0,3)]
        if winner_check_line(table_line) == True:
            return True
            
    table_line = [table[0][0], table[1][1], table[2][2]]
    if winner_check_line(table_line) == True:
        return True
    table_line = [table[2][0], table[1][1], table[0][2]]
    if winner_check_line(table_line) == True:
        return True
    return False

def winner_check_line(line):
    for char in players:
        print(char)
        if line[0]==line[1]==line[2]==char:
            #Mostrar aviso ganador, volver a jugar
            print(f"Ha ganado: {char}")
            return True
    return False
        
def travel():
    for y in range(0,3):
        table_line = [table[x][y] for x in range(0,3)]
        if check_two_positions(table_line) == True:
            return True
        table_line = [table[y][x] for x in range(0,3)]
        if check_two_positions(table_line) == True:
            return True

def check_two_positions():
    for char in players:
        for y in range(0,3):
            # filas
            print(y)
            if (table[0][y]==table[1][y]==char and empty_box(2,y)):
                draw_box(2,y)
                return True
            elif (table[0][y]==table[2][y]==char and empty_box(1,y)):
                draw_box(1,y)
                return True
            elif (table[1][y]==table[2][y]==char and empty_box(0,y)):
                draw_box(0,y)
                return True
            #columnas
            elif  (table[y][0]==table[y][1]==char and empty_box(y,2)):
                draw_box(y,2)
                return True
            elif (table[y][0]==table[y][2]==char and empty_box(y,1)):
                draw_box(y,1)
                return True
            elif (table[y][1]==table[y][2]==char and empty_box(y,0)):
                draw_box(y,0)
                return True
            #diagonales
            elif (table[0][0]==table[1][1]==char)  and empty_box(2,2):
                draw_box(2,2)
                return True
            elif (table[1][1]==table[2][2]==char) and empty_box(0,0):
                draw_box(0,0)
                return True
            elif (table[0][0]==table[2][2]==char) and empty_box(1,1):
                draw_box(1,1)
                return True
            elif (table[2][0]==table[1][1]==char) and empty_box(0,2):
                draw_box(0,2)
                return True
            elif (table[0][2]==table[1][1]==char) and empty_box(2,0):
                draw_box(2,0)
                return True
            elif (table[2][0]==table[0][2]==char) and empty_box(1,1):
                draw_box(1,1)
                return True
    
    return False
def empty_box(x,y):
    if table[x][y]=='':
        return True
    else:
        return False


def draw_box(x,y):
    global current_player, window

    table[x][y] =computer
    window.Element('-'+str(x+1+(y*3))+'-').Update(text = computer)
   
    current_player = player
    
'''avoid that if you have 2 boxes 
    filled in the last column and the last row you can win'''
def smart_move():  
    global easy
    xemp = 3 
    if easy==False:
        count = 0
        for y in range(0,3):
            x = 2
            if table[x][y]=='':
                count += 1
        for x in range(0,3):
            y = 2
            if table[x][y]=='':
                count +=1
                if xemp==3:
                    xemp = x
        if count != 4 :
            if count != 4 :
                count = 0
                for y in range(0,3):
                    x = 2
                    if table[x][y]=='':
                        count += 1
                for x in range(0,3):
                    y = 0
                    if table[x][y]=='':
                        count +=1
                        if xemp==3:
                            xemp = x
        else:                
            draw_box(xemp, y)
            return False


    return True
        
def box_random():
    
    if current_player == computer:
        
        if smart_move():
            if table[1][1]=='':
                draw_box(1,1)
                return
            for y in range(0,3): 
                for x in range(0,3):
                    if table[x][y]=='' : 
                        draw_box(x,y)
                        return

def screen_end(winer):
    score = calculate_time(time_ini,time.time())
    print(show_times())
    pygame.mixer.music.load("end.mid")
    pygame.mixer.music.play()
    layout_end = [
        [sg.Text(f"Ha ganado el jugador {winer}")],
        [sg.Text("Tu tiempo es: " + score)],
        [sg.Button("Nueva partida", key="-OK-"),\
         sg.Button("Tiempos", key="-Time-"),\
         sg.Button("Salir",    key="-Quit-")]
    ]
    score = 'Ganador: ' + winer + '; Tiempo de juego: '+ calculate_time(time_ini,time.time())
    save_times(score)
    window_end = sg.Window("Elige dificultad", layout_end)
    while True:
        event, values = window_end.read()  # Leemos los eventos y valores de la ventana
        if event == sg.WIN_CLOSED or event == "-Quit-":  # Si se cierra la ventana, salimos del bucle
            sys.exit(0)
        elif event == "-OK-":
           reset(False)
           window_end.close()
           screen_play()
           
        elif event == "-Time-":
            window_end.close()
            screen_time()
            

def screen_time():

    layout_time = [
        
        [sg.Output(size=(110,20),text_color ="#7CFF00",  font=('Helvetica', 20, 'bold'),\
                     background_color = 'Black', key = '-show-')],
        [sg.Button("Nueva partida", key="-OK-"),\
         sg.Button("Borrar archivo de tiempo", key="-delete-"),
         sg.Button("Salir",key="-Quit-")]
         ]

    window_time = sg.Window("Lista de tiempos y ganadores", layout_time, finalize=True)
    window_time['-show-'].update(show_times())
    window_time['-show-'].update(disabled = True)
    
    while True:
        event, values = window_time.read()  # Leemos los eventos y valores de la ventana
        
        if event == sg.WIN_CLOSED or event == "-Quit-":  # Si se cierra la ventana, salimos del bucle
            sys.exit(0)
        elif event == "-OK-":
            reset(False)
            window_time.close()
            screen_play()
        elif event =="-delete-":
            delete_times(FILE_TIMES)

           
    
def screen_play():
    global current_player, window, computer, player, players
    opcion = start_screen() 
    window = main_screen()
    player = opcion
    if player == 'O':
        computer = 'X'
        current_player = computer
        players = [player,computer]

    while  True:
        event, values = window.read(timeout=1000)
        width, height = window.current_location()
        
        print(event)

        
        if  event == sg.WIN_CLOSED or event == "-OK-":
            break
        elif event == '-RS-':
            reset(True)

        
        if current_player == player and event != sg.TIMEOUT_EVENT:
            if window.Element(event).ButtonText =="" :
                
                window.Element(event).Update(text = current_player)
                ind = int(event.replace("-"," "))
                
                y = math.ceil(ind/3)-1
                x = (ind-1)%3
                window.Element(event).Update(text = current_player)
                table[x][y] = player
                window.Element('-Estado-').Update(value = f"Turno de las {computer}")
                current_player = computer
                pygame.mixer.music.play()

            current_player = computer
        if event == sg.TIMEOUT_EVENT and current_player == computer:
            if winner_check():
                time.sleep(1)
                window.close()
                screen_end(player_name)
                
                
            check_two_positions()
            box_random()

        
                
            pygame.mixer.music.play()
            window.Element('-Estado-').Update(value = f"Turno del jugador: {player_name}")
            window.Refresh()
            if winner_check() :
                time.sleep(1)
                window.close()
                screen_end(computer)
            if terminate_check():
                time.sleep(1)
                window.close()
                screen_end('Empate')
                

def load_sound():
    if os.path.exists("button.mid"):
        pygame.mixer.music.load("button.mid")
    else:
        for i, (pitch, length) in enumerate(notes):
            midi.addNote(track, channel, pitch, sound_time + i * duration, length * duration, volume)
        

    # Escribir el archivo MIDI a disco
        with open("button.mid", "wb") as midi_file:
            midi.writeFile(midi_file)
        pygame.mixer.music.load("button.mid")
    for n in range(50,81):
        notes.append((n,4))
    if not (os.path.exists("end.mid")):
        for i, (pitch, length) in enumerate(notes):
            midi.addNote(track, channel, pitch, sound_time + i * duration, length * duration, volume)
        with open("end.mid", "wb") as midi_file:
            midi.writeFile(midi_file)
        
def main():
    
    pygame.init()
    sg.theme('Black')
    

    load_sound()
        
    screen_play()
        
    window.Close()

    
if __name__ == '__main__':
    main()
