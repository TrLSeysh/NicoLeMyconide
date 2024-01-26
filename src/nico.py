import pygame
from button import Button
import sys
#import game

class Nico():
    def __init__(self, energy, hunger, hygiene, social, isAsleep, emotion):
        self.energy = energy
        self.hunger = hunger
        self.hygiene = hygiene
        self.social = social
        self.isAsleep = isAsleep
        self.emotion = emotion

    def getTired(self):
        coef = 2 if self.isAsleep else -1
        self.energy += coef * 0.3 # modify 0.3 to lower number to slow down pace

    def getHungry(self):
        # if asleep, decreasing of needs slows down
        coef = 0.5 if self.isAsleep else 1
        if self.hunger > 0:
            self.hunger -= coef * 0.5 # modify 0.5 to lower number to slow down pace


    def live(self,):
        # maximum of each need is 3
        # respective thresholds are 0, 1, 2, 3. 0 being the lowest, 3 being the highest.

        # fall asleep / wake up (add energy to the bar over time)
        if (self.energy < 0.3 and not self.isAsleep) or (self.energy > 2.7 and self.isAsleep):
            self.isAsleep = not self.isAsleep
        # get tired
        self.getTired()
        # get hungry
        self.getHungry()
        # get dirty (coming feature)
        # want to play (coming feature)

    def feelEmotion(self):
        # if hunger or energy =< 1, get angry
        if self.energy <= 1 or self.hunger <= 1:
            emotion = 'angry'
        # if social or hygiene =<1 , get sad
        elif self.hygiene <=1 or self.social <= 1:
            emotion = 'sad'
        # get happy if all needs are met ^_^
        elif self.energy >=2 and self.hunger >=2 and self.hygiene >= 2 and self.social >=2:
            emotion = 'happy'
        else:
            emotion = 'neutral'
        return emotion
    
    def feed(self, food):
        # check emotion (if sad, will not eat)
        # check hunger (if hunger >= 3, will not eat)
        if self.emotion == 'sad' or self.hunger >= 3 or self.isAsleep:
            print("Nico doesn't / can't want to eat right now.")
        # eat food (add hunger to the bar punctually)
        elif self.hunger+food > 3:
            self.hunger = 3
            print("The food was delicious... But Nico ate a bit too much.")
        else :
            self.hunger += food
            print("Nico enjoyed his little snack !")

    def clean(self, hygiene, emotion):
        # check emotion (if angry, will not clean)
        if emotion == 'angry' or hygiene >= 3:
            print("Nico doesn't want to take a bath right now.")
        # clean (add hygiene to the bar punctually)
        else:
            hygiene += 3
            print("Nico is all-clean now !")

    def play(self, social, emotion):
        # check emotion (if angry, will not play)
        if emotion == 'angry':
            print("Nico doesn't feel like playing right now.")
        # play (add social to the bar punctually)
        else:
            social += 1
            print("Nico and you played together, you both had a lot of fun !")
    
    def is_button_pressed(self, current_btn):
        m_pos = pg.mouse.get_pos()

        for button in current_btn:
            if current_btn[button].x < m_pos[0] < current_btn[button].x + current_btn[button].size_x:
                if current_btn[button].y < m_pos[1] < current_btn[button].y + current_btn[button].size_y:
                    self.window.update_item(current_btn[button])
                    return button

        return None

    def has_button_been_pressed(self, current_btn):
        for button in current_btn:
            if current_btn[button].is_pressed:
                self.window.update_item(current_btn[button])
                return button

        return None


def main():
    pygame.init()

    nico = Nico(3,3,3,3,False,'happy')

    clock = pygame.time.Clock()
    fps = 60
    time_elapsed = 0
    # decrementation interval in ms
    # decrement_interval = 500

    # testing window creation
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Nico's behaviour testing")
    screen.fill((255,255,255))
    surf = pygame.Surface((200, 150)) 
    surf.fill((255,255,255)) # white rectangle
    font = pygame.font.Font(None, 36)

    # button creation
    sleep_bt = Button(150,150,96,48,"main_button",screen)
    sleep_bt.display(screen)

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # nico.feed(1)

        # update time
        dt = clock.tick(fps)
        time_elapsed += dt

        if time_elapsed >= 1000:
            nico.live()
            nico.feelEmotion()
            time_elapsed = 0

        # display results on window
        screen.blit(surf, (0, 0))
        text_energy = font.render(f"Energy: {round(nico.energy, 2)}/3", True, (0, 0, 0))
        text_hunger = font.render(f"Hunger: {round(nico.hunger, 2)}/3", True, (0, 0, 0))
        text_sleep = font.render(f"isAsleep: {nico.isAsleep}", True, (0, 0, 0))
        text_emotion = font.render(f"Emotion: {nico.feelEmotion()}", True, (0, 0, 0))
        screen.blit(text_energy, (0, 0))
        screen.blit(text_hunger, (0, 25))
        screen.blit(text_sleep, (0, 50))
        screen.blit(text_emotion, (0, 75))
        #sleep_bt.update(screen)
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
