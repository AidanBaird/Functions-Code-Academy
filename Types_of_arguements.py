# Define out main function and populate it with our three destination variables
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

# Call the function and add the destinations
trip_planner("France", "Germany", "Denmark")

print("")

# Call the function again with different locations
trip_planner("Denmark", "France", "Germany")

print("")

# Call the function again with different locations and making sure to order them by using their specific variables
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")

print("")

# Call the function again with different locations but leave the final destination to be filled by default
trip_planner("Brooklyn", "Queens")