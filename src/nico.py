import pygame
from src.button import Button
import sys


class Nico():
    def __init__(self, energy, hunger, hygiene, social, isAsleep, emotion, coordinates, size):
        self.energy = energy
        self.hunger = hunger
        self.hygiene = hygiene
        self.social = social
        self.isAsleep = isAsleep
        self.emotion = emotion
        self.coordinates = coordinates
        self.size = size
        
        # initialize current emotion's frames
        for _ in range(2):
            self.current_frames = ["assets/nico_"+self.emotion+str(_)+".png","assets/nico_"+self.emotion+str(_)+".png"]

    def live(self):
        """
        slowly decrease needs (energy, hunger, hygiene, social)
        manage the sleep cycle of Nico, set frames depending on his emotion
        """
        # maximum of each need is 3
        # respective thresholds are 0, 1, 2, 3. 0 being the lowest, 3 being the highest.

        # fall asleep / wake up (add energy to the bar over time)
        if (self.energy < 0.3 and not self.isAsleep) or (self.energy > 2.9 and self.isAsleep):
            self.isAsleep = not self.isAsleep
        
        # get tired
        coef = 2 if self.isAsleep else -1
        self.energy += coef * 0.03 # modify number to lower number to slow down pace of each need
        
        # if asleep, decreasing of needs slows down
        # get hungry
        coef = 0.5 if self.isAsleep else 1
        if self.hunger > 0:
            self.hunger -= coef * 0.05

        # get dirty
        coef = 0.5 if self.isAsleep else 1
        if self.hygiene > 0:
            self.hygiene -= coef * 0.01

        # want to play
        coef = 0.25 if self.isAsleep else 1
        if self.social > 0:
            self.social -= coef * 0.03

        # get all sprites animation
        frames = {}
        lst_states = ['neutral', 'happy', 'angry', 'sad', 'sleep']
        for state in lst_states:
            state_frame = []
            for _ in range(2):
                state_frame.append("assets/nico_"+state+str(_)+".png")
            frames[state] = state_frame        

        # update image depending on emotion
        if self.isAsleep:
            self.current_frames = frames['sleep']
        else:
            self.current_frames = frames[self.emotion]


    def feelEmotion(self):
        """
        modify emotion depending on needs' fullfilment
        """
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
        """
        eat food (add hunger to the bar punctually)
        """
        # check emotion (if sad, will not eat)
        # check hunger (if hunger >= 3, will not eat)
        if self.emotion == 'sad' or self.hunger >= 3 or self.isAsleep:
            print("Nico doesn't / can't want to eat right now.")
            return True
        elif self.hunger+food > 3:
            self.hunger += food
            print("The food was delicious... But Nico ate a bit too much.")
            return False
        else :
            self.hunger += food
            print("Nico enjoyed his little snack !")
            return False

    def clean(self):
        """
        clean (add hygiene to the bar punctually)
        """
        # check emotion (if angry, will not clean)
        if self.emotion == 'angry' or self.isAsleep:
            print("Nico doesn't want to take a bath right now.")
            return True
        else:
            self.hygiene = 3
            print("Nico is all-clean now !")
            return False

    def pet(self):
        """
        pet (add social to the bar punctually)
        """
        # check emotion (if angry, will not want to be petted)
        if self.emotion == 'angry' or self.isAsleep:
            self.social = self.social - 1.0 if self.social - 1.0 > 0 else 0
            if self.isAsleep:
                self.isAsleep = False
            print("Nico doesn't want to be petted right now.")
            return True
        else:
            self.social = self.social + 0.05 if self.social + 0.05 < 3 else 3
            return False

    def update(self, screen, frame):
        frame_surface = pygame.image.load(self.current_frames[frame[0]])

        pygame.draw.rect(screen, "#181425FF", (self.coordinates, self.size))
        screen.blit(frame_surface, self.coordinates)
        pygame.display.flip()

def main():
    pygame.init()

    nico = Nico(3,3,3,3,False,'happy',  [150, 150])

    clock = pygame.time.Clock()
    fps = 60
    time_elapsed = 0

    # testing window creation
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Nico's behaviour testing")
    screen.fill((255,255,255))
    surf = pygame.Surface((700, 700)) 
    surf.fill((255,255,255)) # white rectangle
    font = pygame.font.Font(None, 36)

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
            nico.emotion = nico.feelEmotion()
            time_elapsed = 0

        screen.fill((255, 255, 255))  # Efface l'écran
        
        # animations
        if time_elapsed >= 500:
            frame_surface = pygame.image.load(nico.current_frames[1])
        else:
            frame_surface = pygame.image.load(nico.current_frames[0])
        screen.blit(surf, (0, 0))
        screen.blit(frame_surface, (150, 150))

        text_energy = font.render(f"Energy: {round(nico.energy, 2)}/3", True, (0, 0, 0))
        text_hunger = font.render(f"Hunger: {round(nico.hunger, 2)}/3", True, (0, 0, 0))
        text_hygiene = font.render(f"Hygiene: {round(nico.hygiene, 2)}/3", True, (0, 0, 0))
        text_social = font.render(f"Social: {round(nico.social, 2)}/3", True, (0, 0, 0))
        text_sleep = font.render(f"isAsleep: {nico.isAsleep}", True, (0, 0, 0))
        text_emotion = font.render(f"Emotion: {nico.feelEmotion()}", True, (0, 0, 0))
        screen.blit(text_energy, (0, 0))
        screen.blit(text_hunger, (0, 25))
        screen.blit(text_hygiene, (0, 50))
        screen.blit(text_social, (0, 75))
        screen.blit(text_sleep, (0, 100))
        screen.blit(text_emotion, (0, 125))
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
