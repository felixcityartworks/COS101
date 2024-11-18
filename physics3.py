def get_input(prompt, value_type=int, positive=False):
    """Helper function to handle user input, ensure valid input, and optionally ensure positive values."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Oops! That's not a valid number. Please enter a whole number.")

def main():
    """Main function to run all calculations."""
    print("Welcome! Let's go through some physics calculations together!\n")

    #Pressure Calculation
    print("\nLet's calculate Pressure!")
    force = get_input("what is the force applied (in Netwons)?")
    area = get_input("what is the area covered (in square meters)? ")
    print(f"Pressure is: {force / area} Pascals.\n")

#Volume Calculaton
    print("Now, let's calculate Volume!")
    length = get_input("what is the length (in meters)? ")
    breadth = get_input("what is the breadth (in meters)? ")
    height = get_input("what is the height (in meters)? ")

    print(f"Volume is: {length * breadth * height} cubic meters.\n")

#Potential Energy Calculation
    print("Next, let's calculate Potential Energy!")
    mass = get_input("what is the mass (in kilograms)? ")
    gravity = get_input("what is the gravity (in meters per second squared)? ")
    height = get_input("what is the height (in meters)? ")

    print(f"Potential Energy is: {mass * gravity * height}Joules.\n")

# Work Done Calculation
    print("Time to calculate Work Done!")
    force = get_input("what is the force applied (in Newtons)? ")
    distance = get_input("what is the distance moved (in meters)? ")

    print(f"Work Done is: {force * distance} Joules.\n")

# Power calculation
    print(f"Finally, let's calculate Power!")
    work = get_input("what is the work done (in Joules)? ")
    time =get_input("what is the time taken (in seconds)? ")

    print(f"power is: {work / time} Watts.\n")

    print("You've completed all the calculations! Well done!\n")

#Run the Program
main()
