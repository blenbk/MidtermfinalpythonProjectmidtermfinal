import random



random_numbers = []



# Generate random numbers and append them to the list

for i in range(10):

    random_numbers.append(random.randint(1, 100))



# Remove numbers greater than 50 and replace others with "XX"

for i in range(len(random_numbers)):

    if random_numbers[i] > 50:

        random_numbers[i] = None  # Replace with None for removal later

    else:

        random_numbers[i] = "XX"  # Replace with "XX"



# Remove None elements (numbers greater than 50)

random_numbers = [x for x in random_numbers if x is not None]



# Print the list at the end

print(random_numbers)