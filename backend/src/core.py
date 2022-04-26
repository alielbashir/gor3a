import random
from collections import deque


class Receiver:
    def __init__(self, name: str):
        self.name = name
        self.viewed = False


def generate_pairs(gifters: list[str]) -> dict[str, str]:
    """ "
    Randomly generates a dict of gifters and receivers for the gift swap
    """
    random.shuffle(gifters)
    receivers = deque(gifters)
    receivers.rotate()
    return dict(zip(gifters, [Receiver(receiver) for receiver in receivers]))
