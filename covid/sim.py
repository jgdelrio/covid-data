import numpy as np


class Pandemic:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Pandemic._instance:
            Pandemic._instance = super(Pandemic, cls).__new__(cls, *args, **kwargs)
        return Pandemic._instance

    def __init__(self, infectivity=3, mortality=0.1, incubation=14):
        # Pandemic parameters
        self.infectivity = infectivity  # how infectious is the pandemic
        self.mortality = mortality      # average mortality rate
        self.incubation = incubation    # average days of incubation period


class CountryModel:
    def __init__(self, name, population):
        self.name = name                # country name

        # Population
        self.population = population    # total population
        self.infected = 0               # currently infected
        self.deaths = 0                 # accumulated deaths
        self.recovered = 0              # accumulated recovered

        # If the country don't implement any controls the interaction remains 1 (100%)
        self.interaction = 1.0
