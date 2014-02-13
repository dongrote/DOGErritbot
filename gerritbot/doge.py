import random


class DogeMessage(object):
    def __init__(self, prefixes=[], positive=[], neutral=[], negative=[]):
        self.prefixes = prefixes
        self.positive = positive
        self.neutral = neutral
        self.negative = negative

    def __getitem__(self, polarity):
        if polarity > 0:
            return random.choice(self.prefixes) + ' ' + random.choice(self.positive)
        if polarity < 0:
            return random.choice(self.prefixes) + ' ' + random.choice(self.negative)
        return random.choice(self.prefixes) + ' ' + random.choice(self.neutral)
