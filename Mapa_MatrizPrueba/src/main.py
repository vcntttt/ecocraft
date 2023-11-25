import pygame
from classes.map import Map
from classes.menu import Menu

def main():
    pygame.init()
    game = Map()
    menu = Menu() 

    running = True
    while running:
       
        game.map_run()  
        game_hour = game.get_hour()  
        organismos = game.get_organismos()  

       
        menu.updateHour(game_hour)
        menu.updateStates(organismos)
        menu.draw(game.screen, (0, 0))  
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
