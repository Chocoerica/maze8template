# PYGAME BOILERPLATE CODE
# JRYZKNS 2019
import pygame as pg

screen_res = (600,300)

pg.init()
game_win = pg.display.set_mode(screen_res)

running   = True
paused    = False 
dt        = 0

game_clock = pg.time.Clock()
game_clock.tick()

while running:

        # CALLBACKS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                        paused = not paused

        dt = game_clock.get_time()/1000.

        if not paused:
                pass # game update code
        
        
        game_win.fill((0,0,0))
        
        # game draw code

        pg.display.flip()
        game_clock.tick()