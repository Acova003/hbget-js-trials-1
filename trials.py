"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for i in items:
        print(i)


def get_all_evens(nums):
    evenNums = []
    for i in nums:
        if nums % 2 == 0:
            evenNums.append(i)
    return evenNums


def get_odd_indices(items):
    result = []

    for i in items:
        if i % 2 is not 0:
            result.append(i)
    return result

def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    nums = [];

    for i in range(start, stop):
        nums.append(i)


def censor_vowels(word):
    chars = [];

    for letter in word:
        if 'aeiou'.includes(letter):
            chars.append(letter)

    return chars.join('')


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
