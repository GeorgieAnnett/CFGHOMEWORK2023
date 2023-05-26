# Q1

from collections import deque

queue = deque()

with open("hwk3_q1.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        command, name = line[0], line[1]

        if command == "JUMP":
            queue.insert(0, name)
        elif command == "JOIN":
            queue.append(name)

print(list(queue))

# Q2

# Time Complextiy - the splitting and extracting the command aspect of the code has a time complexity of O(1)
#                   the reading of the file has a time complexity of O(n) as running time grows larger with input
# Space Complexity - deque is O(1), the list used to store the queue is O(k) where k = number of people in queue

# Assumptions = the file is an acceptable/ readable size so memeory remains within its limits


# Q3

n = 1

def num_in_seq(n):
    if n < 1:
        return None
    if n == 1:
        return 8
    result = num_in_seq(n - 1) + 7
    print(result)
    return result

sequence_number = num_in_seq(n)
print(sequence_number)

# Q4

base_url = "https://codefirstgirls.com/"
current_url = base_url

options = {
    base_url: ["Courses", "Opportunities"],
    base_url + "courses": ["CFGDegree", "Back"],
    base_url + "opportunities": ["Ambassadors", "Back"],
    base_url + "courses/cfgdegree": ["Back"],
    base_url + "opportunities/ambassadors": ["Back"]}

while True:
    print("You are currently on the URL", current_url)
    print("Where are you clicking?")
    print("Options:", ', '.join(options[current_url]))

    choice = input("Enter your choice: ")

    if choice.lower() == "back":
        current_url = base_url
    elif choice.lower() in options[current_url]:
        current_url += choice.lower()

    print()

# Q4 - Time complexity = O(1) because the number of URLs and options are fixed
#      Space complexity = O(1) because the dictionary options and the variables base_url and current_url occupy a constant amount of memory
#       Assumptions = the number of URLs are only the ones given. So they are fixed.
#
#