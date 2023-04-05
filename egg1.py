import play
import time
import pygame
from random import randint

pygame.mixer_music.load('hello.mp3')
pygame.mixer_music.play()
play.set_backdrop('light green')
hello_txt=play.new_text(words='Catch 10 EGGS!', x=0, y=play.screen.height/2-30)

eggs_amount=play.new_text(words='0', x=300, y=play.screen.height/2-30, color='yellow')

backet=play.new_image(image='корзина.png', x=0, y=-play.screen.height/2+50, size=20)
#backet=play.new_image(image='archi.png', x=0, y=-play.screen.height/2+80, size=80)
frames = 48 
old_time = 0

@play.when_program_starts
def start():
    backet.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=10
    )

async def game():
    pass

play.start_program()