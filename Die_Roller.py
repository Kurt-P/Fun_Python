#!/usr/bin/env python

from random import randint
import argparse

parser = argparse.ArgumentParser()

## Set the number of sides of the dice
parser.add_argument("-s", "--sides", type=int, default=6,
    help="The number of sides the die will have")

## Set the number of dice to roll
parser.add_argument("-d", "--dice", type=int, default=5,
    help="The number of dice to cast")

## Allow the user to sum the outcome of the throws
parser.add_argument("-a", "--add", action="store_true",
    help="Add the sum of the dice cast")

## Assign the args to a new object
## There is probably a better way of doing this
args = parser.parse_args()

number_of_sides = args.sides
number_of_dice  = args.dice

def roll(dice, sides):
    _min    = 1
    _max    = sides
    rolls   = []

    for i in range(dice):
        r = randint(_min, _max)
        print "The roll of die %d is %d" % ((i + 1), r)
        rolls.append(r)
    if args.add is not False:
        _sum = sum(rolls)
        print '=' * 5
        print "The total of the rolls is %d" % _sum

roll(number_of_dice, number_of_sides)
