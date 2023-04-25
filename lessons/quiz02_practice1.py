"""Question 17-19 Practice Problems"""

def odd_and_even(nums: list[int]) -> list[int]:
    """Returns nums that are odd but at an even index."""
    result: list[int] = list()

    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            result.append(nums[i])

    return result


def value_exists(test_dict: dict[str,int], test_int: int) -> bool:
    """Returns true if the dictionary contains test_int."""
    for key in test_dict:
        if test_dict[key] == test_int:
            return True
        
    return False


def short_words(test_words: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    eligible_words: list[str] = []

    for word in test_words:
        if len(word) < 5:
            eligible_words.append(word)
        else:
            print(f"{word} is too long!")

    return eligible_words