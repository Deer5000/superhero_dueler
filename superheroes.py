import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        return random.randint(1, self.attack_strength)


# my_Ability = Ability("Razorian","725")
# print(my_Ability.attack())

# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(1, self.max_block)

# if __name__ == "__main__":
#     armor = Armor("Debugging Ability", 20)
#     print(armor.name)
#     print(armor.block())

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

    def add_ability(self, ability):
        self.abilities.append(ability)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        sum = 0
        for armor in self.armors:
            sum += armor.block()
        return damage_amt-sum


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_armor(armor)
    print(hero.defend(30))
