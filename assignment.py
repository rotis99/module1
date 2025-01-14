# Question 1

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


# Question 2

def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    return sum([number ** 2 for number in numbers])


# Question 3

def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    >>> count_vowels("bcdfg")
    0
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)


# Question 4

def count_repeats(string):

    from collections import Counter

    char_count = Counter(string)  
    return sum(1 for char, count in char_count.items() if count > 1)