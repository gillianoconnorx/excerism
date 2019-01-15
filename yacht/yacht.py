# Score categories
# Change the values as you see fit
#all five dice showing same face
YACHT = lambda d: 50 if len(set(d)) == 1 else 0
#the sum of the dice with number X
ONES = lambda d: sum([x for x in (d) if x == 1])
TWOS = lambda d: sum([x for x in (d)if x == 2])
THREES = lambda d: sum([x for x in(d) if x == 3])
FOURS = lambda d: sum([x for x in (d) if x == 4])
FIVES = lambda d: sum ([x for x in (d) if x == 5])
SIXES = lambda d: sum([x for x in (d) if x == 6])
#three of one number two of another
FULL_HOUSE = lambda d: sum (d) if len(set(d)) == 2 and any ([d.count(x)==3 for x in set(d)]) else 0
#sum of them four digits
FOUR_OF_A_KIND = None
#12345
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == 5 else 0
#23456
BIG_STRAIGHT = None
#combination of all numbers
CHOICE = None


def score(dice, category):
    return category(dice)
