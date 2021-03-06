import time
from random import randrange


class Weather:
    def __init__(self, name=None):
        self.name = name


class Move:
    def __init__(self, power=None, accuracy=None, type=None, category=None, contact=None, priority=0,
                 critical_chance=1):
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.category = category
        self.contact = contact
        self.priority = priority
        self.critical_chance = critical_chance
        # todo: effects


class Pokemon:
    def __init__(self, lvl: int, stats: dict, attacks: list, type1=None, type2=None, name=None, ability=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.lvl = lvl
        self.stats = stats
        self.attacks = attacks
        self.lvl_factor = round(0.9 + 0.1 * self.lvl + 0.0004 * self.lvl * self.lvl, 4)
        self.ability = ability
        # todo: resistances in this class

    def get_type_resistance(self, type_name):
        if self.type2 is not None:
            return self.type1.resistances[type_name] * self.type2.resistances[type_name]
        else:
            return self.type1.resistances[type_name]


class Type:
    def __init__(self, name: str, normal_resistance=1.0, fire_resistance=1.0, water_resistance=1.0,
                 grass_resistance=1.0, electric_resistance=1.0, flying_resistance=1.0, psychic_resistance=1.0,
                 poison_resistance=1.0,
                 ghost_resistance=1.0, fighting_resistance=1.0, steel_resistance=1.0, ground_resistance=1.0,
                 rock_resistance=1.0, ice_resistance=1.0, dark_resistance=1.0, bug_resistance=1.0,
                 dragon_resistance=1.0, fairy_resistance=1.0):
        self.name = name
        self.resistances = {
            'Normal': normal_resistance,
            'Fire': fire_resistance,
            'Water': water_resistance,
            'Grass': grass_resistance,
            'Electric': electric_resistance,
            'Flying': flying_resistance,
            'Psychic': psychic_resistance,
            'Poison': poison_resistance,
            'Ghost': ghost_resistance,
            'Fighting': fighting_resistance,
            'Steel': steel_resistance,
            'Ground': ground_resistance,
            'Rock': rock_resistance,
            'Ice': ice_resistance,
            'Dark': dark_resistance,
            'Bug': bug_resistance,
            'Dragon': dragon_resistance,
            'Fairy': fairy_resistance
        }


normal = Type(name='Normal', fighting_resistance=2, ghost_resistance=0)
fire = Type(name='Fire', fire_resistance=0.5, grass_resistance=0.5, steel_resistance=0.5, bug_resistance=0.5,
            ice_resistance=0.5, fairy_resistance=0.5, water_resistance=2, ground_resistance=2, rock_resistance=2)
water = Type(name="Water", fire_resistance=0.5, water_resistance=0.5, ice_resistance=0.5, steel_resistance=0.5,
             grass_resistance=2, electric_resistance=2)
grass = Type(name='Grass', electric_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, water_resistance=0.5,
             bug_resistance=2, fire_resistance=2, flying_resistance=2, poison_resistance=2, ice_resistance=2)
electric = Type(name='Electric', electric_resistance=0.5, flying_resistance=0.5, steel_resistance=0.5,
                ground_resistance=2)
flying = Type(name='Flying', ground_resistance=0, grass_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5,
              electric_resistance=2, rock_resistance=2, ice_resistance=2)
psychic = Type(name='Psychic', psychic_resistance=0.5, fighting_resistance=0.5, ghost_resistance=2, dark_resistance=2,
               bug_resistance=2)
poison = Type(name='Poison', grass_resistance=0.5, poison_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5,
              fairy_resistance=0.5, psychic_resistance=2, ground_resistance=2)
ghost = Type(name='Ghost', normal_resistance=0, fighting_resistance=0, bug_resistance=0.5, poison_resistance=0.5,
             ghost_resistance=2, dark_resistance=2)
fighting = Type(name='Fighting', rock_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5, flying_resistance=2,
                psychic_resistance=2, fairy_resistance=2)
steel = Type(name='Steel', poison_resistance=0, normal_resistance=0.5, grass_resistance=0.5, flying_resistance=0.5,
             fairy_resistance=0.5, steel_resistance=0.5, rock_resistance=0.5, ice_resistance=0.5, bug_resistance=0.5,
             dragon_resistance=0.5, psychic_resistance=0.5, fire_resistance=2, fighting_resistance=2,
             ground_resistance=2)
ground = Type(name='Ground', electric_resistance=0, poison_resistance=0.5, rock_resistance=0.5, water_resistance=2,
              grass_resistance=2, ice_resistance=2)
rock = Type(name='Rock', poison_resistance=0.5, normal_resistance=0.5, fire_resistance=0.5, flying_resistance=0.5,
            water_resistance=2, grass_resistance=2, fighting_resistance=2, steel_resistance=2, ground_resistance=2)
ice = Type(name='Ice', ice_resistance=0.5, fire_resistance=2, rock_resistance=2, fighting_resistance=2,
           steel_resistance=2)
dark = Type(name='Dark', psychic_resistance=0, dark_resistance=0.5, ghost_resistance=0.5, fighting_resistance=2,
            bug_resistance=2, fairy_resistance=2)
bug = Type(name='Bug', fighting_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, fire_resistance=2,
           flying_resistance=2, rock_resistance=2)
dragon = Type(name='Dragon', fire_resistance=0.5, water_resistance=0.5, grass_resistance=0.5, electric_resistance=0.5,
              ice_resistance=2, dragon_resistance=2, fairy_resistance=2)
fairy = Type(name='Fairy', dragon_resistance=0, fighting_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5,
             poison_resistance=2, steel_resistance=2)

# POKEMON1'S ATTACKS
attacks1 = [
    Move(power=1, accuracy=100, type='Dark', category='Special', contact=False),
    Move(power=1, accuracy=100, type='Ghost', category='Special', contact=False),
    Move(power=1, accuracy=100, type='Ghost', category='Physical', contact=True),
    Move(power=1, accuracy=100, type='Water', category='Physical', contact=True, critical_chance=2)
]
# POKEMON2'S ATTACKS
attacks2 = [
    Move(power=1, accuracy=100, type='Psychic', category='Special', contact=False),
    Move(power=1, accuracy=100, type='Flying', category='Special', contact=False),
    Move(power=1, accuracy=100, type='Flying', category='Special', contact=False),
    Move(power=1, accuracy=100, type='Flying', category='Special', contact=False, critical_chance=2)
]


def fight(pokemon_1, pokemon_2):
    try:
        for x in range(12):
            for round in range(4):

                if pokemon_1.attacks[round].priority == pokemon_2.attacks[round].priority:
                    if pokemon_1.stats['spd'] >= pokemon_2.stats['spd']:
                        # ATAK POKA 1
                        attack(attacker=pokemon_1, defender=pokemon2, runda=round)
                        # ATAK POKA 2
                        attack(attacker=pokemon_2, defender=pokemon_1, runda=round)
                    else:
                        # ATAK POKA 2
                        attack(attacker=pokemon_2, defender=pokemon_1, runda=round)
                        # ATAK POKA 1
                        attack(attacker=pokemon_1, defender=pokemon_2, runda=round)

                elif pokemon_1.attacks[round].priority > pokemon_2.attacks[round].priority:
                    # ATAK POKA 1
                    attack(attacker=pokemon_1, defender=pokemon_2, runda=round)
                    # ATAK POKA 2
                    attack(attacker=pokemon_2, defender=pokemon_1, runda=round)

                elif pokemon_1.attacks[round].priority < pokemon_2.attacks[round].priority:
                    # ATAK POKA 2
                    attack(attacker=pokemon_2, defender=pokemon_1, runda=round)
                    # ATAK POKA 1
                    attack(attacker=pokemon_1, defender=pokemon_2, runda=round)
    except ValueError:
        pass


def attack(attacker, defender, runda):
    print(f"HP of defender: {defender.stats['hp']} ({defender.name})")
    print(f"HP of attacker: {attacker.stats['hp']} ({attacker.name})")
    # todo: chance of using attack based on accuracy

    if attacker.attacks[runda].category == 'Status':
        print("Move's effect")
        pass
    else:
        physical_factor = round(0.27 * (attacker.stats['att'] + 25) / (defender.stats['def'] + 25), 4)
        special_factor = round(0.27 * (attacker.stats['spatt'] + 25) / (defender.stats['spdef'] + 25), 4)
        power_factor = attacker.attacks[runda].power

        if attacker.attacks[runda].type == attacker.type1 or attacker.attacks[runda].type == attacker.type2:
            power_factor = power_factor * 1.30
        if attacker.attacks[runda].category == 'Physical':
            stats_factor = physical_factor
        else:
            stats_factor = special_factor

        # power_factor multiplied by items
        # weather

        friend_guard_factor = 1
        friend_guard_factor = friend_guard(defender, friend_guard_factor)

        effectiveness_factor = defender.get_type_resistance(attacker.attacks[runda].type)
        print(f'Effectiveness of attack: {effectiveness_factor}')
        if effectiveness_factor == 0:
            print(f'{defender.name} is immune to this type of move')
        else:
            damage = int(power_factor * stats_factor * attacker.lvl_factor * effectiveness_factor * friend_guard_factor)
            # power_factor * stats_factor * attacker.lvl_factor * effectiveness_factor * weather_factor * friend_guard_factor

            damage = randomised_damage(damage)

            damage = critical_strike(attacker, damage, runda)

            defender.stats['hp'] = int(defender.stats['hp']) - int(damage)

            print(f"{attacker.name} attacks as first dealing {int(damage)}")
    print(f"{defender.name} ends up with {defender.stats['hp']} HP \n")

    verifying_winner(attacker, defender)


def friend_guard(defender, friend_guard_factor):
    if defender.ability == 'Friend Guard':
        friend_guard_factor = 0.85
        return friend_guard_factor
    else:
        return friend_guard_factor


def randomised_damage(damage):
    minimally = int(damage * 0.9)
    maximally = int(damage * 1.1)
    damage = randrange(minimally, maximally)
    return damage


def critical_strike(attacker, damage, runda):
    if attacker.attacks[runda].critical_chance == 1:
        if randrange(1000) <= 63:
            return damage * 1.5
        else:
            return damage

    elif attacker.attacks[runda].critical_chance == 2:
        if randrange(1000) <= 125:
            return damage * 1.5
        else:
            return damage

    elif attacker.attacks[runda].critical_chance == 3:
        if randrange(100) <= 50:
            return damage * 1.5
        else:
            return damage

    else:
        return damage * 1.5


def verifying_winner(attacker, defender):
    if defender.stats['hp'] <= 0:
        print(f"{attacker.name} won")
        raise ValueError

    elif attacker.stats['hp'] <= 0:
        print(f"{defender.name} won")
        raise ValueError


tic = time.perf_counter()
for i in range(1):
    # POKEMON1'S STATS
    stats1 = {
        'att': 385,
        'def': 671,
        'spatt': 1879,
        'spdef': 686,
        'spd': 897,
        'hp': 3575,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    # POKEMON2'S STATS
    stats2 = {
        'att': 268,
        'def': 542,
        'spatt': 698,
        'spdef': 683,
        'spd': 453,
        'hp': 1090,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    pokemon1 = Pokemon(type1=ghost, type2=poison, lvl=60, stats=stats1, attacks=attacks1, name=f'Gengar_{i}',
                       ability='Cursed Body')
    pokemon2 = Pokemon(type1=psychic, type2=fairy, lvl=57, stats=stats2, attacks=attacks2, name=f'Gardevoir_{i}',
                       ability='Trace')
    fight(pokemon_1=pokemon1, pokemon_2=pokemon2)

toc = time.perf_counter()
print(f'Duration of fight: {toc - tic:0.4f}')
