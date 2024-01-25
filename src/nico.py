import pygame
import sys

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
        self.energy += coef * 0.1

    def getHungry(self):
        # if asleep, decreasing of needs slows down
        coef = 0.5 if self.isAsleep else 1
        self.hunger -= coef * 0.1

    def live(self,):
        # maximum of each need is 3
        # respective thresholds are 0, 1, 2. 0 being the lowest, 2 being the highest.

        # get tired
        if self.energy > 0.3: self.energy -= 0.3
        # get hungry
        if self.hunger > 0: self.hunger -= 0.5
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
    
    def feed(self, hunger, emotion, food):
        # check emotion (if sad, will not eat)
        # check hunger (if hunger >= 3, will not eat)
        if emotion == 'sad' or hunger >= 3:
            print("Nico doesn't want to eat right now.")
        # eat food (add hunger to the bar punctually)
        else:
            hunger += food
            print("Nico enjoyed his little snack !")

    def sleep(self, energy):
        # sleep (add energy to the bar over time)
        print("Nico fell asleep.")
        self.isAsleep = True

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

def main():
    pygame.init()

    nico = Nico(3,3,3,3,False,'happy')

    clock = pygame.time.Clock()
    fps = 60
    time_elapsed = 0
    # decrementation interval in ms
    # decrement_interval = 500

    # window creation
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Nico's behaviour testing")

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update time
        dt = clock.tick(fps)
        time_elapsed += dt

        if time_elapsed >= 1000:
            nico.live()
            nico.feelEmotion()
            time_elapsed = 0

        # Affichage du résultat
        screen.fill((255, 255, 255))  # Fond blanc
        font = pygame.font.Font(None, 36)
        text_energy = font.render(f"Energy: {round(nico.energy, 2)}/3", True, (0, 0, 0))
        text_hunger = font.render(f"Hunger: {round(nico.hunger, 2)}/3", True, (0, 0, 0))
        text_emotion = font.render(f"Emotion: {nico.feelEmotion()}", True, (0, 0, 0))
        screen.blit(text_energy, (0, 0))
        screen.blit(text_hunger, (0, 25))
        screen.blit(text_emotion, (0, 50))

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
