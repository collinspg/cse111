import math
from datetime import datetime

#I'm using this funvtion to calculate the volume of tire to make my work easier

def calculate_tire_volume(width_of_tire, ratio_of_tire, diameter_of_tire_inches):
    volume_of_tire =   math.pi * (width_of_tire ** 2) * ratio_of_tire * (width_of_tire * ratio_of_tire + (2540 * diameter_of_tire_inches)) / 10000000000
    return volume_of_tire

#Get input values from the user and convert them into integers
width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))
ratio_of_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_of_tire_inches = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume_of_tire = calculate_tire_volume(width_of_tire, ratio_of_tire, diameter_of_tire_inches)
# Get the current date 
current_date = datetime.today()

#Open the file in append mode and write the data
with open("volumes.txt", mode="at") as textfile:
    textfile.write(f"Current date: {current_date:%Y-%m-%d}\n")
    textfile.write(f"Width of tire: {width_of_tire}\n")
    textfile.write(f"Ratio of tire: {ratio_of_tire}\n")
    textfile.write(f"Diameter of tire: {diameter_of_tire_inches}\n")
    textfile.write(f"Volume of tire: {volume_of_tire:.2f}\n")
print()
print(f"The approximate volume is: {volume_of_tire:.2f} litres")
print(f"{current_date:%Y-%m-%d}, {width_of_tire}, {ratio_of_tire}, {diameter_of_tire_inches}, {volume_of_tire:.2f}")

print()
#exceeding requirements
#Get user input decision on whether he/she wants to buy tire.
buy_tires = input("Do you want to buy tire with these dimensions? (yes/No): ")
if buy_tires.lower() == "yes":
    phone_number = input("Please enter your phone number: ")

# Store user phone information in the txt file
    with open("volumes.txt", mode="at") as textfile:
        textfile.write(f"Phone number: {phone_number}\n")


        print(f"\nThank you for sharing your phone number, it has been stored.")

else:
    print(f"\nThank you for sharing your dimensions only.")