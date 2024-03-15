from dataclasses import dataclass
import random

roshambocalls = ("rock", "paper", "scissors")

@dataclass
class Player:
    name: str
    roshambo: str = roshambocalls[0]
    wins: int = 0
    losses: int = 0

    def generateRoshambo(self):
        self.__roshambo = roshambocalls[0]

    def
