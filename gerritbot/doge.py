import random


doge_prefixes = [
    '',
    'SO ',
    'VERY ',
    'MUCH ',
    'WOW ',
    'VERY MUCH ',
    'SO MUCH ',
]
doge_positive = [
    'CODE',
    'BRILLIANCE',
    'OBJECTS',
    'SUCCESS',
    'WIN',
    'SUNSHINE',
    'GREATNESS',
]
doge_neutral = [
    'COMMENT',
    'DISCUSSION',
]
doge_negative = [
    'GARBAGE',
    'TRASH',
    'POOP',
    'FAIL',
    'FAILURE',
    'FAILBOAT',
    'CLOUDS',
    'DEMOTION',
    'REJECTION',
]


class DogeMessage(object):
    def __init__(self, prefixes=[], positive=[], neutral=[], negative=[]):
        self.prefixes = prefixes
        self.positive = positive
        self.neutral = neutral
        self.negative = negative

    def __getitem__(self, polarity):
        if self.polarity > 0:
            return random.choice(doge_prefixes) + random.choice(doge_positive)
        if self.polarity < 0:
            return random.choice(doge_prefixes) + random.choice(doge_negative)
        return random.choice(doge_prefixes) + random.choice(doge_neutral)
