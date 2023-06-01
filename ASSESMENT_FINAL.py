# Question 1 -
question_1 = input("what constanants would you like to count?")

def count_consonants(string):
    vowels = ['a','e','i','o','u']
    consonants = set()

    for charachter in string.lower():
        if charachter not in vowels:
            consonants.add(charachter)

    return len(consonants)

result = count_consonants(question_1)

print(result)

# Time Complexity: O(n) because
# Space Complexity:O(c) where c is the number of unique consonants in the string

# QUESTION 2 -

def count_squares(x):
    if x == 1:
        return 1
    else:
        return x * x + count_squares(x - 1)

# QUESTION 3 -

key = "abcde"

def basic_hash_function(key):
    hash_value = 0

    for character in key:
        hash_value += ord(character)

    final_hash_value = hash_value

    print(final_hash_value)

print(basic_hash_function(key))

# 1. abcde = key
# 2. my basic_hash_function is called whilst taking in the key as the input
# 3. a hash value is set initially to 0
# 4. iterates over key e.g. a = ASCII 97, b = ASCII 98, c = ASCII 99, d = ASCII 100, e = ASCII 101
# 5. So, when you add it all up together 0 + 97 + 98 + 99 + 100 + 101 = 495
# 6 this is made into the final_hash_value which has been told to be printed
# 7. there are no hash collisions here becasuse each value adds onto the hash value individually and the final value is calculated correctly

# 1. we can create a collision by changing the key
# 2. if the key was something like "aba" or "baa" the result would be the same hence a collison
# 3. our hash function here would add thier ASCII values together regardless of thier positions the output woud be the same

