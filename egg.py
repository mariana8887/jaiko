import play
import time
import pygame
from random import randint

pygame.mixer_music.load('mus.mp3')
pygame.mixer_music.play()
play.set_backdrop('violet')
hello_txt=play.new_text(words='Catch 10 EGGS!', x=0, y=play.screen.height/2-30)

egg=play.new_circle(color='pink', x=0, y=0, radius=25, border_color='grey', border_width=2)
#egg = play.new_image(image='pic.png', x=0, y=0, angle=0, size=30, transparency=100)
eggs=[egg]
eggs_amount=play.new_text(words='0', x=300, y=play.screen.height/2-30, color='yellow')

backet=play.new_image(image='corzz.png', x=0, y=-play.screen.height/2+50, size=20)
#backet=play.new_image(image='archi.png', x=0, y=-play.screen.height/2+80, size=80)
frames = 48 
old_time = 0

@play.when_program_starts
def start():
    global old_time
    old_time = time.time()

    backet.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=10
    )
    eggs[0].x = randint(-play.screen.width/2+20, play.screen.width/2-20)
    eggs[0].y = play.screen.height/2-20

@play.repeat_forever
async def game():
    global old_time

    #ловля яиц
    for egg in eggs:
        if egg.is_touching(backet):
            eggs.remove(egg)
            egg.hide()
            eggs_amount.words=str(int(eggs_amount.words)+1)
        egg.y=egg.y-5

        #победа
        if int(eggs_amount.words) == 10:
            lose = play.new_text(words='YOU WIN', x=0, y=0, color='yellow', font_size=100)
            backet.hide()
            await play.timer(seconds=1)
            quit()

        #проигрыш
        if egg.y < backet.y:
            lose = play.new_text(words='YOU LOSE', x=0, y=0, color='red', font_size=100)
            backet.hide()
            await play.timer(seconds=1)
            quit()

    #перемещение платформы
    if play.key_is_pressed('a'):
        backet.physics.x_speed = -15
    elif play.key_is_pressed('d'):
        backet.physics.x_speed = 15
    else:
        backet.physics.x_speed = 0

    #новые яйцв
    if time.time()-old_time > 3:
        new_egg = play.new_circle(color='pink', x=0, y=0, radius=25, border_color='grey', border_width=2)
        #new_egg = play.new_image(image='pic.png', x=0, y=0, angle=0, size=30, transparency=100)
        new_egg.x = randint(-play.screen.width/2+20, play.screen.width/2-20)
        new_egg.y = play.screen.height/2-20
        eggs.append(new_egg)

        old_time = time.time()

    await play.timer(seconds=1/frames)


play.start_program()
