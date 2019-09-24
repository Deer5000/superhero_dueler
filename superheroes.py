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
        return random.randint(0, self.max_block)

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

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
