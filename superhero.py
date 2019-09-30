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

    def attack(self):
        sum = 0
        for ability in self.abilities:
            sum += ability.attack()
        return sum

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        sum = 0
        for armor in self.armors:
            sum += armor.block()
        return damage_amt-sum


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     armor = Armor("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_armor(armor)
#     print(hero.defend(30))

    def take_damage(self,damage):
        self.current_health -= self.defend(damage)

# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.name)
#     print(hero.current_health)

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
       while self.is_alive() and opponent.is_alive():
           opponent.take_damage(self.attack())
           self.take_damage(opponent.attack())


       if self.abilities == None and opponent.abilities == None:
           print("DRAW!!!")

       else:
           if self.is_alive() == True:
               print(self.name, "won!")
           elif opponent.is_alive() == True:
               print(opponent.name, "won!")



# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)
class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__(self, name):
        self.heroes = []
        self.name = name

    ''' Initialize your team with its team name
    '''
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
    def add_hero(self,hero):
        self.heroes.append(hero)


    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0
        # TODO: Implement this method to remove the hero from the list given their name.

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
            '''Prints out all heroes to the console.'''
            # TODO: Loop over the list of heroes and print their names to the terminal.
