import re


# A custom function to split based on one or multiple delimiters.
# If delimiters are not found, split based on numbers found.
def custom_split(input_str) -> list[str]:
    # find all delimiters, if any
    delimiters = re.findall(r"\[(.+?)\]", input_str)
    result = []

    # check if delimiters ar found
    if len(delimiters):
        # escape all characters in each delimiter
        split_patterns = map(re.escape, delimiters)
        # create a regex string to compile
        split_patterns = "|".join(split_patterns)

        # split the input string based on delimiters after the first new-line character
        input_str = input_str[input_str.index("\n") + 1 :]
        result = re.compile(split_patterns).split(input_str)

        # exclude empty strings, if any
        result = filter(lambda str: len(str) > 0, result)
    else:
        # find all numbers if delimiters are not found
        result = re.findall(r"-?[0-9]+", input_str)

    return result


def add(input: str) -> int:
    # base case if string is empty
    if input == "":
        return 0

    # using the custom split helper, map all string values to integers
    numbers = map(int, custom_split(input))
    # filter out numbers over 1000 and convert to list
    numbers = filter(lambda x: x <= 1000, numbers)
    numbers = list(numbers)

    # throw an exception if a negative number is found
    for number in numbers:
        if number < 0:
            raise Exception("negative numbers not allowed: " + str(number))

    # add all integers in the final list
    return sum(numbers)
