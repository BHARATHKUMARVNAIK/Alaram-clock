
import pygame
import time
import os

'''

print("Building an alarm clock \n")

# Initialize the mixer
pygame.mixer.init()

# Load and play the sound
pygame.mixer.music.load("./Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3")
#pygame.mixer.music.play()

# Wait until the sound finishes
#while pygame.mixer.music.get_busy():
#    time.sleep(1)  # Sleep for smoother CPU usage


CLEAR = '\033[2'
CLEAR_AND_RETURN = '\033[H'


def alaram(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        mintes_left = time_left // 60
        seconds_left = time_left % 60
        print(f'{CLEAR_AND_RETURN} {mintes_left:02d} {seconds_left:02d}')
        pygame.mixer.music.play()

minutes = int(input("How many minutes to wait : "))
seconds = int(input('How many seconds to wait : '))
total_seconds = minutes * 60 * seconds
alaram(total_seconds)

'''

import pygame
import time
import os

print("🔔 Building an Alarm Clock\n")

# Initialize the mixer
pygame.mixer.init()

# Load the sound file (make sure the path is correct)
pygame.mixer.music.load("./Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com-www.fesliyanstudios.com.mp31")

def alarm(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time left: {time_format}", end='\r')  # Overwrites on same line
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up! Playing alarm...")
    pygame.mixer.music.play()

    # Wait while music is playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Get user input
try:
    minutes = int(input("How many minutes to wait? "))
    seconds = int(input("How many seconds to wait? "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)
except ValueError:
    print("Please enter valid numbers!")
