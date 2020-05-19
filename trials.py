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
    nums = []

    for i in range(start, stop):
        nums.append(i)


def censor_vowels(word):
    chars = []

    for letter in word:
        if 'aeiou'.includes(letter):
            chars.append('*')
        else:
            chars.append(letter)

    return chars.join('')


def snake_to_camel(string):
    camelCase = []

    for word in string.split('_'):
    camelCase.append("f{word[0].capitalize}{word[1].capitalize}")
  }

  return camelCase.join('')


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return result.join('')


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif (char === ')':
            parens -= 1

    if parens < 0:
        return false


def compress(string):
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char is not curr_char:
            compressed.append(curr_char)

    if char_count > 1:
        compressed.append(str(char_count))
        curr_char = char
        char_count = 0
    char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
