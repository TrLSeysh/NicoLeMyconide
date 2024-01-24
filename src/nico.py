class Nico():
    def __init__(self, energy, hunger, hygiene, social):
        self.energy = energy
        self.hunger = hunger
        self.hygiene = hygiene
        self.social = social
    def live(self, energy, hunger, hygiene, social):
        # maximum of each need is 3
        # respective thresholds are 0, 1, 2. 0 being the lowest, 2 being the highest.
        # get tired
        # get hungry
        # get dirty
        # want to play (if not angry)
        [...]
    def feelEmotion(self, energy, hunger, hygiene, social):
        # if hunger or energy =< 1, get angry
        # if social or hygiene =<1 , get sad
        [...]
    def feed(self, hunger, emotion, food):
        # check emotion (if sad, will not eat)
        # check hunger (if hunger >= 3, will not eat)
        # eat food (add hunger to the bar punctually)
        [...]
    def sleep(self, energy):
        # sleep (add energy to the bar over time)
        # decreasing of needs slows down
        [...]
    def clean(self, hygiene, emotion):
        # check emotion (if angry, will not clean)
        # clean (add hygiene to the bar punctually)
        [...]
    def play(self, social, emotion):
        # check emotion (if angry, will not play)
        # play (add social to the bar punctually)
        [...]