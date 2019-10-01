import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength


    def attack(self):
        return random.randint(1, self.max_damage)


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
        self.kills = 0
        self.deaths = 0

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.








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

    def defend(self, damage_amt =0):
        sum = 0
        for piece in self.armors:
            sum += piece.block()
        return abs(damage_amt-sum)

        def add_kills(self,num_kills):
            self.kills += num_kills

        def add_deaths(self, num_deaths):
            self.deaths += num_deaths

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     armor = Armor("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_armor(armor)
#     print(hero.defend(30))

    def take_damage(self,damage):
        self.current_health -= self.defend(damage)
        self.current_health = current_health - final_damage

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
        if (len(self.abilities) + len(opponent.abilities)) > 0:
           while self.is_alive() and opponent.is_alive():
               opponent.take_damage(self.attack())
               self.take_damage(opponent.attack())


               if self.is_alive() == True:
                   self.add_kills(1)
                   opponent.add_deaths(1)
                   print(self.name, "won!")

               elif opponent.is_alive() == True:
                   opponent.add_kills(1)
                   self.add_deaths(1)
                   print(opponent.name, "won!")

               else:
                    print("DRAW!!!")
                    self.add_kills(1)
                    opponent.add_deaths(1)
                    opponent.add_kills(1)
                    self.add_deaths(1)
        else:
            print("DRAW!!!")
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
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        hero = random.choice(self.heroes)
        opponent = random.choice(self.heroes)
        Hero.fight(hero, opponent)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health


    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(f"-{hero.name} = {hero.kills}/{hero.deaths}")


        # ktdr = 0
        # total_kills = 0
        # total_deaths = 0
        # for hero in self.heroes:
        #     total_kills += hero.kills
        #     total_deaths += hero.deaths
        # if total_deaths == 0:
        #     ktdr = total_kills
        # else:
        #     ktdr = total_kills/total_deaths
        # return ktdr

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team("Team A")
        self.team_two = Team("Team B")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        Ability.name = input("Enter an ability: ")
        Ability.attack_strength = input ("Enter a weapon: ")
        return Ability.name, Ability.attack_strength

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        Weapon.name = input("Enter a weapon: ")
        Weapon.attack_strength = input("Enter attack strength: ")
        return Weapon.name, Weapon.attack_strength

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        Armor.name = input("Enter name of armor")
        Armor.max_block = input("Enter block strength")
        return Armor.name, Armor.max_block

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Choose a name for your hero: ")
        health = input("What is your heroes starting health?: ")
        hero = Hero(hero_name, health)

        armor_option = input("Would you like to add an armor?: (Y/N): ")
        while armor_option == 'yes' or 'Y':
            armor = self.create_armor()
            hero.add_armor(armor)
            armor_option = input("Do you want to add another?: (Y/N): ")
            if armor_option == 'Y' or 'y' or 'yes':
                return True
            elif armor_option =='N' or 'n' or 'no':
                armor_option = False
                continue
            else:
                continue
        ability_option = input("Do you want to add an ability?: Y/N ")
        while ability_option == 'y' or 'yes' or 'Y':
             adding_ability = True
             while adding_ability:
                 ability = self.create_ability()
                 hero.add_ability(ability)
                 another_ability = input("Would you like to add another?: (Y/N) ")
                 if another_ability == 'Y' or 'y' or 'yes':
                     return True
                 elif another_ability == 'no' or 'n' or 'N':
                     adding_ability = False
        weapon_option = input("Do you want to add a weapons?: (Y/N)")
        while weapon_option == 'Y' or 'y' or 'Yes':
            adding_weapon = True
            while adding_weapon:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                another_weapon = input("Do you want to add another weapon?: (Y/N) ")
                if another_weapon == 'y' or 'yes' or 'Y':
                    return True
                elif another_weapon == 'n' or 'no' or 'N':
                    break
                else:
                    break

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        sizeof_team_one = input("How many heroes are on the first team? ")
        for hero in range(int(sizeof_team_one)):
            self.create_hero()
            self.team_one.add_hero(hero)
    def build_team_two(self):
        sizeof_team_two = input("How many heroes are on the second team? ")
        for hero in range(int(sizeof_team_two)):
            self.create_hero()
            self.team_two.add_hero(hero)
    def team_battle(self):
        Team.fight(self.team_one, self.team_two)
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        self.team_one.stats()
        self.team_two.stats()

        winners = self.team_one.attack(self.team_two)
        print("The winners are {}! Good Job".format(winners))

if __name__== "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

    if __name__ == "__main__":
        game_is_running = True

        # Instantiate Game Arena
        arena = Arena()

        #Build Teams
        arena.build_team_one()
        arena.build_team_two()

        while game_is_running:

            arena.team_battle()
            arena.show_stats()
            play_again = input("Play Again? Y or N: ")

            #Check for Player Input
            if play_again.lower() == "n":
                game_is_running = False

            else:
            #Revive heroes to play again
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
