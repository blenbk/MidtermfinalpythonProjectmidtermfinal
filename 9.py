def days_since_birthday(birthday):
    """

    A function to calculate the number of days passed since the given birthday,

    excluding the days in the birth year and the current year.



    :param birthday: The birthday in the format "DD-MM-YYYY".

    :return: The number of days passed since the birthday (excluding the birth year and the current year).

    """

    # Extract day, month, and year from the birthday string

    day, month, year = map(int, birthday.split('-'))

    # Calculate the current year

    current_year = 2024  # Assuming the current year is 2024

    # Initialize a variable to store the total number of days

    total_days = 0

    # Iterate through the years between the birth year and the current year (exclusive)

    for y in range(year + 1, current_year):

        # Check if the current year is a leap year

        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):

            total_days += 366  # Add 366 days for leap years

        else:

            total_days += 365  # Add 365 days for non-leap years

    return total_days


# Example usage:

birthday = "10-01-2004"

print(days_since_birthday(birthday))  # Output: Number of days passed since the birthday