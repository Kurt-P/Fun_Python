#!/usr/bin/env python

## Imports
from random import randint, random ## Need to generate the random numbers
import argparse ## Used for argument parsing

## Useing argparse for quick and simple argument parsing
parser = argparse.ArgumentParser()

## Set the number of sides of the dice
## If no int is provided, the default number of '6' is used.
parser.add_argument("-s", "--sides", type=int, default=6,
    help="The number of sides the die will have")

## Set the number of dice to roll
## If no int is provided, the default amount of '5' is used.
parser.add_argument("-d", "--dice", type=int, default=5,
    help="The number of dice to cast")

## Allow the user to roll a percentile; 0.0 to 1.0
parser.add_argument("-p", "--percentile", action="store_true",
    help="Roll a random percentile (0.0 to 1.0). Now usable with any other option")

## Allow the user to sum the outcome of the throws
## When the argument is passed, no value needs to accompny it. It is stored as "True".
parser.add_argument("-a", "--add", action="store_true",
    help="Add the sum of the dice cast")

## END OF ARGUMENT PARSER ##

## Assign the args to a new object
## There is probably a better way of doing this
args = parser.parse_args()

## Argument assignemtn
number_of_sides = args.sides
number_of_dice  = args.dice

## METHODS ##

## The method for rolling x number of n sided dice.
## The defaut sizes for dice and sides are
def roll(dice, sides):
    _min    = 1
    _max    = sides
    rolls   = []

## NOTE ##
## This could also be done by rolling the values and storing then in an array,
## then having another method to loop through the array to print the values to
## the user. That may also increase the reusableability of the script for other
## applications and uses

    for i in range(dice):
        r = randint(_min, _max)
        print "The roll of die %d is %d" % ((i + 1), r)
        rolls.append(r)
    if args.add is not False:
        _sum = sum(rolls)
        print '=' * 5 ## Makes a break between the rolls and the sum
        print "The total of the rolls is %d" % _sum

def roll_percentile():
    i = random()
    percent = "%.2f" % i
    return percent

## END OF METHODS ##

## IMPLEMENTATION OF METHODS ##

## There might be a better way of doing this, but b/c there currently only two
## methods that need to be implemented, this is the best way I can think of
## Doing this.
if args.percentile is not True:
    roll(number_of_dice, number_of_sides)
else:
    print roll_percentile()

## END OF IMPLEMENTATION ##

