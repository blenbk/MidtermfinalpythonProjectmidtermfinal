def is_valid_url(url):

    """

    A function to check if the passed parameter is a valid URL.



    :param url: The string to be checked.

    :return: True if the string is a valid URL, False otherwise.

    """

    # Check if the string starts with 'http://' or 'https://'

    if url.startswith('http://') or url.startswith('https://'):

        # Check if there is at least one character after 'http://' or 'https://'

        if len(url) > 7:

            return True

    return False



# Example usage:

print(is_valid_url("https://www.example.com"))  # Output: True

print(is_valid_url("http://example.com"))       # Output: True

print(is_valid_url("example.com"))              # Output: False