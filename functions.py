import random


def my_print(something_to_print):
    lost_value = "Oh nooo"
    # This is where I send the something_to_print to a process outside python
    # ...

    # End (with no return)
    # return None


some_return_value = my_print("Start")
print(some_return_value)

some_value = None

if True:
    print(f"This depends on the if statement. Value in variable")
    print(f"This depends on the if statement. {some_value}")

is_light_on = False
my_object_on_street = "car"


def print_some_words(word):
    print(f"Inside view on the object: {my_object_on_street}")

    # Side effect #1
    print(f"This {word} is printed when function is called")

    # Side effect #2
    is_light_on = True
    some_inner_value = "I'm hidden"
    number = random.randint(1, 10)
    print(f"Inside the function is_light_on: {is_light_on}")
    print(f"Inner value: {some_inner_value}")
    return number


print(f"Outside object: {my_object_on_street}")
print(f"The light is {is_light_on}")

the_best_number = print_some_words("apple")
print(f"The light is {is_light_on}")

print(the_best_number)
print(print_some_words("pen"))

print("End")
