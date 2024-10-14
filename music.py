import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the pygame mixer
pygame.mixer.init()

# Create the main application window
root = tk.Tk()
root.title("Python Music Player")
root.geometry("600x400")
root.config(bg="#282c34")  # Background color

# Global variables
playlist = []
current_song_index = -1
is_paused = False

# Function to add music from local system
def add_music():
    global playlist
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        playlist.append(file_path)
        playlist_listbox.insert(tk.END, file_path.split("/")[-1])  # Show filename in playlist

# Function to play music
def play_music():
    global current_song_index, is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        if playlist:
            if playlist_listbox.curselection():
                current_song_index = playlist_listbox.curselection()[0]
            else:
                current_song_index = 0
            pygame.mixer.music.load(playlist[current_song_index])
            pygame.mixer.music.play()
        else:
            messagebox.showinfo("Error", "No songs in the playlist!")

# Function to pause music
def pause_music():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to play the next song in the playlist
def next_song():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index + 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

# Function to play the previous song in the playlist
def prev_song():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index - 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

# Create the playlist listbox
playlist_listbox = tk.Listbox(root, width=60, height=10, bg="#3e4451", fg="white", font=("Arial", 12))
playlist_listbox.pack(pady=20)

# Create control buttons with colors
controls_frame = tk.Frame(root, bg="#282c34")
controls_frame.pack(pady=20)

button_style = {
    "bg": "#61afef",
    "fg": "white",
    "font": ("Arial", 12, "bold"),
    "width": 8,
    "relief": "raised"
}

play_button = tk.Button(controls_frame, text="Play", **button_style, command=play_music)
play_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(controls_frame, text="Pause", **button_style, command=pause_music)
pause_button.grid(row=0, column=1, padx=10)

stop_button = tk.Button(controls_frame, text="Stop", **button_style, command=stop_music)
stop_button.grid(row=0, column=2, padx=10)

prev_button = tk.Button(controls_frame, text="Previous", **button_style, command=prev_song)
prev_button.grid(row=0, column=3, padx=10)

next_button = tk.Button(controls_frame, text="Next", **button_style, command=next_song)
next_button.grid(row=0, column=4, padx=10)

# Add Music Button with color
add_button = tk.Button(root, text="Add Music", **button_style, command=add_music)
add_button.pack(pady=10)

# Start the main event loop
root.mainloop()
