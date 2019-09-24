import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        return random.randint(1, self.attack_strength)


# my_Ability = Ability("Razorian","725")
# print(my_Ability.attack())

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
