"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ANSWER AT BOTTOM
"""

from day_1_part_1 import getSum, CalibratiionValueException

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

# get Calibration Value for part two of the problem
def getCalVal(line=""):
    if len(line) == 0:
        raise CalibratiionValueException("ERROR: Line cannot be empty.")
    
    # find indexes for first and last appearances of an integer

    firstIntIndex = -1
    lastIntIndex = -1
    
    for i, char in enumerate(line):
        if char.isdigit():
            firstIntIndex = i
            first = char
            break

    # get last digit
    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            lastIntIndex = len(line) - i - 1
            last = char
            break

    # check if each number spelled out is in the line
    # if it's found in the line, we can also compare it with the current first and last number appearances

    for numStr, num in nums.items():
        # find first appearance of substr
        firstStrIndex = line.find(numStr)

        # find last appearance of substr
        lastStrIndex = line.rfind(numStr)

        # if numStr was found in the line
        if firstStrIndex != -1 or lastStrIndex != -1:
            # check if this is the first number that appears in the line

            # if firstIntIndex's value is -1, then this is the first number that has been found, so set it as the first number that appears
            if firstIntIndex == -1:
                first = str(num)
                firstIntIndex = firstStrIndex

            # otherwise first number that appears has already been found, 
            # so compare that first number's index with this index to see if this appears first
            # if this number's index is less than the current first appearing index, then this number appears first
            elif firstIntIndex > firstStrIndex:
                first = str(num)
                firstIntIndex = firstStrIndex

            # otherwise this spelled out number was found after another number in the list,
            # so now check if this is the last number that appears in the line

            # if lastIntIndex's value is -1, then this is the first number that has been found, so set it as the last number that appears
            if lastIntIndex == -1:
                last = str(num)
                lastIntIndex = lastStrIndex

            # otherwise last number that appears has already been found,
            # so compare that last number's index with this index to see if this appears last
            # if this number's index is greater than the current last appearing index, then this number appears after
            elif lastIntIndex < lastStrIndex:
                last = str(num)
                lastIntIndex = lastStrIndex
        

    calVal = ""
    calVal += first
    calVal += last

    if len(calVal) != 2:
        raise CalibratiionValueException(
            "ERROR: Calibration Value must be a 2 digit number.")
    
    return int(calVal)


def main():
    # read input file
    with open("day_1_input.dat") as inf:
        sum = getSum(inf, getCalVal)

    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()

# ANSWER: 54985
