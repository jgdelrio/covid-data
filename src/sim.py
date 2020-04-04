

class country_model():
    def __init__(self, name, population):
        self.name = name                # country name
        self.population = population    # total population
        self.infected = 0
        self.dead = 0
        self.recovered = 0

        self.infectivity = 3
        self.mortality_rate = 0.1



