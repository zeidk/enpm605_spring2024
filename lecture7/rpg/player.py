"""
This file contains the player class.
"""

import random
from typing import Any


class Player:
    """
    A class representing a player in the game.

    Attributes:
        name (str): The name of the player.
        health (int): The health of the player.

    """
    def __init__(self, name="Hero", health=100):
        self.name = name
        self.health = health

    def __str__(self):
        """
        Returns the string representation of the player.

        Returns:
            str: The string representation of the player.
        """
        return f"{self.name} has {self.health} health."

    def __iter__(self):
        """
        Returns an iterator for the player.

        Returns:
            Iterator[str|int]: An iterator for the player.
        """
        return iter([self.name, self.health])

    def __contains__(self, item: Any):
        """
        Returns whether the player contains the item.

        Args:
            item (Any): The item to check for.

        Returns:
            bool: Whether the player contains the item.
        """
        return item in (self.name, self.health)

    def __call__(self, amount: int):
        """
        Heals the player by the given amount.

        Args:
            amount (int): The amount to heal the player by.
        """
        if amount > 0:
            self.health += amount
            print(f"{self.name} is healed by {amount} health points.")
        else:
            print("Invalid healing amount. Please provide a positive integer.")

    def __gt__(self, other: "Player"):
        """
        Returns whether the player has more health than the other player.

        Args:
            other (Player): The other player to compare health with.

        Raises:
            TypeError: If the other object is not a player.

        Returns:
            bool: Whether the player has more health than the other player.
        """
        if isinstance(other, Player):
            return self.health > other.health
        else:
            raise TypeError("Unsupported operand types for >")

    def __add__(self, other: int|"Player"):
        """
        Adds the player's health to the other player's health or to the given amount.

        Args:
            other (int|"Player"): The other player or the amount to add to the player's health.

        Raises:
            TypeError: If the other object is not a player or an integer.

        Returns:
            Player: The new player with the combined health.
        """
        if isinstance(other, int):
            return Player(self.name, self.health + other)
        elif isinstance(other, Player):
            return Player(f"{self.name+other.name}", self.health + other.health)
        else:
            raise TypeError("Unsupported operand types for +")

    def attack(self, enemy: "Enemy", damage: int):
        """
        Attack the enemy.

        Args:
            enemy (Enemy): The enemy to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🤴🗡️ {self.name} attacks {enemy.name}!")
        enemy.take_damage(damage)

    def defend(self):
        """
        Defend against an attack.
        """
        print(f"🤴🛡️ {self.name} defends!")

    def take_damage(self, damage):
        """
        Take damage from an attack.

        Use random to determine if the player will defend or take damage.
        50% chance to defend, 50% chance to take damage.


        Args:
            damage (int): The amount of damage to take.
        """
        # create a random number between 0 and 1
        # if the number is greater than 0.5, the player will defend
        # if the number is less than 0.5, the player will take damage
        if random.random() > 0.5:
            self.defend()
        else:
            self.health -= damage
            if self.health <= 0:
                print(f"🤴💀 {self.name} has been defeated!")
            else:
                print(f"🤴💚 {self.name} has {self.health} health left.")


if __name__ == "__main__":
    arthur = Player("Arthur")
    arthur.health = "hello"
    arthur.take_damage(50)
