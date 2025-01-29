from tkinter import *
from tkinter import filedialog
import pygame

pygame.mixer.init()

root = Tk()
root.geometry("300x300")
root.configure(bg="white")
root.title("MP3 Player")

volume = 1.0  # Global volume variable, initial value set to max volume (1.0)
sound_file = None  # Variable to store the sound file path
is_new_selection = False  # Flag to check if the song is newly selected

def pause():
    global is_new_selection
    if is_new_selection:  # If the song was just selected, start playing it
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volume)  # Apply volume when playing
        is_new_selection = False  # Reset the flag once the song starts playing
        pause_button.configure(text="||")  # Change button to "Pause"
        pause_button.configure(command=pause)
    else:  # If song is already playing, just pause it
        pygame.mixer.music.pause()
        pause_button.configure(text="▶")  # Change button to "Play"
        pause_button.configure(command=unpause)

def unpause():
    pygame.mixer.music.unpause()
    pause_button.configure(text="||")  # Change button to "Pause"
    pause_button.configure(command=pause)

def choose_sound():
    global sound_file, is_new_selection
    sound_file = filedialog.askopenfilename()
    is_new_selection = True  # Flag is set to True when a new song is selected

def volume_add():
    global volume
    if volume < 1.0:
        volume += 0.1
        volume = min(volume, 1.0)  # Ensure volume does not exceed 1.0
        if sound_file:  # Reapply the volume whenever it's changed
            pygame.mixer.music.set_volume(volume)

def volume_lower():
    global volume
    if volume > 0.0:
        volume -= 0.1
        volume = max(volume, 0.0)  # Ensure volume does not go below 0.0
        if sound_file:  # Reapply the volume whenever it's changed
            pygame.mixer.music.set_volume(volume)

# Settings Functions

def settings():
    select_button.pack_forget()

    add_volume_button.pack_forget()
    lower_volume_button.pack_forget()
    add_volume_button.place_forget()
    lower_volume_button.place_forget()
    pause_button.pack_forget()
    pause_button.place_forget()

    settings_button.pack_forget()
    settings_button.place_forget()

    theme_button.pack(pady=7)
    back_setting_button.pack(pady=7)
    back_setting_button.place(x=0, y=0)

def back_settings_f():
    select_button.pack(pady=7)

    add_volume_button.pack(pady=7)
    add_volume_button.place(y=50, x=100)

    lower_volume_button.pack(pady=7)
    lower_volume_button.place(y=50, x=185)

    pause_button.pack(pady=7)
    pause_button.place(y=50, x=143)

    settings_button.pack(pady=7)
    settings_button.place(y=0, x=250)

    pause_button.pack(pady=7)
    pause_button.place(y=50, x=143)

    theme_button.pack_forget()
    dark_red_theme.pack_forget()
    dark_purple_theme.pack_forget()
    camo_theme.pack_forget()
    basic_theme.pack_forget()
    back_setting_button.pack_forget()
    back_setting_button.place_forget()

# Theme Functions

def Themes():
    basic_theme.pack(pady=7)
    dark_red_theme.pack(pady=7)
    dark_purple_theme.pack(pady=7)
    camo_theme.pack(pady=7)

def basic_theme_f():
    global root
    root.configure(bg="white")

    select_button.configure(bg="white", fg="black")
    add_volume_button.configure(bg="white", fg="black")
    lower_volume_button.configure(bg="white", fg="black")
    pause_button.configure(bg="white", fg="black")
    settings_button.configure(bg="white", fg="black")
    theme_button.configure(bg="white", fg="black")
    back_setting_button.configure(bg="white", fg="black")
    dark_red_theme.configure(bg="white", fg="black")
    dark_purple_theme.configure(bg="white", fg="black")
    camo_theme.configure(bg="white", fg="black")
    basic_theme.configure(bg="white", fg="black")

def Darkred_theme():
    global root
    root.configure(bg="black")

    select_button.configure(bg="black", fg="darkred")
    add_volume_button.configure(bg="black", fg="darkred")
    lower_volume_button.configure(bg="black", fg="darkred")
    pause_button.configure(bg="black", fg="darkred")
    settings_button.configure(bg="black", fg="darkred")
    theme_button.configure(bg="black", fg="darkred")
    back_setting_button.configure(bg="black", fg="darkred")
    dark_red_theme.configure(bg="black", fg="darkred")
    dark_purple_theme.configure(bg="black", fg="darkred")
    camo_theme.configure(bg="black", fg="darkred")
    basic_theme.configure(bg="black", fg="darkred")

def Darkpurple_theme():
    global root
    root.configure(bg="black")

    select_button.configure(bg="black", fg="purple")
    add_volume_button.configure(bg="black", fg="purple")
    lower_volume_button.configure(bg="black", fg="purple")
    pause_button.configure(bg="black", fg="purple")
    settings_button.configure(bg="black", fg="purple")
    theme_button.configure(bg="black", fg="purple")
    back_setting_button.configure(bg="black", fg="purple")
    dark_red_theme.configure(bg="black", fg="purple")
    dark_purple_theme.configure(bg="black", fg="purple")
    camo_theme.configure(bg="black", fg="purple")
    basic_theme.configure(bg="black", fg="purple")

def camotheme():
    global root
    root.configure(bg="#182D09")

    select_button.configure(bg="#06402B", fg="#006400")
    add_volume_button.configure(bg="#06402B", fg="#006400")
    lower_volume_button.configure(bg="#06402B", fg="#006400")
    pause_button.configure(bg="#06402B", fg="#006400")
    settings_button.configure(bg="#06402B", fg="#006400")
    theme_button.configure(bg="#06402B", fg="#006400")
    back_setting_button.configure(bg="#06402B", fg="#006400")
    dark_red_theme.configure(bg="#06402B", fg="#006400")
    dark_purple_theme.configure(bg="#06402B", fg="#006400")
    camo_theme.configure(bg="#06402B", fg="#006400")
    basic_theme.configure(bg="#06402B", fg="#006400")


# Player Buttons
select_button = Button(root, text="Choose Song", command=choose_sound, bg="white", fg="black")
select_button.pack(pady=7)

add_volume_button = Button(root, text="+", command=volume_add, font=("Arial", 12), bg="white", fg="black")
add_volume_button.pack(pady=7)
add_volume_button.place(y=50, x=100)

lower_volume_button = Button(root, text="-", command=volume_lower, font=("Arial", 12), bg="white", fg="black")
lower_volume_button.pack(pady=7)
lower_volume_button.place(y=50, x=185)

pause_button = Button(root, text="||", command=pause, font=("Arial", 12), bg="white", fg="black")
pause_button.pack(pady=7)
pause_button.place(y=50, x=143)

settings_button = Button(root, text="Settings", command=settings, bg="white", fg="black")
settings_button.pack(pady=7)
settings_button.place(y=0, x=250)

# Settings Buttons

theme_button = Button(root, text="Themes", command=Themes, bg="white", fg="black")
back_setting_button = Button(root, text="Back", command=back_settings_f, bg="white", fg="black" )

# Theme Buttons
basic_theme = Button(root, text="Basic Theme", command=basic_theme_f, bg="white", fg="black")
dark_red_theme = Button(root, text="Dark Red Theme", command=Darkred_theme, bg="white", fg="black")
dark_purple_theme = Button(root, text="Dark Purple Theme", command=Darkpurple_theme, bg="white", fg="black")
camo_theme = Button(root, text="Camo Theme", command=camotheme, bg="white", fg="black")

root.mainloop()
