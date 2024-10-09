
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
#########
    # Write your logic to generate 2 numbers between 1 and 6 here
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Sum 2 numbers
    # return sum to calling function
    return die1 + die2
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total = 0
    for _ in range(100):
        total += randDice()
        
    average = round(total / 100, 2)
    print("Average of dice rolls:", average)

if __name__ == "__main__":
    main()
# Jadon Anderstrom, 10/08/24, "Random Dice".
