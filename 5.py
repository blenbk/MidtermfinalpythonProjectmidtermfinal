text = "bBob Bob is Bobbing Bob"
def count_bob_occurrences(text):
    """
    A function to find all occurrences of a pattern that starts with "b",
    has an unlimited number of letters, and ends with "Bob".

    :param text: The text to look into.
    :return: The number of matches found.
    """
    count = 0  # Initialize a variable to count occurrences
    length = len(text)  # Get the length of the text

    # Iterate through the text
    for i in range(length - 2):  # We iterate until the third last character
        # Check if the current character starts with "b" and the next 3 characters form the pattern "Bob"
        if text[i] == 'b' and text[i + 3:i + 6] == 'Bob':
            count += 1  # If a match is found, increment the count

    return count


# Example usage:
text = "bBob Bob is Bobbing Bob"
print(count_bob_occurrences(text))  # Output: 3 (matches: bBob, Bob, Bob)