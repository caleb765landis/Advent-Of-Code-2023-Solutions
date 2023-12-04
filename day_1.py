"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

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
ANSWERS AT BOTTOM
"""

# Simple Custom Exception Class
class CalibratiionValueException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# get Calibration Value for part one of the problem
def getCalVal(line=""):
    if len(line) == 0:
        raise CalibratiionValueException("ERROR: Line cannot be empty.")

    calVal = ""

    for char in line:
        if char.isdigit():
            calVal += char
            break

    # get last digit
    for char in line[::-1]:
        if char.isdigit():
            calVal += char
            break

    if len(calVal) != 2:
        raise CalibratiionValueException(
            "ERROR: Calibration Value must be a 2 digit number.")

    return int(calVal)


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
def getCalValStrs(line=""):
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
    with open("input/day_1_input.dat") as inf:
        pt1Sum = 0
        pt2Sum = 0

        for line in inf:
            line.rstrip()
            # handle errors if line doesn't have a two digit number
            try:
                # get calibration values
                pt1CalVal = getCalVal(line)
                pt2CalVal = getCalValStrs(line)

                # add calibration values to sum
                pt1Sum += pt1CalVal
                pt2Sum += pt2CalVal
            except CalibratiionValueException as e:
                print(e)


    print(f"Part 1 Sum: {pt1Sum}")
    print(f"Part 2 Sum: {pt2Sum}")


if __name__ == '__main__':
    main()

# PART 1 ANSWER: 55130
# PART 2 ANSWER: 54985
