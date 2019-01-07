from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: digit(x,1))
TWOS = (lambda x: digit(x,2))
THREES = (lambda x: digit(x,3))
FOURS = (lambda x: digit(x,4))
FIVES = (lambda x: digit(x,5))
SIXES = (lambda x: digit(x,6))
FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2,3] else 0)
FOUR_OF_A_KIND = (lambda x: four_of_a_kind(x))
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2,3,4,5,6] else 0)
CHOICE = sum

def digit(list, digit):
  return digit * list.count(digit)

def four_of_a_kind(list):
  elements = [dice for dice in set(list) if list.count(dice) >= 4]
  return 4 * elements[0] if len(elements) > 0 else 0

def score(dice, category):
  return category(dice)
