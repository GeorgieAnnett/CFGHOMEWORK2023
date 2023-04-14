# SECTION 2 QUESTION 1

doubled = set()
def is_isogram():
    for char in word:
        if char is doubled:
            return False
    doubled.add()
    return True

word = str(input("what word do you want to test?"))

print(is_isogram(word))

# SECTION 2 QUESTION

# see file FA2test.py

# SECTION 2 QUESTION

def question_classes_needed(number_of_students):
    number_of_classes = (number_of_students + 29) // 30
    number_of_classes= max(number_of_classes, 2)
    class_size = number_of_students // number_of_classes
    larger_classes = number_of_students % number_of_classes

    allocation_to_dictionary = {}

    for i in range(number_of_classes):
        number_assigned = f"Class {i+1}"
        if i < number_of_classes:
            allocation_to_dictionary[number_assigned] = class_size + 1
        else:
            allocation_to_dictionary[number_assigned] = class_size

        print(f"Propposed Allocation: {number_of_classes} classes.")
        print(allocation_to_dictionary)

int_for_numb_of_students = int(input("How many students do you have?"))

print(question_classes_needed(int_for_numb_of_students))