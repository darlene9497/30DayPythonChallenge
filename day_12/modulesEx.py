# Exercises: Day 12
# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits  # Includes uppercase and lowercase letters and digits
    random_id = ''.join(random.choices(characters, k=6))
    return random_id
random_user_id = generate_random_user_id()
print(random_user_id)
