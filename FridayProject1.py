# Define a function named madlib
def madlib():
    
    # Madlib template with placeholders
    template = "I've had a very {adjective} day. This morning, I dropped a box of {large_object_plural} on my {body_part}. Then, at lunch, I went to {restaurant} for their delicious {food}, but the waiter brought me {another_food}, which I was not hungry for. Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

    # Get user input for placeholders
    adjective = input("Enter an adjective: ")
    large_object_plural = input("Enter a plural form of a large object: ")
    large_object = input("Enter a large object: ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter a restaurant name: ")
    food = input("Enter a food item: ")
    another_food = input("Enter another food item: ")

    # Replace placeholders with user input
    madlib_story = template.format(
        adjective=adjective,
        large_object_plural=large_object_plural,
        body_part=body_part,
        restaurant=restaurant,
        food=food,
        large_object=large_object,
        another_food=another_food
    )

    # Print the completed madlib story
    print(madlib_story)

# Call the madlib function to generate the story
madlib()