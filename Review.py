# Create function to welcome with a variable name
def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0", name)


# Call the function and add a name to the variable
trip_planner_welcome("Aidan")


# Create a function that estimated travel time to the nearest half an hour
def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


# Create a variable to store the number called from the function
estimate = estimated_time_rounded(0.51)


# Create a function that contains both location, destination, time and mode of transport whilst setting the default mode of transport to car
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in", origin)
    print("And you are traveling to", destination)
    print("You will be traveling by", mode_of_transport)
    print("It will take approximately", str(estimated_time), "hours")


# Call the function
destination_setup("House", "Other house", estimate, "Feet")

# Printing commands
# print(estimate)
