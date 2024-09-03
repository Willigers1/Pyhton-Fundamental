def car(make, model, year):
    def display_info():
        print(f"Car Information: {year} {make} {model}")
    
    display_info()

# Initialize an empty list to store car details
car_list = []

while True:
    # Prompt the user to enter the make of the car
    make = input("Enter the make of the car (or type 'done' to finish): ")
    if make.lower() == "done":
        break
    
    # Prompt the user to enter the model of the car
    model = input("Enter the model of the car (or type 'done' to finish): ")
    if model.lower() == "done":
        break
    
    # Prompt the user to enter the year of the car
    year = input("Enter the year of the car (or type 'done' to finish): ")
    if year.lower() == "done":
        break
    
    # Add the car details as a tuple to the car_list
    car_list.append((make, model, year))

# Check if any cars were entered
if car_list:
    # Print the list of cars after the user is done
    print("\nList of cars entered:")
    for car_info in car_list:
        # Unpack the tuple and call the car function to display each car's information
        car(*car_info)
else:
    print("No cars were entered.")
