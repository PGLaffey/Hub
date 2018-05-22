from typer import *
from escape import *
import time
from random import randint 

class Battle():
    """Instance of a battle"""
    def __init__(self, pokemon1, pokemon2):
        self.player,self.computer = pokemon1,pokemon2
        self.player_turn()

    def player_turn(self):
        time.sleep(1)
        if self.player.health > 0 and self.computer.health > 0:
            typer(('-'*9)+'\n'+"Your turn\n"+('-'*9))
            typer("Actions:\nAttack\nRun\nUpdate\nSkip Turn\nWhat do you do?")
            command = input()
            command = command.lower()
            if command.startswith('a'):
                damage = self.damage_calculator(self.player,self.computer,40)
                self.computer.health -= damage
                typer(self.computer.name+' took '+str(damage)+' damage.\n')
                self.computer_turn()
            elif command.startswith('r'):
                if attempt_escape():
                    self.end_battle()
                else:
                    typer('You failed to escape!\n')
                    self.computer_turn()
            elif command.startswith('u'):
                typer('Your Pokemon:\n'+self.player.__str__()+'\n\nOpponent Pokemon:\n'+self.computer.__str__()+'\n')
                self.player_turn()
            elif command.startswith('s'):
                typer('You wait for the opportune moment.')
                self.computer_turn()
            else:
                typer('Invalid command "'+str(command)+'".')
                self.player_turn()
            
        else:
            self.end_battle()

    def computer_turn(self):
        time.sleep(1)
        if self.player.health > 0 and self.computer.health > 0:
            typer(('-'*(len(self.computer.name)+7))+'\n'+self.computer.name+"'s turn\n"+('-'*(len(self.computer.name)+7)))
            typer(self.computer.name+' attacks')
            damage = self.damage_calculator(self.computer,self.player,40)
            self.player.health -= damage
            typer(self.player.name+' took '+str(damage)+' damage.\n')
            self.player_turn()            
        else:
            self.end_battle()
            
    def damage_calculator(self,attacking,defending,power):
        attack = attacking.attack * power / defending.defense
        crit_chance = randint(0,100)
        if crit_chance < 1:
            attack = attack * 2
            typer("Super Critical Hit!")
        elif crit_chance < 5:
            attack = attack * 1.5
            typer("Critical Hit!")
        if attacking.element == defending.weakness:
            attack = attack * 2
            typer("Attack is Super Effective!")
        elif attacking.element == defending.strength:
            attack = attack / 2
            typer("Attack is Not Very Effective!")
        return int(attack)
        

    def end_battle(self):
        if self.player.health <= 0:
            typer('Your pokemon ({}) has been Defeated!'.format(self.player.name))
        elif self.computer.health <= 0:
            typer('You have defeated {}!'.format(self.computer.name))
        else:
            typer('You escaped the battle!')


        
