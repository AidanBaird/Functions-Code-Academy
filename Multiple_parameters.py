# Create a function that will calculate the expenses of travel
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  # Create new variables for car_rental_total car_rental_rate and trip_time. Then add the equation to work out the car_rental_total
  car_rental_total = car_rental_rate * trip_time
  car_rental_rate = 0
  trip_time = 0
  # Create new variables for hotel_total hotel_rate and trip_time. Then add the equation to work out the hotel_total
  hotel_total = hotel_rate * trip_time - 10
  hotel_rate = 0
  # Print command for total expenses
  print(car_rental_total + hotel_total + plane_ticket_price)

# Add relevent prices/rates to calculate_expenses
calculate_expenses(200, 100, 100, 5)