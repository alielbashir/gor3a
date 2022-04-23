import random
from collections import deque


def generate_pairs(gifters: list[str]) -> dict[str, str]:
    """ "
    Randomly generates a dict of gifters and receivers for the gift swap
    """
    random.shuffle(gifters)
    receivers = deque(gifters)
    receivers.rotate()
    return dict(zip(gifters, receivers))
