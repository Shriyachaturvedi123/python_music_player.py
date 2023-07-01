
import pygame
import os
pygame.init()

# Set the path to your music directory
music_directory = "path/to/your/music/directory"

# Get a list of all music files in the directory
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

# Initialize the Pygame mixer
pygame.mixer.init()

# Create a Pygame window
window = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Music Player")

# Function to play a music file
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Function to stop the currently playing music
def stop_music():
    pygame.mixer.music.stop()

# Function to pause the currently playing music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the paused music
def resume_music():
    pygame.mixer.music.unpause()

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Play music when 'P' key is pressed
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    resume_music()
            elif event.key == pygame.K_s:
                # Stop music when 'S' key is pressed
                stop_music()
            elif event.key == pygame.K_1:
                # Play the first music file in the list when '1' key is pressed
                play_music(os.path.join(music_directory, music_files[0]))
            elif event.key == pygame.K_2:
                # Play the second music file in the list when '2' key is pressed
                play_music(os.path.join(music_directory, music_files[1]))

    # Update the display
    pygame.display.update()

# Quit the program
pygame.quit()
