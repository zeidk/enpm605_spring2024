"""
This file contains the Enemy class.
"""

class Enemy:
    """
    A class representing an enemy in the game.

    Attributes:
        name (str): The name of the enemy.
        health (int): The health of the enemy.
    """

    def __init__(self, name="Enemy", health=50):
        self.name = name
        self.health = health

    def __str__(self):
        """
        Returns the string representation of the enemy.

        Returns:
            str: The string representation of the enemy.
        """
        return f"{self.name} has {self.health} health."


    def attack(self, player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🧟🗡️ {self.name} attacks {player.name}!")
        player.take_damage(damage)

    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            print(f"🧟💀 {self.name} has been defeated!")
        else:
            print(f"🧟💜 {self.name} has {self.health} health left.")
