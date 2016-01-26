registry = []
ENUMERATION = 'Enumeration'
TEXT = 'Text'
NUMERIC = 'Numeric'


class Harvester():
    name = ''
    seed_types = []
    harvest_options = []

    def get_seed_types(self):
        return self.seed_types

    def get_harvest_options(self):
        return self.harvest_options

    def register(self):
        registry.append(self)


def get_harvester_list():
    return registry


class SeedType():
    name = ''
