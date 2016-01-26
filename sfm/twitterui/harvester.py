from ui.harvester import Harvester, SeedType, HarvestOption, ENUMERATION


class Incremental(HarvestOption):
    name = 'Incremental'
    harvest_option_type = ENUMERATION
    enum_values = ['Yes', 'No']


class TwitterUserSeed(SeedType):
    name = 'Twitter User'
    harvest_options = [Incremental]


class TwitterRestSeed(SeedType):
    name = 'Twitter Rest'
    harvest_options = []


class TwitterHarvester(Harvester):
    name = 'TwitterHarvester'
    seed_types = [TwitterUserSeed, TwitterRestSeed]
