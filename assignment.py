# A python program that prompts a user to enter a letter then checks whether
# it is a consonant or a vowel.
# A python program to check whether a number is prime or not

def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Example usage:
number = 59  # Replace with any number you want to check
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")




def check_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"

    # Check if the input is a single letter
    if len(letter) != 1:
        return "Invalid input: Please enter a single letter."

    # Check if the input is an alphabet letter
    if not letter.isalpha():
        return "Invalid input: Please enter an alphabet letter."

    # Check if the letter is a vowel or a consonant
    if letter in vowels:
        return f"The letter '{letter}' is a vowel."
    else:
        return f"The letter '{letter}' is a consonant."

# Prompt the user to enter a letter
letter = input("Enter a letter: ")

# Call the function to check if it's a vowel or consonant and print the result
result = check_vowel_or_consonant(letter)
print(result)
